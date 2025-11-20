from os						import getenv
from json					import loads
from asyncio				import Event
from server.handlers		import IndexHandler
from server.handlers		import WordsHandler
from server.handlers		import NavbowWebSocketHandler
from server.handlers		import WordRemoveHandler
from server.handlers		import WordAcceptHandler
from server.handlers		import ViewerReceiverHandler
from server.handlers		import IndexHandler
from pygwarts.irma.contrib	import LibraryContrib
from tornado.web			import Application








history = { "view": list(), "control": list() }
control_sockets = dict()
hosts = loads(getenv("ACCESS_LIST",r"{}"))
irma = LibraryContrib(

	handler=getenv("SERVER_LOGGY"),
	init_name=getenv("APP_NAME"),
	init_level=getenv("SERVER_LOGGY_LEVEL"),
	force_handover=getenv("SERVER_LOGGY_HANDOVER")
)








async def app(outer_addr :str =None, outer_port :int =None):

	app = Application(
		[
			(
				r"/",
				IndexHandler,
				{
					"hosts":	set(hosts.get("view",[])),
					"history":	history,
					"loggy":	irma
				}
			),
			(
				r"/words",
				WordsHandler,
				{
					"hosts":	set(hosts.get("view",[])),
					"loggy":	irma
				}
			),
			(
				r"/controller-ws-cast",
				NavbowWebSocketHandler,
				{
					"clients":	control_sockets,
					"hosts":	set(hosts.get("view",[])),
					"history":	history,
					"loggy":	irma
				}
			),
			(
				r"/controller-word-remove",
				WordRemoveHandler,
				{
					"hosts":	set(hosts.get("control",[])),
					"history":	history,
					"loggy":	irma
				}
			),
			(
				r"/controller-word-accept",
				WordAcceptHandler,
				{
					"hosts":	set(hosts.get("control",[])),
					"history":	history,
					"loggy":	irma
				}
			),
			(
				r"/ws-cast-receiver",
				ViewerReceiverHandler,
				{
					"clients":	control_sockets,
					"hosts":	set(hosts.get("receive",[])),
					"history":	history,
					"loggy":	irma
				}
			)
		],
		template_path=getenv("APP_TEMPLATES_FOLDER"),
		static_path=getenv("APP_STATIC_FOLDER"),
	)
	app.listen(outer_port or getenv("LISTEN_PORT"), outer_addr or getenv("LISTEN_ADDRESS"))
	await Event().wait()







