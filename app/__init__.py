from os						import getenv
from json					import loads
from asyncio				import Event
from .handlers				import IndexHandler
from .handlers				import WordRemoveHandler
from .handlers				import WordAcceptHandler
from .handlers				import NavbowWebSocketHandler
from .handlers				import ViewerReceiverHandler
from pygwarts.irma.contrib	import LibraryContrib
from tornado.web			import Application
from dotenv					import load_dotenv








load_dotenv()
history = dict()
control_sockets = dict()
hosts = loads(getenv("ACCESS_LIST"))
irma = LibraryContrib(

	handler=getenv("LOGGY_FILE"),
	init_name=getenv("APP_NAME"),
	init_level=getenv("LOGGY_LEVEL"),
	force_handover=getenv("LOGGY_HANDOVER")
)








async def app():

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
				r"/controller-ws-cast",
				NavbowWebSocketHandler,
				{
					"clients":	control_sockets,
					"hosts":	set(hosts.get("view",[])),
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
		# dev settings ################
		compiled_template_cache=False,#
		static_hash_cache=False,#######
		autoreload=True################
		# dev settings ################
	)
	app.listen(getenv("LISTEN_PORT"), getenv("LISTEN_ADDRESS"))
	await Event().wait()







