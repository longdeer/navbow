from asyncio	import run
from argparse	import ArgumentParser
from server.app	import app








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
	current_call = current_args.parse_args()
	analyzer = current_call.analyzer
	server = current_call.server
	test = current_call.test


	match 0 ^bool(server) ^bool(analyzer) *2 ^(test is not None) *4:
		case 1:

			if server == "environment" : run(app())
			else:
				try:

					addr,port = server.split(":")
					port = int(port)

				except:

					current_args.print_help()
					print("\n\n\nFailed to parse address and port for server!")

				else:	run(app(addr, port))


		case 2: print("running analyzer")
		case 4: print("running tests")
		case _:

			current_args.print_help()
			print("\n\n\nCan run only one of analyzer | server | test module in single call!")







