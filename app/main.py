from os						import getenv
from asyncio				import Event
from asyncio				import run
from handlers				import IndexHandler
from handlers				import NavbowWebSocketHandler
from handlers				import ViewerReceiverHandler
from pygwarts.irma.contrib	import LibraryContrib
from tornado.web			import Application
from dotenv					import load_dotenv








load_dotenv()
view_sockets = dict()
control_sockets = dict()
irma = LibraryContrib(init_name="navbow", init_level=10, force_handover=True)








async def main():

	app = Application(
		[
			( r"/", IndexHandler,{ "loggy": irma }),
			( r"/viewer-ws-cast", NavbowWebSocketHandler,{ "clients": view_sockets, "loggy": irma }),
			( r"/controller-ws-cast", NavbowWebSocketHandler,{ "clients": control_sockets, "loggy": irma }),
			(
				r"/ws-cast-receiver",
				ViewerReceiverHandler,
				{
					"viewers":		view_sockets,
					"controllers":	control_sockets,
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







