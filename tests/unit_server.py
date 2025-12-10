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
from	sqlite3							import connect
from	server.handlers					import NavbowRequestHandler
from	pygwarts.magical.time_turner	import TimeTurner








class ServerCase(unittest.IsolatedAsyncioTestCase):

	maxDiff = None
	@classmethod
	def setUpClass(cls):

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








if __name__ == "__main__" : unittest.main(verbosity=2)







