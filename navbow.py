from sys		import argv
from argparse	import ArgumentParser








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
			"run Analyzer for provided strings as either pathnames or files text"
		)
	)
	current_args.add_argument(

		"-t", "--test",
		metavar="module",
		nargs="*",
		help=(
			"run tests for analyzer | server | client modules"
		)
	)
	current_args.add_argument(

		"-p", "--pipe",
		const="environment",
		metavar="address:port",
		nargs="?",
		help=(
			"when --analyze files issued with this flag, provided address:port will be used "
			"to send results to; if address:port omitted, it will be tried from .env file; "
			"using this flag with --server or --test will make no effect"
		)
	)
	current_call = current_args.parse_args()
	analyzer = current_call.analyzer
	server = current_call.server
	test = current_call.test


	match 0 ^bool(server) ^bool(analyzer) <<1 ^(test is not None) <<2:
		case 1:

			from asyncio	import run
			from server.app	import app

			if server == "environment" : run(app())
			else:
				try:

					addr,port = server.split(":")
					port = int(port)

				except:

					current_args.print_help()
					print("\n\n\nFailed to parse address and port for server!")
				else:
					run(app(addr, port))


		case 2:

			match current_call.pipe:
				case None:			print("running analyzer")
				case "environment":	print("running analyzer and piping to .env server")
				case _:

					try:

						addr,port = current_call.pipe.split(":")
						port = int(port)

					except:

						print("\n\n\nFailed to parse address and port for pipe, analyzer didn't worked!")
					else:
						print(f"running analyzer and piping to {addr}:{port}")

		case 4:

			if	"analyzer" in test:

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







