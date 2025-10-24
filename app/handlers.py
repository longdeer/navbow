from uuid				import uuid1
from json				import loads
from typing				import Dict
from typing				import List
from datetime			import datetime
from tornado.web		import RequestHandler
from tornado.websocket	import WebSocketHandler








class NavbowRequestHandler(RequestHandler):

	def initialize(self, loggy): self.loggy = loggy
	def __getattribute__(self, name :str):

		attr = super().__getattribute__(name)
		if name == "loggy" : attr.handover(self)
		return attr


class IndexHandler(NavbowRequestHandler):
	def initialize(self, history :Dict[str,List[str]], loggy):

		self.history = history
		self.loggy = loggy

	def get(self):
		return self.render("index.html", history=self.history)


class ViewerReceiverHandler(NavbowRequestHandler):
	def initialize(	self,
					viewers		:Dict[str,RequestHandler],
					controllers	:Dict[str,RequestHandler],
					history		:Dict[str,List[str]],
					loggy
				):

		self.controllers = controllers
		self.viewers = viewers
		self.history = history
		self.loggy = loggy

	def post(self):

		data = loads(self.request.body)
		control = data.get("control")
		view = data.get("view")
		src = self.request.remote_ip

		self.loggy.info(f"received {len(view)} symbols from {src}")

		full_date = datetime.today().astimezone().strftime("%A %B %m %Y %H:%M:%S %Z (GMT%z)")
		view = f"---------- {full_date} ----------\n\n{view}"
		self.history.setdefault("views", list()).insert(0,view)

		for handler in self.viewers.values(): handler.write_message(view)
		if	control:
			for handler in self.controllers.values(): handler.write_message(control)








class NavbowWebSocketHandler(WebSocketHandler):
	def __getattribute__(self, name :str):

		attr = super().__getattribute__(name)
		if name == "loggy" : attr.handover(self)
		return attr

	def initialize(self, clients :Dict[str,RequestHandler], loggy):

		self.clients = clients
		self.loggy = loggy

	def open(self):

		self.current_connection_uuid = uuid1()
		ip = self.request.remote_ip
		self.loggy.info(f"openned websocket for {ip} ({self.current_connection_uuid})")
		self.clients[self.current_connection_uuid] = self

	def on_close(self):

		self.loggy.info(f"closing {self.current_connection_uuid}")
		del self.clients[self.current_connection_uuid]







