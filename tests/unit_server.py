import os
import sys

tests_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_root)
db_root = os.path.join(project_root,"db")
if(project_root not in sys.path): sys.path.insert(0,project_root)
if(db_root not in sys.path): sys.path.insert(0,db_root)

import	unittest
import	unittest.mock					as um
from	collections						import namedtuple
from	collections						import defaultdict
from	sqlite3							import connect
from	json							import dumps
from	server.handlers					import NavbowRequestHandler
from	server.handlers					import IndexHandler
from	server.handlers					import WordsHandler
from	server.handlers					import ViewerReceiverHandler
from	analyzer						import NavtexAnalyzer
from	db								import historydb_fetch_view
from	db								import historydb_fetch_control
from	pygwarts.magical.time_turner	import TimeTurner








class ServerCase(unittest.IsolatedAsyncioTestCase):

	maxDiff = None

	@classmethod
	def tearDownClass(cls):

		cls.connection.close()
		if os.path.isfile(cls.db_path): os.remove(cls.db_path)

	@classmethod
	def setUpClass(cls):

		cls.NA22 = os.path.join(tests_root, "msg", "NA22")
		cls.db_path = os.path.join(tests_root, "db_test.sqlite3")
		cls.connection = connect(cls.db_path)
		os.environ["DB_PATH"] = cls.db_path
		os.environ["WORDS_TABLE"] = "navbow_db_test"
		os.environ["HISTORY_VIEW_TABLE"] = "navbow_hvdb_test"
		os.environ["HISTORY_CONTROL_TABLE"] = "navbow_hcdb_test"


	async def test_NavbowRequestHandler_accept(self):

		handler = um.Mock()
		await NavbowRequestHandler.accept(handler,{ "OOH": "EEH" })

		self.assertEqual(handler.set_status.mock_calls[0],um.call(200))
		self.assertEqual(handler.set_header.mock_calls[0],um.call("Content-type","application/json"))
		self.assertEqual(handler.finish.mock_calls[0],um.call({ "OOH": "EEH" }))


	async def test_NavbowRequestHandler_deny(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy

			await NavbowRequestHandler.deny(handler, 400, "connection", "10.11.12.13")

			self.assertEqual(handler.set_status.mock_calls[0],um.call(400))
			self.assertEqual(handler.set_header.mock_calls[0],um.call("Content-type","application/json"))
			self.assertEqual(

				handler.finish.mock_calls[0],
				um.call({ "reason": "Your connection request denied by the server" })
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("connection denied for 10.11.12.13")
			)


	async def test_NavbowRequestHandler_deny_reason(self):

		handler = um.Mock()
		await NavbowRequestHandler.deny_reason(handler, 400, "connection", "not interesting")

		self.assertEqual(handler.set_status.mock_calls[0],um.call(400))
		self.assertEqual(handler.set_header.mock_calls[0],um.call("Content-type","application/json"))
		self.assertEqual(

			handler.finish.mock_calls[0],
			um.call({ "reason": "Your connection denied: not interesting" })
		)








	async def test_IndexHandler_get(self):

		with self.connection:

			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
			self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
					view TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)
			self.connection.execute("""
				INSERT INTO navbow_hvdb_test VALUES
					("OOH",{ts1},"127.0.0.2"),
					("EEH",{ts2},"127.0.0.1"),
					("AH",{ts3},"127.0.0.3")
				""".format(ts1=ts1, ts2=ts2, ts3=ts3)
			)
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)
			self.connection.execute("""
				INSERT INTO navbow_hcdb_test VALUES
					("OOH",{ts1},"127.0.0.2"),
					("EEH",{ts3},"127.0.0.1"),
					("AH",{ts2},"127.0.0.3")
				""".format(ts1=ts1, ts2=ts2, ts3=ts3)
			)

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.request = namedtuple("request",[ "remote_ip" ])("10.11.12.13")
			handler.hosts = { "10.11.12.13" }

			response = IndexHandler.get(handler)

			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call("index.html access granted for 10.11.12.13")
			)
			self.assertEqual(

				handler.render.mock_calls[0],
				um.call("index.html",content={ "view":[ "AH","OOH","EEH" ], "control":[ "AH","EEH","OOH" ]})
			)


	async def test_IndexHandler_get_restricted(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.request = namedtuple("request",[ "remote_ip" ])("10.11.12.13")
			handler.hosts = { "10.10.10.10" }

			response = IndexHandler.get(handler)

			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("index.html access denied for 10.11.12.13")
			)
			self.assertEqual(handler.render.mock_calls[0],um.call("restricted.html"))








	async def test_WordsHandler_get(self):

		with self.connection:

			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
			self.connection.execute(
				"""CREATE TABLE navbow_db_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					added REAL,
					source TEXT
				)"""
			)
			self.connection.execute(
				"""INSERT INTO navbow_db_test VALUES
					("OOH",{ts2},"127.0.0.2"),
					("EEH",{ts1},"127.0.0.1"),
					("AH",{ts3},"127.0.0.3")
				""".format(ts1=ts1, ts2=ts2, ts3=ts3)
			)

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.request = namedtuple("request",[ "remote_ip" ])("10.11.12.13")
			handler.hosts = { "10.11.12.13" }

			response = WordsHandler.get(handler)

			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call("words.html access granted for 10.11.12.13")
			)
			self.assertEqual(

				handler.render.mock_calls[0],
				um.call(

					"words.html",
					content=[

						( "OOH",ts2,"127.0.0.2" ),
						( "EEH",ts1,"127.0.0.1" ),
						( "AH",ts3,"127.0.0.3" )
					]
				)
			)


	async def test_WordsHandler_get_restricted(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.request = namedtuple("request",[ "remote_ip" ])("10.11.12.13")
			handler.hosts = { "10.10.10.10" }

			response = WordsHandler.get(handler)

			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("words.html access denied for 10.11.12.13")
			)
			self.assertEqual(handler.render.mock_calls[0],um.call("restricted.html"))


	async def test_WordsHandler_get_failed(self):

		with self.connection:
			self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.request = namedtuple("request",[ "remote_ip" ])("10.11.12.13")
			handler.hosts = { "10.11.12.13" }

			response = WordsHandler.get(handler)

			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call("words.html access granted for 10.11.12.13")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Database content was not fetched by route handler")
			)
			self.assertEqual(handler.render.mock_calls[0],um.call("words.html",content=[]))








	async def test_ViewerReceiverHandler_files(self):

		with self.connection:

			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=-2).epoch

			self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
			self.connection.execute(
				"""CREATE TABLE navbow_db_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					added REAL,
					source TEXT
				)"""
			)
			self.connection.execute(
				"""INSERT INTO navbow_db_test VALUES
						("UTC",{ts2},"127.0.0.2"),
						("MAR",{ts1},"127.0.0.1"),
						("NORWEGIAN",{ts3},"127.0.0.3"),
						("NAV",{ts3},"127.0.0.3"),
						("WARNING",{ts3},"127.0.0.3"),
						("CHART",{ts3},"127.0.0.3"),
						("AREA",{ts3},"127.0.0.3"),
						("IS",{ts3},"127.0.0.3"),
						("INOPERATIVE",{ts3},"127.0.0.3")
				""".format(ts1=ts1, ts2=ts2, ts3=ts3)
			)
			self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
					view TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)
			self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			os.environ["STATION_LITERAL"] = "N"
			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.hosts = { "10.11.12.13" }
			handler.broadcast = um.AsyncMock()
			handler.accept = um.AsyncMock()
			handler.form_view.return_value = "formed_view"
			Req = namedtuple("request",[ "remote_ip","files" ])
			with open(self.NA22,"rb") as F:
				handler.request = Req(

					"10.11.12.13",
					{
						"NA22": [{

							"filename":	"NA22",
							"body":		F.read()
						}]
					}
				)
			view = str(

				"1    ZCZC NA22\n"
				"2    110905 UTC MAR 19\n"
				"3    NORWEGIAN NAV. WARNING 184/2019\n"
				"4    CHART N36\n"
				"5    AREA GRIP\n"
				"6    HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE\n"
				"7    NNNN\n"
				"\nmessage is outdated"
				"\nunknown word \"GRIP\" at line 5"
				"\nunknown word \"HILBAAAN\" at line 6"
				"\nunknown word \"RACON\" at line 6"
			)

			await ViewerReceiverHandler.post(handler)

			self.assertEqual(handler.form_view.mock_calls[0],um.call(view))
			self.assertEqual(

				handler.broadcast.mock_calls[0],
				um.call("NA22",{ "view": "formed_view", "control": [ "GRIP","HILBAAAN","RACON" ]})
			)
			self.assertEqual(

				handler.accept.mock_calls[0],
				um.call(
					{
						"NA22": {
							"analysis": {
								"analysis": {

									"coords": { 6: { "63-12.0N": 1, "007-43.8E": 1 }},
									'alnums': { 4: { "N36": 1 }},
									"nums": {

										2: { "110905": 1, "19": 1 },
										3: { "184/2019": 1 }
									},
									"known": {

										6: { "INOPERATIVE": 1, "IS": 1 },
										3: { "WARNING": 1, "NORWEGIAN": 1, "NAV": 1 },
										4: { "CHART": 1 },
										2: { "MAR": 1, "UTC": 1 },
										5: { "AREA": 1 }
									},
									'unknown': {

										6: { "RACON": 1, "HILBAAAN": 1 },
										5: { "GRIP": 1 }
									},
									"punct": {},
									"header": ("N", "A", "22"),
									"DTG": 1552284300.0
								},
								"state": 127,
								"air": [
									["ZCZC", "NA22"],
									["110905", "UTC", "MAR", "19"],
									["NORWEGIAN", "NAV.", "WARNING", "184/2019"],
									["CHART", "N36"],
									["AREA", "GRIP"],
									["HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE"],
									["NNNN"]
								],
								"raw": [
									"ZCZC NA22",
									"110905 UTC MAR 19",
									"NORWEGIAN NAV. WARNING 184/2019",
									"CHART  N36",
									"AREA GRIP",
									"HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE",
									"NNNN",
									""
								]
							},
							"view": "formed_view"
						}
					}
				)
			)
			loggy.reset_mock()
			self.assertEqual(historydb_fetch_view(loggy=loggy),[ "formed_view" ])
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT view,discovered FROM navbow_hvdb_test ORDER BY 2 DESC")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 1 row from navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			self.assertEqual(

				historydb_fetch_control(loggy=loggy),
				[ "GRIP","HILBAAAN","RACON" ]
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_hcdb_test ORDER BY 1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 3 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	async def test_ViewerReceiverHandler_messages(self):

		with self.connection:

			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=-2).epoch

			self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
			self.connection.execute(
				"""CREATE TABLE navbow_db_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					added REAL,
					source TEXT
				)"""
			)
			self.connection.execute(
				"""INSERT INTO navbow_db_test VALUES
						("UTC",{ts2},"127.0.0.2"),
						("MAR",{ts1},"127.0.0.1"),
						("NORWEGIAN",{ts3},"127.0.0.3"),
						("NAV",{ts3},"127.0.0.3"),
						("WARNING",{ts3},"127.0.0.3"),
						("CHART",{ts3},"127.0.0.3"),
						("AREA",{ts3},"127.0.0.3"),
						("IS",{ts3},"127.0.0.3"),
						("INOPERATIVE",{ts3},"127.0.0.3")
				""".format(ts1=ts1, ts2=ts2, ts3=ts3)
			)
			self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
					view TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)
			self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			os.environ["STATION_LITERAL"] = "N"
			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.hosts = { "10.11.12.13" }
			handler.broadcast = um.AsyncMock()
			handler.accept = um.AsyncMock()
			handler.form_view.return_value = "formed_view"
			Req = namedtuple("request",[ "remote_ip","files","body" ])
			with open(self.NA22) as F:
				handler.request = Req(

					"10.11.12.13",
					None,
					dumps({ "messages":{ "NA22": F.read() }})
				)
			view = str(

				"1    ZCZC NA22\n"
				"2    110905 UTC MAR 19\n"
				"3    NORWEGIAN NAV. WARNING 184/2019\n"
				"4    CHART N36\n"
				"5    AREA GRIP\n"
				"6    HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE\n"
				"7    NNNN\n"
				"\nmessage is outdated"
				"\nunknown word \"GRIP\" at line 5"
				"\nunknown word \"HILBAAAN\" at line 6"
				"\nunknown word \"RACON\" at line 6"
			)

			await ViewerReceiverHandler.post(handler)

			self.assertEqual(handler.form_view.mock_calls[0],um.call(view))
			self.assertEqual(

				handler.broadcast.mock_calls[0],
				um.call("NA22",{ "view": "formed_view", "control": [ "GRIP","HILBAAAN","RACON" ]})
			)
			self.assertEqual(

				handler.accept.mock_calls[0],
				um.call(
					{
						"NA22": {
							"analysis": {
								"analysis": {

									"coords": { 6: { "63-12.0N": 1, "007-43.8E": 1 }},
									'alnums': { 4: { "N36": 1 }},
									"nums": {

										2: { "110905": 1, "19": 1 },
										3: { "184/2019": 1 }
									},
									"known": {

										6: { "INOPERATIVE": 1, "IS": 1 },
										3: { "WARNING": 1, "NORWEGIAN": 1, "NAV": 1 },
										4: { "CHART": 1 },
										2: { "MAR": 1, "UTC": 1 },
										5: { "AREA": 1 }
									},
									'unknown': {

										6: { "RACON": 1, "HILBAAAN": 1 },
										5: { "GRIP": 1 }
									},
									"punct": {},
									"header": ("N", "A", "22"),
									"DTG": 1552284300.0
								},
								"state": 127,
								"air": [
									["ZCZC", "NA22"],
									["110905", "UTC", "MAR", "19"],
									["NORWEGIAN", "NAV.", "WARNING", "184/2019"],
									["CHART", "N36"],
									["AREA", "GRIP"],
									["HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE"],
									["NNNN"]
								],
								"raw": [
									"ZCZC NA22",
									"110905 UTC MAR 19",
									"NORWEGIAN NAV. WARNING 184/2019",
									"CHART  N36",
									"AREA GRIP",
									"HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE",
									"NNNN",
									""
								]
							},
							"view": "formed_view"
						}
					}
				)
			)
			loggy.reset_mock()
			self.assertEqual(historydb_fetch_view(loggy=loggy),[ "formed_view" ])
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT view,discovered FROM navbow_hvdb_test ORDER BY 2 DESC")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 1 row from navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			self.assertEqual(

				historydb_fetch_control(loggy=loggy),
				[ "GRIP","HILBAAAN","RACON" ]
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_hcdb_test ORDER BY 1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 3 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	async def test_ViewerReceiverHandler_analysis(self):

		with self.connection:

			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=-2).epoch

			self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
			self.connection.execute(
				"""CREATE TABLE navbow_db_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					added REAL,
					source TEXT
				)"""
			)
			self.connection.execute(
				"""INSERT INTO navbow_db_test VALUES
						("UTC",{ts2},"127.0.0.2"),
						("MAR",{ts1},"127.0.0.1"),
						("NORWEGIAN",{ts3},"127.0.0.3"),
						("NAV",{ts3},"127.0.0.3"),
						("WARNING",{ts3},"127.0.0.3"),
						("CHART",{ts3},"127.0.0.3"),
						("AREA",{ts3},"127.0.0.3"),
						("IS",{ts3},"127.0.0.3"),
						("INOPERATIVE",{ts3},"127.0.0.3")
				""".format(ts1=ts1, ts2=ts2, ts3=ts3)
			)
			self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
					view TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)
			self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
					word TEXT UNIQUE NOT NULL PRIMARY KEY,
					discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
					source TEXT
				)"""
			)

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			os.environ["STATION_LITERAL"] = "N"
			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.hosts = { "10.11.12.13" }
			handler.broadcast = um.AsyncMock()
			handler.accept = um.AsyncMock()
			handler.form_view.return_value = "formed_view"
			Req = namedtuple("request",[ "remote_ip","files","body" ])
			analysis =  NavtexAnalyzer("N")(self.NA22)
			load = {
				"analysis": {
					"NA22": { "view": NavtexAnalyzer.pretty_air(analysis) }
				}
			}
			control = set()
			for words in analysis["analysis"]["unknown"].values(): control |= set(words)
			if control: load["analysis"]["NA22"]["control"] = sorted(control)
			handler.request = Req("10.11.12.13", None, dumps(load))
			view = str(

				"1    ZCZC NA22\n"
				"2    110905 UTC MAR 19\n"
				"3    NORWEGIAN NAV. WARNING 184/2019\n"
				"4    CHART N36\n"
				"5    AREA GRIP\n"
				"6    HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE\n"
				"7    NNNN\n"
				"\nmessage is outdated"
				"\nunknown word \"GRIP\" at line 5"
				"\nunknown word \"HILBAAAN\" at line 6"
				"\nunknown word \"RACON\" at line 6"
			)

			await ViewerReceiverHandler.post(handler)

			self.assertEqual(handler.form_view.mock_calls[0],um.call(view,corrupted=None))
			self.assertEqual(

				handler.broadcast.mock_calls[0],
				um.call("NA22",{ "view": "formed_view", "control": [ "GRIP","HILBAAAN","RACON" ]})
			)
			loggy.reset_mock()
			self.assertEqual(historydb_fetch_view(loggy=loggy),[ "formed_view" ])
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT view,discovered FROM navbow_hvdb_test ORDER BY 2 DESC")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 1 row from navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			self.assertEqual(

				historydb_fetch_control(loggy=loggy),
				[ "GRIP","HILBAAAN","RACON" ]
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_hcdb_test ORDER BY 1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 3 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	async def test_ViewerReceiverHandler_deny_body(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			os.environ["STATION_LITERAL"] = "N"
			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.hosts = { "10.11.12.13" }
			handler.deny = um.AsyncMock()
			Req = namedtuple("request",[ "remote_ip","files","body" ])
			handler.request = Req("10.11.12.13", None, dumps({ "OOH": "EEH" }))

			await ViewerReceiverHandler.post(handler)

			self.assertEqual(

				handler.deny.mock_calls[0],
				um.call(422, "data transfer", "10.11.12.13")
			)




	async def test_ViewerReceiverHandler_deny_host(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			os.environ["STATION_LITERAL"] = "N"
			loggy = irma.return_value
			handler = um.Mock()
			handler.loggy = loggy
			handler.hosts = { "10.11.12.14" }
			handler.deny = um.AsyncMock()
			Req = namedtuple("request",[ "remote_ip","files","body" ])
			handler.request = Req("10.11.12.13", None, dumps({ "OOH": "EEH" }))

			await ViewerReceiverHandler.post(handler)

			self.assertEqual(

				handler.deny.mock_calls[0],
				um.call(403, "data transfer", "10.11.12.13")
			)




	def test_form_timestamp(self):

		handler = um.Mock()
		p = TimeTurner()
		r = ViewerReceiverHandler.form_timestamp(handler)
		self.assertRegex(r,r"---- \w+ \w+ \d\d? \d{4} \d\d:\d\d:\d\d \(local time\)")


	def test_form_view_valid(self):

		handler = um.Mock()
		handler.form_timestamp.return_value = "formed"
		p = TimeTurner()
		r = ViewerReceiverHandler.form_view(handler,"view")
		self.assertEqual(r,"formed\n\nview")


	def test_form_view_valid_corrupted(self):

		handler = um.Mock()
		handler.form_timestamp.return_value = "formed"
		p = TimeTurner()
		r = ViewerReceiverHandler.form_view(handler,"view",corrupted=True)
		self.assertEqual(
			r,"formed\n\ncorrupted message\n\nview\n\n* must be checked in original file"
		)


	def test_form_view_invalid(self):

		handler = um.Mock()
		handler.form_timestamp.return_value = "formed"
		for invalid in (

			42, .69, True, False, None, ..., unittest, print,
			[ "view" ],( "view", ),{ "view" },{ "view": "view" }
		):
			self.assertIsNone(ViewerReceiverHandler.form_view(handler,invalid))
			self.assertIsNone(ViewerReceiverHandler.form_view(handler,invalid,corrupted=True))








if __name__ == "__main__" : unittest.main(verbosity=2)







