from os				import getenv
from asyncio		import Event
from asyncio		import run
from tornado.web	import RequestHandler
from tornado.web	import Application
from dotenv			import load_dotenv








load_dotenv()








class Router(RequestHandler):
	def get(self): return self.render("index.html")








async def main():

	app = Application(

		[( r"/",Router )],
		template_path=getenv("APP_TEMPLATES_FOLDER"),
		static_path=getenv("APP_STATIC_FOLDER"),
		# dev settings ################
		compiled_template_cache=False,#
		static_hash_cache=False       #
		# dev settings ################
	)
	app.listen(getenv("LISTEN_PORT"), getenv("LISTEN_ADDRESS"))
	await Event().wait()








if	__name__ == "__main__" : run(main())







