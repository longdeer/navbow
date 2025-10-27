from os						import getenv
from json					import loads
from asyncio				import Event
from asyncio				import run
from handlers				import IndexHandler
from handlers				import WordRemoveHandler
from handlers				import WordAcceptHandler
from handlers				import NavbowWebSocketHandler
from handlers				import ViewerReceiverHandler
from pygwarts.irma.contrib	import LibraryContrib
from tornado.web			import Application
from dotenv					import load_dotenv








load_dotenv()
history = dict()
view_sockets = dict()
control_sockets = dict()
hosts = loads(getenv("ACCESS_LIST"))
irma = LibraryContrib(

	handler=getenv("LOGGY_FILE"),
	init_name=getenv("APP_NAME"),
	init_level=getenv("LOGGY_LEVEL"),
	force_handover=getenv("LOGGY_HANDOVER")
)








async def main():

	app = Application(
		[
			(
				r"/",
				IndexHandler,
				{
					"history":	history,
					"hosts":	set(hosts.get("view",[])),
					"loggy":	irma
				}
			),
			(
				r"/viewer-ws-cast",
				NavbowWebSocketHandler,
				{
					"clients":	view_sockets,
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
					"loggy":	irma
				}
			),
			(
				r"/controller-word-remove",
				WordRemoveHandler,
				{
					"history":	history,
					"hosts":	set(hosts.get("control",[])),
					"loggy":	irma
				}
			),
			(
				r"/controller-word-accept",
				WordAcceptHandler,
				{
					"history":	history,
					"hosts":	set(hosts.get("control",[])),
					"loggy":	irma
				}
			),
			(
				r"/ws-cast-receiver",
				ViewerReceiverHandler,
				{
					"controllers":	control_sockets,
					"viewers":		view_sockets,
					"hosts":		set(hosts.get("receive",[])),
					"history":		history,
					"loggy":		irma
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








if	__name__ == "__main__" : run(main())







