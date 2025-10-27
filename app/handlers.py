from uuid				import uuid1
from json				import loads
from json				import dumps
from typing				import Dict
from typing				import List
from typing				import Set
from datetime			import datetime
from tornado.web		import RequestHandler
from tornado.websocket	import WebSocketHandler








class NavbowRequestHandler(RequestHandler):

	def initialize(self, loggy): self.loggy = loggy
	def __getattribute__(self, name :str):

		attr = super().__getattribute__(name)
		if name == "loggy" : attr.handover(self)
		return attr


	async def restrict(self, operation :str, address :str):

		self.set_status(403)
		self.set_header("Content-type", "application/json")
		self.finish({ "reason": "Operation not not permitted for your address" })
		self.loggy.info(f"{operation} denied for {address}")




class MainHandler(NavbowRequestHandler):
	def initialize(self, history :Dict[str,List[str]], hosts :Set[str], loggy):

		self.history = history
		self.hosts = hosts
		self.loggy = loggy




class IndexHandler(MainHandler):
	async def get(self):

		if self.request.remote_ip not in self.hosts: return self.render("restricted.html")
		return self.render("index.html", history=self.history)




class WordRemoveHandler(MainHandler):
	async def put(self):

		src = self.request.remote_ip

		if src not in self.hosts : await self.restrict("word removing", src)
		else:

			word = loads(self.request.body).get("word")

			# DB magic goes here
			self.history["controls"].remove(word)
			self.loggy.info(f"{src} removed {word}")




class WordAcceptHandler(MainHandler):
	async def put(self):

		src = self.request.remote_ip

		if src not in self.hosts : await self.restrict("word accepting", src)
		else:

			word = loads(self.request.body).get("word")

			# DB magic goes here
			self.history["controls"].remove(word)
			self.loggy.info(f"{src} accepted {word}")




class ViewerReceiverHandler(NavbowRequestHandler):
	def initialize(	self,
					controllers	:Dict[str,RequestHandler],
					viewers		:Dict[str,RequestHandler],
					history		:Dict[str,List[str]],
					hosts		:Set[str],
					loggy
				):

		self.controllers = controllers
		self.viewers = viewers
		self.history = history
		self.hosts = hosts
		self.loggy = loggy

	async def post(self):

		src = self.request.remote_ip

		if src not in self.hosts : await self.restrict("data transfer", src)
		else:

			data = loads(self.request.body)
			control = data.get("control")
			view = data.get("view")

			self.loggy.info(f"received {len(view)} symbols from {src}")

			full_date = datetime.today().astimezone().strftime("%A %B %m %Y %H:%M:%S %Z (GMT%z)")
			view = f"---------- {full_date} ----------\n\n{view}"
			self.history.setdefault("views", list()).insert(0,view)

			for handler in self.viewers.values(): handler.write_message(view)
			if	control:

				current = sorted(control)
				state = set(self.history.get("controls",list()))
				self.history["controls"] = sorted(state | set(current))

				for handler in self.controllers.values(): handler.write_message(dumps(current))








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







