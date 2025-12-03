import os
import sys

tests_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_root)
db_root = os.path.join(project_root,"db")
if(project_root not in sys.path): sys.path.insert(0,project_root)
if(db_root not in sys.path): sys.path.insert(0,db_root)

import	unittest
import	unittest.mock					as um
from	sqlite3							import connect
from	db								import wordsdb_init
from	db								import wordsdb_match_set
from	db								import wordsdb_fetch
from	db								import wordsdb_remove
from	db								import wordsdb_add
from	db								import historydb_init_view
from	db								import historydb_fetch_view
from	db								import historydb_add_view
from	db								import historydb_init_control
from	db								import historydb_fetch_control
from	db								import historydb_add_control
from	db								import historydb_remove_control
from	pygwarts.magical.time_turner	import TimeTurner








class DatabaseCase(unittest.TestCase):

	maxDiff = None

	@classmethod
	def tearDownClass(cls):

		cls.connection.close()
		if os.path.isfile(cls.db_path): os.remove(cls.db_path)

	@classmethod
	def setUpClass(cls):

		cls.db_path = os.path.join(tests_root, "db_test.sqlite3")
		cls.connection = connect(cls.db_path)
		os.environ["DB_PATH"] = cls.db_path
		os.environ["WORDS_TABLE"] = "navbow_db_test"
		os.environ["HISTORY_VIEW_TABLE"] = "navbow_hvdb_test"
		os.environ["HISTORY_CONTROL_TABLE"] = "navbow_hcdb_test"


	def test_wordsdb_init(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

			self.assertEqual(

				wordsdb_fetch(loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_db_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test ORDER BY 2,1")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)

			loggy.reset_mock()
			self.assertIsNone(wordsdb_init(loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(

					"Constructed query: CREATE TABLE IF NOT EXISTS navbow_db_test ("
					"word TEXT UNIQUE NOT NULL PRIMARY KEY,"
					"added REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),"
					"source TEXT"
					")"
				)
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)

			loggy.reset_mock()
			self.assertEqual(wordsdb_fetch(loggy=loggy),"No rows found in navbow_db_test")
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test ORDER BY 2,1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("No rows found in navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_init_view(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")

			self.assertEqual(

				historydb_fetch_view(loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_hvdb_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT view,discovered FROM navbow_hvdb_test ORDER BY 2 DESC")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)

			loggy.reset_mock()
			self.assertIsNone(historydb_init_view(loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(

					"Constructed query: CREATE TABLE IF NOT EXISTS navbow_hvdb_test ("
					"view TEXT UNIQUE NOT NULL PRIMARY KEY,"
					"discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),"
					"source TEXT"
					")"
				)
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)

			loggy.reset_mock()
			self.assertEqual(historydb_fetch_view(loggy=loggy),"No rows found in navbow_hvdb_test")
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
				um.call("No rows found in navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_init_control(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")

			self.assertEqual(

				historydb_fetch_control(loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_hcdb_test"
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

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)

			loggy.reset_mock()
			self.assertIsNone(historydb_init_control(loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(

					"Constructed query: CREATE TABLE IF NOT EXISTS navbow_hcdb_test ("
					"word TEXT UNIQUE NOT NULL PRIMARY KEY,"
					"discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),"
					"source TEXT"
					")"
				)
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)

			loggy.reset_mock()
			self.assertEqual(historydb_fetch_control(loggy=loggy),"No rows found in navbow_hcdb_test")
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
				um.call("No rows found in navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_wordsdb_match_set_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
				self.connection.execute("CREATE TABLE navbow_db_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

			self.assertEqual(wordsdb_match_set({ "OOH", "EEH" },loggy=loggy),set())
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertIn(

				loggy.debug.mock_calls[1],
				[
					um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word IN ('OOH','EEH')"),
					um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word IN ('EEH','OOH')")
				]
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Matched 0 rows from navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_match_set_1matched(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
				self.connection.execute("CREATE TABLE navbow_db_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
				self.connection.execute("INSERT INTO navbow_db_test VALUES ('OOH'),('EEH')")

			self.assertEqual(wordsdb_match_set({ "OOH" },loggy=loggy),{ "OOH" })
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word IN ('OOH')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Matched 1 row from navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_match_set_2matched(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
				self.connection.execute("CREATE TABLE navbow_db_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
				self.connection.execute("INSERT INTO navbow_db_test VALUES ('OOH'),('EEH')")

			self.assertEqual(wordsdb_match_set({ "OOH", "EEH" },loggy=loggy),{ "OOH", "EEH" })
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertIn(

				loggy.debug.mock_calls[1],
				[
					um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word IN ('OOH','EEH')"),
					um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word IN ('EEH','OOH')")
				]
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Matched 2 rows from navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_match_set_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

			self.assertEqual(

				wordsdb_match_set({ "OOH", "EEH" },loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_db_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertIn(

				loggy.debug.mock_calls[1],
				[
					um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word IN ('OOH','EEH')"),
					um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word IN ('EEH','OOH')")
				]
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_wordsdb_fetch_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
				self.connection.execute(
					"""CREATE TABLE navbow_db_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""
				)

			self.assertEqual(wordsdb_fetch(loggy=loggy),"No rows found in navbow_db_test")
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test ORDER BY 2,1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("No rows found in navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_fetch_words(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=-2).epoch

			with self.connection:

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

			self.assertEqual(

				wordsdb_fetch(loggy=loggy),
				[
					( "AH", ts3, "127.0.0.3" ),
					( "OOH", ts2, "127.0.0.2" ),
					( "EEH", ts1, "127.0.0.1" )
				]
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test ORDER BY 2,1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 3 rows from navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_fetch_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

			self.assertEqual(

				wordsdb_fetch(loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_db_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test ORDER BY 2,1")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_wordsdb_remove_word(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=-2).epoch

			with self.connection:

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

			self.assertIsNone(wordsdb_remove("OOH",loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result: [('OOH',)]")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call("Constructed query: DELETE FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[4],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[5],
				um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[6],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("\"OOH\" removed from db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[7],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)

			loggy.reset_mock()
			response = wordsdb_fetch(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),2)
			self.assertIsInstance(response[0],tuple)
			self.assertIsInstance(response[1],tuple)
			self.assertIn(response[0][0],[ "EEH","AH" ])
			self.assertIsInstance(response[0][1],float)
			self.assertIn(response[0][2],[ "127.0.0.1","127.0.0.3" ])
			self.assertIn(response[1][0],[ "EEH","AH" ])
			self.assertIsInstance(response[1][1],float)
			self.assertIn(response[1][2],[ "127.0.0.1","127.0.0.3" ])
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test ORDER BY 2,1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 2 rows from navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_remove_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
				self.connection.execute(
					"""CREATE TABLE navbow_db_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""
				)

			self.assertEqual(wordsdb_remove("OOH",loggy=loggy),"\"OOH\" cannot be removed cause it is not in db")
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result: []")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("\"OOH\" cannot be removed cause it is not in db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_remove_absent(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch

			with self.connection:

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
							("EEH",{ts1},"127.0.0.1"),
							("AH",{ts2},"127.0.0.3")
					""".format(ts1=ts1, ts2=ts2)
				)

			self.assertEqual(wordsdb_remove("OOH",loggy=loggy),"\"OOH\" cannot be removed cause it is not in db")
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result: []")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("\"OOH\" cannot be removed cause it is not in db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_remove_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

			self.assertEqual(

				wordsdb_remove("OOH",loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_db_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_remove_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

			self.assertEqual(

				wordsdb_remove(69,loggy=loggy),
				"Invalid word type <class 'int'> to remove from db"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Invalid word type <class 'int'> to remove from db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_wordsdb_add(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
				self.connection.execute(
					"""CREATE TABLE navbow_db_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""
				)

			response = wordsdb_add("oOh", "127.0.0.1", loggy=loggy)
			self.assertIsInstance(response,tuple)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"OOH")
			self.assertIsInstance(response[1],float)
			self.assertEqual(response[2],"127.0.0.1")
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result: []")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[4],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[5],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test WHERE word='OOH'")
			)
			# SELECT query result omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("\"OOH\" successfully added to db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[7],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = wordsdb_fetch(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),1)
			self.assertIsInstance(response[0],tuple)
			self.assertEqual(response[0][0],"OOH")
			self.assertIsInstance(response[0][1],float)
			self.assertEqual(response[0][2],"127.0.0.1")
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added,source FROM navbow_db_test ORDER BY 2,1")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("Fetched 1 row from navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)



	def test_wordsdb_add_duplicate(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1)
			ts3 = TimeTurner(days=-2).epoch

			with self.connection:

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
					""".format(ts1=ts1, ts2=ts2.epoch, ts3=ts3)
				)

			self.assertEqual(

				wordsdb_add("OOH", "127.0.0.2", loggy=loggy),
				f"\"OOH\" in db since {ts2.Ymd_dashed}"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Query result: [('OOH', {ts2.epoch})]")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call(f"\"OOH\" in db since {ts2.Ymd_dashed}")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_add_duplicate_no_since(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")
				self.connection.execute(
					"""CREATE TABLE navbow_db_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added TEXT,
						source TEXT
					)"""
				)
				self.connection.execute(
					"""INSERT INTO navbow_db_test VALUES
							("OOH","{ts2}","127.0.0.2"),
							("EEH","{ts1}","127.0.0.1"),
							("AH","{ts3}","127.0.0.3")
					"""
				)

			self.assertEqual(

				wordsdb_add("OOH", "127.0.0.2", loggy=loggy),
				"\"OOH\" in db since when not determined"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result: [('OOH', '{ts2}')]")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("\"OOH\" in db since when not determined")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_add_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

			self.assertEqual(

				wordsdb_add("OOH", "127.0.0.1", loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_db_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT word,added FROM navbow_db_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_db_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_wordsdb_add_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_db_test")

			self.assertEqual(

				wordsdb_add(69, "127.0.0.1", loggy=loggy),
				"Invalid word type <class 'int'> to add to db"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Invalid word type <class 'int'> to add to db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_historydb_fetch_view(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute("""
					INSERT INTO navbow_hvdb_test VALUES
						("OOH",{ts2},"127.0.0.2"),
						("EEH",{ts1},"127.0.0.1"),
						("AH",{ts3},"127.0.0.3")
					""".format(ts1=ts1, ts2=ts2, ts3=ts3)
				)

			self.assertEqual(historydb_fetch_view(loggy=loggy),[ "AH","EEH","OOH" ])
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
				um.call("Fetched 3 rows from navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_fetch_view_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(historydb_fetch_view(loggy=loggy),"No rows found in navbow_hvdb_test")
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
				um.call("No rows found in navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_fetch_view_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")

			self.assertEqual(

				historydb_fetch_view(loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_hvdb_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_hvdb_test")
			)








	def test_historydb_add_view_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_view("OOH", "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 symbols view successfully added to db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call("Constructed query: SELECT COUNT(*) FROM navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[4],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[5],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_view(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),1)
			self.assertEqual(response[0],"OOH")
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


	def test_historydb_add_view_not_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute("""
					INSERT INTO navbow_hvdb_test VALUES
						("EEH",{ts2},"127.0.0.1"),
						("AH",{ts3},"127.0.0.3")
					""".format(ts2=ts2, ts3=ts3)
				)

			self.assertIsNone(historydb_add_view("OOH", "127.0.0.2", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 symbols view successfully added to db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call("Constructed query: SELECT COUNT(*) FROM navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[4],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[5],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_view(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"OOH")
			self.assertEqual(response[2],"EEH")
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
				um.call("Fetched 3 rows from navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_view_overflow(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute(
					"INSERT INTO navbow_hvdb_test (view,source) VALUES %s"%(
						",".join( f"('{str(i).zfill(5)}','127.0.0.{i}')" for i in range(1,101) )
					)
				)

			self.assertIsNone(historydb_add_view("OOH", "127.0.0.102", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 symbols view successfully added to db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call("Constructed query: SELECT COUNT(*) FROM navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[4],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[5],
				um.call(

					"Constructed query: "
					"DELETE FROM navbow_hvdb_test WHERE (view,discovered) IN ("
					"SELECT view,discovered FROM navbow_hvdb_test ORDER BY 2 LIMIT 1"
					")"
				)
			)
			self.assertEqual(

				loggy.debug.mock_calls[6],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[7],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_view(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),100)
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
				um.call("Fetched 100 rows from navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_view_overflow_more(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute(
					"INSERT INTO navbow_hvdb_test (view,source) VALUES %s"%(
						",".join( f"('{str(i).zfill(5)}','127.0.0.{i}')" for i in range(1,110) )
					)
				)

			self.assertIsNone(historydb_add_view("OOH", "127.0.0.102", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 symbols view successfully added to db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call("Constructed query: SELECT COUNT(*) FROM navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[4],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[5],
				um.call(

					"Constructed query: "
					"DELETE FROM navbow_hvdb_test WHERE (view,discovered) IN ("
					"SELECT view,discovered FROM navbow_hvdb_test ORDER BY 2 LIMIT 10"
					")"
				)
			)
			self.assertEqual(

				loggy.debug.mock_calls[6],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.debug.mock_calls[7],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_view(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),100)
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
				um.call("Fetched 100 rows from navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_view_duplicate(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute("""
					INSERT INTO navbow_hvdb_test VALUES
						("OOH",{ts1},"127.0.0.1"),
						("EEH",{ts2},"127.0.0.2"),
						("AH",{ts3},"127.0.0.3")
					""".format(ts1=ts1, ts2=ts2, ts3=ts3)
				)

			self.assertEqual(

				historydb_add_view("OOH", "127.0.0.1", loggy=loggy),
				"Query failed due to IntegrityError: UNIQUE constraint failed: navbow_hvdb_test.view"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to IntegrityError: UNIQUE constraint failed: navbow_hvdb_test.view")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_view_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")

			self.assertEqual(

				historydb_add_view("OOH", "127.0.0.1", loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_hvdb_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_hvdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_view_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hvdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hvdb_test (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_add_view(69, "127.0.0.1", loggy=loggy),
				"Invalid view type <class 'int'> to add to db"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Invalid view type <class 'int'> to add to db")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_historydb_fetch_control(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute("""
					INSERT INTO navbow_hcdb_test VALUES
						("OOH",{ts2},"127.0.0.2"),
						("EEH",{ts3},"127.0.0.1"),
						("AH",{ts1},"127.0.0.3")
					""".format(ts1=ts1, ts2=ts2, ts3=ts3)
				)

			self.assertEqual(historydb_fetch_control(loggy=loggy),[ "AH","EEH","OOH" ])
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


	def test_historydb_fetch_control_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(historydb_fetch_control(loggy=loggy),"No rows found in navbow_hcdb_test")
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
				um.call("No rows found in navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_fetch_control_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")

			self.assertEqual(

				historydb_fetch_control(loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_hcdb_test"
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

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_historydb_add_control_empty_single_string(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_control("OOH", "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),1)
			self.assertEqual(response[0],"OOH")
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
				um.call("Fetched 1 row from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_empty_single_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_control({ "EEH" }, "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),1)
			self.assertEqual(response[0],"EEH")
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
				um.call("Fetched 1 row from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_empty_single_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_control([ "OOH" ], "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),1)
			self.assertEqual(response[0],"OOH")
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
				um.call("Fetched 1 row from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_empty_single_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_control(( "AH", ), "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),1)
			self.assertEqual(response[0],"AH")
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
				um.call("Fetched 1 row from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_empty_many_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_control({ "OOH", "EEH", "AH" }, "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_add_control_empty_many_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_control([ "OOH", "EEH", "AH" ], "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_add_control_empty_many_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertIsNone(historydb_add_control(( "OOH", "EEH", "AH" ), "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_add_control_not_empty_single_string(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control("TING", "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),4)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"TING")
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
				um.call("Fetched 4 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_not_empty_single_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control({ "TANG" }, "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),4)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"TANG")
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
				um.call("Fetched 4 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_not_empty_single_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control([ "WALLA" ], "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),4)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"WALLA")
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
				um.call("Fetched 4 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_not_empty_single_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control(( "WALLA", ), "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),4)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"WALLA")
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
				um.call("Fetched 4 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_not_empty_many_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control({ "WALLA", "BING", "BANG" }, "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),6)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"BANG")
			self.assertEqual(response[2],"BING")
			self.assertEqual(response[3],"EEH")
			self.assertEqual(response[4],"OOH")
			self.assertEqual(response[5],"WALLA")
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
				um.call("Fetched 6 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_not_empty_many_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control([ "TING", "TANG", "WALLA" ], "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),6)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"TANG")
			self.assertEqual(response[4],"TING")
			self.assertEqual(response[5],"WALLA")
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
				um.call("Fetched 6 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_not_empty_many_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control(( "WALLA", "BING", "BANG" ), "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),6)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"BANG")
			self.assertEqual(response[2],"BING")
			self.assertEqual(response[3],"EEH")
			self.assertEqual(response[4],"OOH")
			self.assertEqual(response[5],"WALLA")
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
				um.call("Fetched 6 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_duplicate_single_string(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control("OOH", "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_add_control_duplicate_single_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control({ "OOH" }, "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_add_control_duplicate_single_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control([ "OOH" ], "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_add_control_duplicate_single_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_add_control(( "OOH", ), "127.0.0.1", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_add_control_duplicate_many_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(
				historydb_add_control({ "OOH", "EEH", "TING", "TANG" }, "127.0.0.1", loggy=loggy)
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("4 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),5)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"TANG")
			self.assertEqual(response[4],"TING")
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
				um.call("Fetched 5 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_duplicate_many_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(
				historydb_add_control([ "OOH", "EEH", "TING", "TANG" ], "127.0.0.1", loggy=loggy)
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("4 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),5)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"TANG")
			self.assertEqual(response[4],"TING")
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
				um.call("Fetched 5 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_duplicate_many_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(
				historydb_add_control(( "OOH", "EEH", "TING", "TANG" ), "127.0.0.1", loggy=loggy)
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("4 control words adding processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),5)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
			self.assertEqual(response[3],"TANG")
			self.assertEqual(response[4],"TING")
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
				um.call("Fetched 5 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)




	def test_historydb_add_control_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")

			self.assertEqual(

				historydb_add_control("OOH", "127.0.0.1", loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_hcdb_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_add_control(69, "127.0.0.1", loggy=loggy),
				"Query failed due to TypeError: object of type 'int' has no len()"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: object of type 'int' has no len()")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_invalid_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_add_control({ 420,69 }, "127.0.0.1", loggy=loggy),
				"Query failed due to TypeError: can only concatenate str (not \"int\") to str"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: can only concatenate str (not \"int\") to str")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_invalid_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_add_control([ 420,69 ], "127.0.0.1", loggy=loggy),
				"Query failed due to TypeError: can only concatenate str (not \"int\") to str"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: can only concatenate str (not \"int\") to str")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_add_control_invalid_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_add_control(( 420,69 ), "127.0.0.1", loggy=loggy),
				"Query failed due to TypeError: can only concatenate str (not \"int\") to str"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			# INSERT query construction omitted cause of timestamp accuracy
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: can only concatenate str (not \"int\") to str")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








	def test_historydb_remove_control_not_empty_single_string(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control("OOH", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word='OOH'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),2)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
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
				um.call("Fetched 2 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_not_empty_single_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control({ "OOH" }, loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),2)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
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
				um.call("Fetched 2 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_not_empty_single_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control([ "OOH" ], loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),2)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
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
				um.call("Fetched 2 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_not_empty_single_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control(( "OOH", ), loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),2)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
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
				um.call("Fetched 2 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_not_empty_many_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute("""
					INSERT INTO navbow_hcdb_test VALUES
						("OOH",{ts2},"127.0.0.2"),
						("EEH",{ts1},"127.0.0.1"),
						("AH",{ts2},"127.0.0.3"),
						("TING",{ts1},"127.0.0.4"),
						("TANG",{ts1},"127.0.0.5"),
						("WALLA",{ts2},"127.0.0.6"),
						("BING",{ts1},"127.0.0.7"),
						("BANG",{ts1},"127.0.0.8")
					""".format(ts1=ts1, ts2=ts2)
				)

			self.assertIsNone(historydb_remove_control({ "OOH", "EEH", "AH" }, loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertIn(

				loggy.debug.mock_calls[1],
				[
					um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH','EEH','AH')"),
					um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH','AH','EEH')"),
					um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('EEH','OOH','AH')"),
					um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('EEH','AH','OOH')"),
					um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('AH','OOH','EEH')"),
					um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('AH','EEH','OOH')")
				]
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),5)
			self.assertEqual(response[0],"BANG")
			self.assertEqual(response[1],"BING")
			self.assertEqual(response[2],"TANG")
			self.assertEqual(response[3],"TING")
			self.assertEqual(response[4],"WALLA")
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
				um.call("Fetched 5 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_not_empty_many_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute("""
					INSERT INTO navbow_hcdb_test VALUES
						("OOH",{ts2},"127.0.0.2"),
						("EEH",{ts1},"127.0.0.1"),
						("AH",{ts2},"127.0.0.3"),
						("TING",{ts1},"127.0.0.4"),
						("TANG",{ts1},"127.0.0.5"),
						("WALLA",{ts2},"127.0.0.6"),
						("BING",{ts1},"127.0.0.7"),
						("BANG",{ts1},"127.0.0.8")
					""".format(ts1=ts1, ts2=ts2)
				)

			self.assertIsNone(historydb_remove_control([ "OOH", "EEH", "AH" ], loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH','EEH','AH')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),5)
			self.assertEqual(response[0],"BANG")
			self.assertEqual(response[1],"BING")
			self.assertEqual(response[2],"TANG")
			self.assertEqual(response[3],"TING")
			self.assertEqual(response[4],"WALLA")
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
				um.call("Fetched 5 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_not_empty_many_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)
				self.connection.execute("""
					INSERT INTO navbow_hcdb_test VALUES
						("OOH",{ts2},"127.0.0.2"),
						("EEH",{ts1},"127.0.0.1"),
						("AH",{ts2},"127.0.0.3"),
						("TING",{ts1},"127.0.0.4"),
						("TANG",{ts1},"127.0.0.5"),
						("WALLA",{ts2},"127.0.0.6"),
						("BING",{ts1},"127.0.0.7"),
						("BANG",{ts1},"127.0.0.8")
					""".format(ts1=ts1, ts2=ts2)
				)

			self.assertIsNone(historydb_remove_control(( "OOH", "EEH", "AH" ), loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH','EEH','AH')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),5)
			self.assertEqual(response[0],"BANG")
			self.assertEqual(response[1],"BING")
			self.assertEqual(response[2],"TANG")
			self.assertEqual(response[3],"TING")
			self.assertEqual(response[4],"WALLA")
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
				um.call("Fetched 5 rows from navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_absent_single_string(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control("TING", loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word='TING'")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_remove_control_absent_single_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control({ "TANG" }, loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('TANG')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_remove_control_absent_single_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control([ "TANG" ], loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('TANG')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_remove_control_absent_single_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control(( "WALLA", ), loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('WALLA')")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("1 control word removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_remove_control_absent_many_set(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control({ "TING", "TANG", "WALLA" }, loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertIn(

				loggy.debug.mock_calls[1],
				[
					um.call(
						"Constructed query: DELETE FROM navbow_hcdb_test "
						"WHERE word IN ('TING','TANG','WALLA')"
					),
					um.call(
						"Constructed query: DELETE FROM navbow_hcdb_test "
						"WHERE word IN ('TING','WALLA','TANG')"
					),
					um.call(
						"Constructed query: DELETE FROM navbow_hcdb_test "
						"WHERE word IN ('WALLA','TING','TANG')"
					),
					um.call(
						"Constructed query: DELETE FROM navbow_hcdb_test "
						"WHERE word IN ('WALLA','TANG','TING')"
					),
					um.call(
						"Constructed query: DELETE FROM navbow_hcdb_test "
						"WHERE word IN ('TANG','TING','WALLA')"
					),
					um.call(
						"Constructed query: DELETE FROM navbow_hcdb_test "
						"WHERE word IN ('TANG','WALLA','TING')"
					)
				]
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_remove_control_absent_many_list(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control([ "TING", "TANG", "WALLA" ], loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(
					"Constructed query: DELETE FROM navbow_hcdb_test "
					"WHERE word IN ('TING','TANG','WALLA')"
				)
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_remove_control_absent_many_tuple(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1).epoch
			ts3 = TimeTurner(days=1).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
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

			self.assertIsNone(historydb_remove_control(( "TING", "TANG", "WALLA" ), loggy=loggy))
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(
					"Constructed query: DELETE FROM navbow_hcdb_test "
					"WHERE word IN ('TING','TANG','WALLA')"
				)
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call("Query result no exception")
			)
			self.assertEqual(

				loggy.info.mock_calls[0],
				um.call("3 control words removing processed")
			)
			self.assertEqual(

				loggy.debug.mock_calls[3],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)
			loggy.reset_mock()
			response = historydb_fetch_control(loggy=loggy)
			self.assertIsInstance(response,list)
			self.assertEqual(len(response),3)
			self.assertEqual(response[0],"AH")
			self.assertEqual(response[1],"EEH")
			self.assertEqual(response[2],"OOH")
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


	def test_historydb_remove_control_reason(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:
				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")

			self.assertEqual(

				historydb_remove_control(( "OOH", "EEH", "AH" ), loggy=loggy),
				"Query failed due to OperationalError: no such table: navbow_hcdb_test"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: DELETE FROM navbow_hcdb_test WHERE word IN ('OOH','EEH','AH')")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to OperationalError: no such table: navbow_hcdb_test")
			)
			self.assertEqual(

				loggy.debug.mock_calls[2],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_single_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_remove_control(69, loggy=loggy),
				"Query failed due to TypeError: object of type 'int' has no len()"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: object of type 'int' has no len()")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_set_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_remove_control({ 420,69 }, loggy=loggy),
				"Query failed due to TypeError: can only concatenate str (not \"int\") to str"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: can only concatenate str (not \"int\") to str")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_list_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_remove_control([ 420,69 ], loggy=loggy),
				"Query failed due to TypeError: can only concatenate str (not \"int\") to str"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: can only concatenate str (not \"int\") to str")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)


	def test_historydb_remove_control_tuple_invalid(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS navbow_hcdb_test")
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS navbow_hcdb_test (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						discovered REAL NOT NULL DEFAULT (CURRENT_TIMESTAMP +0),
						source TEXT
					)"""
				)

			self.assertEqual(

				historydb_remove_control(( 420,69 ), loggy=loggy),
				"Query failed due to TypeError: can only concatenate str (not \"int\") to str"
			)
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.warning.mock_calls[0],
				um.call("Query failed due to TypeError: can only concatenate str (not \"int\") to str")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call(f"Closing connection to db: \"{self.db_path}\"")
			)








if __name__ == "__main__" : unittest.main(verbosity=2)







