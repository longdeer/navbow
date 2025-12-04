from os			import getenv
from sys		import argv
from sys		import exit
from argparse	import ArgumentParser
from dotenv		import load_dotenv








if	__name__ == "__main__":


	current_args = ArgumentParser(

		prog="Navtex bag of words analyzer",
		usage="nabow [-s]",
		description="Run and analyze",
		epilog="\n\nv1 2025-11-9\n",
	)
	current_args.add_argument(

		"-s", "--server",
		const="environment",
		metavar="address:port",
		nargs="?",
		help=(
			"run server app to manage db and control messages content;"
			"if supplied with argument like xxx.xxx.xxx.xxx:xxxx will bind to such address and port"
		)
	)
	current_args.add_argument(

		"-a", "--analyzer",
		metavar="path|text",
		nargs="+",
		help=(
			"run Analyzer for provided strings as either path names or files text"
		)
	)
	current_args.add_argument(

		"-t", "--test",
		metavar="module",
		nargs="*",
		help=(
			"run tests for analyzer | server | client | db modules by supplying corresponding "
			"words arguments, or by omitting arguments to run all tests; any other arguments "
			"will be ignored."
		)
	)
	current_args.add_argument(

		"-p", "--pretty",
		action="store_true",
		help=(
			"when --analyze issued with this flag, every successful analysis will be putted to "
			"\"pretty_air\" function to produce fancy output message; unsuccessful analysis "
			"means non-ASCII symbols were found and substituted with * so for such inputs "
			"message already formed."
		)
	)
	current_args.add_argument(

		"-u", "--upload",
		const="environment",
		metavar="address:port",
		nargs="?",
		help=(
			"when --analyze files issued with this argument, provided address:port will be used "
			"to send results to; if address:port omitted, it will be tried from .env file; "
			"using this argument with --server or --test will make no effect"

		)
	)
	current_call = current_args.parse_args()
	analyzer_state = current_call.analyzer
	server_state = current_call.server
	pretty_state = current_call.pretty
	upload_state = current_call.upload
	test_state = current_call.test
	load_dotenv()


	match 0 ^bool(server_state) ^bool(analyzer_state) <<1 ^(test_state is not None) <<2:
		case 1:

			from asyncio	import run
			from server		import app
			from db			import wordsdb_init
			from db			import historydb_init_view
			from db			import historydb_init_control

			if	server_state == "environment":

				wordsdb_init()
				historydb_init_view()
				historydb_init_control()
				run(app())
			else:
				try:

					addr,port = server_state.split(":")
					port = int(port)

				except:

					current_args.print_help()
					print("\n\n\nFailed to parse address and port for server!")
				else:
					wordsdb_init()
					historydb_init_view()
					historydb_init_control()
					run(app(addr, port))


		case 2:

			from analyzer	import NavtexAnalyzer
			from db			import wordsdb_init

			navanalyzer = NavtexAnalyzer(getenv("STATION_LITERAL"))
			wordsdb_init()
			analysis = {}

			for file in analyzer_state:

				current_analysis = navanalyzer(file)
				analysis[file] = current_analysis

				if	"analysis" in current_analysis and pretty_state:
					analysis[file]["pretty_air"] = navanalyzer.pretty_air(analysis[file])

			if	upload_state is not None:

				from requests	import post
				from json		import dumps

				load = { "data": { "analysis": {}}}
				target = load["data"]["analysis"]

				for file,analysis in analysis.items():
					if	"analysis" in analysis:

						target[file] = { "view": analysis.get("pretty_air", navanalyzer.pretty_air(analysis)) }
						control = set()
						for words in analysis["analysis"]["unknown"].values(): control |= set(words)
						if control : target[file]["control"] = sorted(control)
					else:
						target[file] = { "view": analysis.get("message") }
						target[file]["corrupted"] = True

				if	upload_state == "environment":

					load["url"] = f"http://{getenv('LISTEN_ADDRESS')}:{getenv('LISTEN_PORT')}/ws-cast-receiver"
				else:
					try:	addr,port = upload_state.split(":")
					except:

						print("\n\n\nFailed to parse address and port for upload, analyzer didn't worked!")
						exit(1)

					else:	load["url"] = f"http://{addr}:{port}/ws-cast-receiver"

				load["data"] = dumps(load["data"])
				print(post(**load).reason)
			else:
				print(analysis)

		case 4:

			for test_module in test_state or [ "analyzer", "server", "client" ]:
				if	test_module == "db":

					from tests.unit_db				import *

				if	test_module == "analyzer":

					from tests.unit_scanner			import *
					from tests.unit_header			import *
					from tests.unit_DTG				import *
					from tests.unit_numerical		import *
					from tests.unit_alphanumerical	import *
					from tests.unit_coordinates		import *
					from tests.unit_analyzer		import *

			import unittest
			unittest.main(verbosity=2, argv=[ argv[0] ])


		case _:

			current_args.print_help()
			print("\n\n\nCan run only one of analyzer | server | test module in single call!")







