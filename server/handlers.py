from os								import getenv
from uuid							import uuid1
from json							import loads
from typing							import Dict
from typing							import List
from typing							import Set
from typing							import Any
from asyncio						import Future
from functools						import partial
from analyzer						import NavtexAnalyzer
from db								import db_fetch
from db								import db_remove
from db								import db_accept
from pygwarts.magical.spells		import patronus
from pygwarts.magical.time_turner	import TimeTurner
from tornado.web					import RequestHandler
from tornado.websocket				import WebSocketHandler








class NavbowRequestHandler(RequestHandler):

	def initialize(self, loggy): self.loggy = loggy
	def __getattribute__(self, name :str):

		attr = super().__getattribute__(name)
		if name == "loggy" : attr.handover(self)
		return attr


	async def broadcast(self, item :str, load :Dict[Any,Any]):

		for client,socket in self.clients.items():

			self.loggy.info(f"Sending {item} to {client}")
			await socket.write_message(load)


	async def accept(self, load :Dict[str,Any]):

		self.set_status(200)
		self.set_header("Content-type", "application/json")
		self.finish(load)


	async def deny(self, code :int, operation :str, address :str):

		self.set_status(code)
		self.set_header("Content-type", "application/json")
		self.finish({ "reason": f"Your {operation} request denied by the server" })
		self.loggy.info(f"{operation} denied for {address}")


	async def deny_reason(self, code :int, operation :str, reason :str):

		self.set_status(code)
		self.set_header("Content-type", "application/json")
		self.finish({ "reason": f"Your {operation} denied: {reason}" })




class MainHandler(NavbowRequestHandler):
	def initialize(self, hosts :Set[str], history :Dict[str,List[str]], loggy):

		self.history = history
		self.hosts = hosts
		self.loggy = loggy




class IndexHandler(MainHandler):
	def get(self):

		src = self.request.remote_ip

		if	src not in self.hosts:

			self.loggy.info(f"index.html access denied for {src}")
			return self.render("restricted.html")

		self.loggy.debug(f"index.html access granted for {src}")
		return self.render("index.html", history=self.history)




class WordsHandler(NavbowRequestHandler):
	def initialize(self, hosts :Set[str], loggy):

		self.hosts = hosts
		self.loggy = loggy


	def get(self):

		src = self.request.remote_ip

		if	src not in self.hosts:

			self.loggy.info(f"words.html access denied for {src}")
			return self.render("restricted.html")

		self.loggy.debug(f"words.html access granted for {src}")
		if isinstance(words := db_fetch(self.loggy),list): return self.render("words.html", content=words)

		self.loggy.warning("Database content was not fetched by route handler")
		return self.render("words.html", content=[])




class WordRemoveHandler(MainHandler):
	async def delete(self):

		src = self.request.remote_ip

		if	src not in self.hosts:

			await self.deny(403, "word removing", src)
			return


		word = loads(self.request.body).get("word")
		self.loggy.debug(f"Received word to delete: {word}")


		if	(reason := db_remove(word, self.loggy)):

			await self.deny_reason(400, "word removing", reason)
			return




class WordAcceptHandler(MainHandler):
	async def put(self):

		src = self.request.remote_ip

		if src not in self.hosts : await self.deny(403, "word accepting", src)
		else:

			word = loads(self.request.body).get("word")

			if(reason := db_accept(word, self.loggy)): await self.deny_reason(400, "word accepting", reason)
			else:

				try:	self.history["control"].remove(word)
				except	ValueError : self.loggy.warning(f"{word} not found in controller history")
				except	Exception as E : self.loggy.error(f"Unexpected {patronus(E)}")
				else:	self.loggy.info(f"{src} accepted {word}")








class ViewerReceiverHandler(NavbowRequestHandler):
	def initialize(	self,
					clients	:Dict[str,RequestHandler],
					history	:Dict[str,List[str]],
					hosts	:Set[str],
					loggy
				):

		self.clients = clients
		self.history = history
		self.hosts = hosts
		self.loggy = loggy


	async def post(self):

		src = self.request.remote_ip

		if src not in self.hosts : await self.deny(403, "data transfer", src)
		else:

			# Received json must content a messages mapping of
			# file names with it's corresponding text content.
			#
			# Non-ASCII symbols transfer must raise no Exceptions in "JSON.loads"
			# parsing time, when it is obvious Exception when it will be read from file
			# without special encoding set. So for the transfer the further word scan
			# must account for such problem symbols.
			#
			# It is assumed that endpoint will receive either "data" json with "messages"/"analysis"
			# or uploaded binary "files" (not both).
			if	(raw := self.request.files):

				targets = { part[0]["filename"]: part[0]["body"] for part in raw.values() }
			else:
				body = loads(self.request.body)

				if	isinstance(targets := body.get("analysis"), dict):
					for name,content in targets.items():
						if	isinstance(content,dict):
							if	isinstance(view := content.get("view"),str):


								if content.get("corrupted"): view = self.form_corrupted(view)
								else: view = f"{self.form_timestamp()}\n\n{view}"


								self.history["view"].insert(0,view)
								load = { "view": view }


								if	isinstance((control := content.get("control")),list):

									total = sorted(set(self.history["control"]) | set(control))
									self.history["control"] = total
									load["control"] = control


								await self.broadcast(name,load)


							else:	self.loggy.warning(f"Invalid \"{name}\" view received")
						else:		self.loggy.warning(f"Invalid \"{name}\" content received")
					else:			return


				elif	(targets := body.get("messages")): pass
				else:	return await self.deny(422, "data transfer", src)


			analyzer = NavtexAnalyzer(getenv("STATION_LITERAL"))
			response = dict()


			for name,content in targets.items():

				analysis = analyzer(content)
				response[name] = analysis
				load = dict()

				match analysis:

					case { "message": view }:	load["view"] = self.form_corrupted(view)
					case { "analysis": res }:

						try:	pretty_view = analyzer.pretty_air(analysis)
						except	Exception as E:

							self.loggy.warning(f"failed to prettify {analysis} due to {patronus(E)}")

						else:

							load["view"] = f"{self.form_timestamp()}\n\n{pretty_view}"
							control = set()

							for words in res["unknown"].values(): control |= set(words)
							if	control:

								self.history["control"] = sorted(set(self.history["control"]) | control)
								load["control"] = sorted(control)

					case _:

						self.loggy.warning(f"Navtex analyzer returned invalid analysis for \"{name}\"")
						continue


				self.history["view"].insert(0,load["view"])
				await self.broadcast(name,load)


			return	await self.accept(response)




	def form_timestamp(self):

		"""
			Makes a current moment timestamp for message
		"""

		p = TimeTurner()
		return f"---- {p.A} {p.B} {int(p.d)} {p.Y} {p.H}:{p.M}:{p.S} (local time)"




	def form_corrupted(self, message :str) -> str | None :

		"""
			Make final message which will account for non-ASCII symbols. If "message" argument
			is a string, will wrap it with timestamp header and warning footer. Will return None
			otherwise.
		"""

		if	isinstance(message,str):
			return "%s\n\n%s\n\n%s\n\n%s"%(

				self.form_timestamp(),
				"corrupted message",
				message,
				"* must be checked in original file"
			)




	def Future_status(self, addr :str, client_uuid :str, future :Future):

		"""
			Takes Future object returned by "write_message" method of "WebSocketHandler" object
			and consider it's status. As this method designed to be added as a Future callback,
			the "future" is assumed to be done. Any result value will be considered success,
			cause in any other cases corresponding Exception must be raised, according to
			https://docs.python.org/3.12/library/asyncio-future.html#asyncio.Future.result
		"""

		future.result()
		self.loggy.info(f"sent to {addr} ({client_uuid})")








class NavbowWebSocketHandler(WebSocketHandler):
	def __getattribute__(self, name :str):

		attr = super().__getattribute__(name)
		if name == "loggy" : attr.handover(self)
		return attr


	def initialize(	self,
					clients	:Dict[str,RequestHandler],
					history	:Dict[str,List[str]],
					hosts	:Set[str],
					loggy
				):

		self.clients = clients
		self.history = history
		self.hosts = hosts
		self.loggy = loggy


	async def broadcast(self, item :str, load :Dict[Any,Any]):

		for client,socket in self.clients.items():

			self.loggy.info(f"Sending {item} to {client}")
			await socket.write_message(load)


	async def on_message(self, message :str):

		src = self.request.remote_ip

		if	src in self.hosts:
			match message.split(":"):

				case [ "forget",word ]:

					# Just removing "word" from "control" history
					try:	self.history["control"].remove(word)
					except	Exception as E: self.loggy.warning(f"Failed to forget \"{word}\" due to {patronus(E)}")
					else:

						self.loggy.info(f"\"{word}\" forgotten by {src} ({self.current_connection_uuid})")
						await self.broadcast("release",{ "released": word })

				case [ "accept",word ]:

					try:

						print(f"accepting {word}") # Imitating db query for now
						self.history["control"].remove(word)

					except	Exception as E: self.loggy.warning(f"Failed to accept \"{word}\" due to {patronus(E)}")
					else:

						self.loggy.info(f"\"{word}\" accepted by {src} ({self.current_connection_uuid})")
						await self.broadcast("release",{ "released": word })
				case _:	self.loggy.warning(f"Improper message received: {message}")

		else:

			self.close(1008, "Source address not allowed")
			self.loggy.info(f"denied websocket for {src}")


	def open(self):

		src = self.request.remote_ip

		if	src in self.hosts:

			self.current_connection_uuid = uuid1()
			self.clients[self.current_connection_uuid] = self
			self.loggy.info(f"opened websocket for {src} ({self.current_connection_uuid})")

		else:

			self.close(1008, "Source address not allowed")
			self.loggy.info(f"denied websocket for {src}")


	def on_close(self):

		if	hasattr(self, "current_connection_uuid"):

			del self.clients[self.current_connection_uuid]
			self.loggy.info(f"closed connection ({self.current_connection_uuid})")







