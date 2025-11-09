from uuid						import uuid1
from json						import loads
from typing						import Dict
from typing						import List
from typing						import Set
from asyncio					import Future
from datetime					import datetime
from functools					import partial
from server.db					import db_fetch
from server.db					import db_remove
from server.db					import db_accept
from pygwarts.magical.spells	import patronus
from tornado.web				import RequestHandler
from tornado.websocket			import WebSocketHandler








class NavbowRequestHandler(RequestHandler):

	def initialize(self, loggy): self.loggy = loggy
	def __getattribute__(self, name :str):

		attr = super().__getattribute__(name)
		if name == "loggy" : attr.handover(self)
		return attr


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

		if self.request.remote_ip not in self.hosts: return self.render("restricted.html")
		return self.render("index.html", history=self.history)




class WordsHandler(NavbowRequestHandler):
	def initialize(self, hosts :Set[str], loggy):

		self.hosts = hosts
		self.loggy = loggy


	def get(self):

		if self.request.remote_ip not in self.hosts: return self.render("restricted.html")
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

			# Received json must content a message string as "view" key and
			# optionaly a list of unknown words as strings "control".
			data = loads(self.request.body)
			view = data.get("view")
			control = data.get("control",list())


			if	not isinstance(view,str):

				await self.deny(422, "data transfer", src)
				return


			self.loggy.info(f"received {len(view)} view symbols from {src}")
			full_date = datetime.today().astimezone().strftime("%A %B %m %Y %H:%M:%S %Z (GMT%z)")
			view = f"---------- {full_date} ----------\n\n{view}"
			self.history.setdefault("views", list()).insert(0,view)
			wsm = { "view": view }


			if	isinstance(control,list) and all( isinstance(word,str) for word in control ):

				current = set(control)
				self.history["control"] = sorted(set(self.history.get("control",list())) | current)
				wsm["control"] = sorted(current)


			for client_uuid, socket_handler in self.clients.items():

				try:	socket_handler.write_message(wsm).add_done_callback(partial(self.Future_status, src, client_uuid))
				except	Exception as E : self.loggy.error(f"{src} ({client_uuid}) send failed due to {patronus(E)}")


	def Future_status(self, addr :str, client_uuid :str, future :Future):

		"""
			Takes Future object returned by "write_message" method of "WebSocketHandler" object
			and consider it's status. As this method designed to be added as a Future callback,
			the "future" is assumed to be done. Any result value will be considered success,
			cause in any other cases corresponding Excepetion must be raised, according to
			https://docs.python.org/3.12/library/asyncio-future.html#asyncio.Future.result
		"""

		future.result()
		self.loggy.info(f"sent to {addr} ({client_uuid})")








class NavbowWebSocketHandler(WebSocketHandler):
	def __getattribute__(self, name :str):

		attr = super().__getattribute__(name)
		if name == "loggy" : attr.handover(self)
		return attr


	def initialize(self, clients :Dict[str,RequestHandler], hosts :Set[str], loggy):

		self.clients = clients
		self.hosts = hosts
		self.loggy = loggy


	def open(self):

		src = self.request.remote_ip

		if	src in self.hosts:

			self.current_connection_uuid = uuid1()
			self.clients[self.current_connection_uuid] = self
			self.loggy.info(f"openned websocket for {src} ({self.current_connection_uuid})")

		else:

			self.close(1008, "Source address not allowed")
			self.loggy.info(f"denied websocket for {src}")


	def on_close(self):

		if	hasattr(self, "current_connection_uuid"):

			del self.clients[self.current_connection_uuid]
			self.loggy.info(f"closed connection ({self.current_connection_uuid})")







