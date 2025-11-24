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
from	contextlib						import closing
from	db								import wordsdb_match_set
from	db								import wordsdb_fetch
from	db								import wordsdb_remove
from	db								import wordsdb_add
from	db								import historydb_fetch_view
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
		cls.words_table = "navbow_db_test"
		cls.history_view_table = "navbow_hvdb_test"


	def test_wordsdb_match_set_empty(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"CREATE TABLE %s (word TEXT UNIQUE NOT NULL PRIMARY KEY)"%self.words_table
				)

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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"CREATE TABLE %s (word TEXT UNIQUE NOT NULL PRIMARY KEY)"%self.words_table
				)
				self.connection.execute("INSERT INTO %s VALUES ('OOH'),('EEH')"%self.words_table)

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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"CREATE TABLE %s (word TEXT UNIQUE NOT NULL PRIMARY KEY)"%self.words_table
				)
				self.connection.execute("INSERT INTO %s VALUES ('OOH'),('EEH')"%self.words_table)

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
				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)

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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""%self.words_table
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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""%self.words_table
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
				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)

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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""%self.words_table
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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""%self.words_table
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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""%self.words_table
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
				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)

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
				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)

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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""%self.words_table
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



	def test_wordsdb_add_added(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:

			loggy = irma.return_value
			ts1 = TimeTurner().epoch
			ts2 = TimeTurner(days=-1)
			ts3 = TimeTurner(days=-2).epoch

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL,
						source TEXT
					)"""%self.words_table
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


	def test_wordsdb_add_added_no_since(self):

		with um.patch("pygwarts.irma.contrib.LibraryContrib") as irma:
			loggy = irma.return_value

			with self.connection:

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)
				self.connection.execute(
					"""CREATE TABLE %s (
						word TEXT UNIQUE NOT NULL PRIMARY KEY,
						added TEXT,
						source TEXT
					)"""%self.words_table
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
				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)

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
				self.connection.execute("DROP TABLE IF EXISTS %s"%self.words_table)

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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.history_view_table)
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS %s (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL NOT NULL DEFAULT CURRENT_TIMESTAMP,
						source TEXT
					)"""%self.history_view_table
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
				um.call("Constructed query: SELECT view,added FROM navbow_hvdb_test ORDER BY 2 DESC")
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

				self.connection.execute("DROP TABLE IF EXISTS %s"%self.history_view_table)
				self.connection.execute("""
					CREATE TABLE IF NOT EXISTS %s (
						view TEXT UNIQUE NOT NULL PRIMARY KEY,
						added REAL NOT NULL DEFAULT CURRENT_TIMESTAMP,
						source TEXT
					)"""%self.history_view_table
				)

			self.assertEqual(historydb_fetch_view(loggy=loggy),"No rows found in navbow_hvdb_test")
			self.assertEqual(

				loggy.debug.mock_calls[0],
				um.call(f"Established connection to db: \"{self.db_path}\"")
			)
			self.assertEqual(

				loggy.debug.mock_calls[1],
				um.call("Constructed query: SELECT view,added FROM navbow_hvdb_test ORDER BY 2 DESC")
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
				self.connection.execute("DROP TABLE IF EXISTS %s"%self.history_view_table)

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








if __name__ == "__main__" : unittest.main(verbosity=2)







