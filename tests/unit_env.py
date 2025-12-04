import os
import sys

tests_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_root)
db_root = os.path.join(project_root,"db")
if(project_root not in sys.path): sys.path.insert(0,project_root)
if(db_root not in sys.path): sys.path.insert(0,db_root)

import	unittest
from	json							import loads
from	analyzer.header					import B1
from	pygwarts.filch.nettherin		import is_valid_ip4
from	pygwarts.filch.transportclaw	import validate_port
from	dotenv							import load_dotenv








class EnvFileCase(unittest.TestCase):

	maxDiff = None

	@classmethod
	def setUpClass(cls): load_dotenv(os.path.join(project_root,".env"))
	def test_APP_NAME(self):

		self.assertIsNotNone(os.getenv("APP_NAME"))
		self.assertIsInstance(os.getenv("APP_NAME"),str)

	def test_APP_STATIC_FOLDER(self):

		self.assertIsNotNone(os.getenv("APP_STATIC_FOLDER"))
		self.assertTrue(os.path.isdir(os.getenv("APP_STATIC_FOLDER")))

	def test_APP_TEMPLATES_FOLDER(self):

		self.assertIsNotNone(os.getenv("APP_TEMPLATES_FOLDER"))
		self.assertTrue(os.path.isdir(os.getenv("APP_TEMPLATES_FOLDER")))

	def test_LISTEN_ADDRESS(self):

		self.assertIsNotNone(os.getenv("LISTEN_ADDRESS"))
		self.assertTrue(is_valid_ip4(os.getenv("LISTEN_ADDRESS")))

	def test_LISTEN_PORT(self):

		self.assertIsNotNone(os.getenv("LISTEN_PORT"))
		self.assertIsInstance(validate_port(os.getenv("LISTEN_PORT")),int)

	def test_SERVER_LOGGY(self):

		self.assertIsNotNone(os.getenv("SERVER_LOGGY"))
		self.assertTrue(os.path.isabs(os.getenv("SERVER_LOGGY")))

	def test_SERVER_LOGGY_HANDOVER(self):

		self.assertIsNotNone(os.getenv("SERVER_LOGGY_HANDOVER"))
		self.assertIn(os.getenv("SERVER_LOGGY_HANDOVER"),( "True","False" ))

	def test_SERVER_LOGGY_LEVEL(self):

		self.assertIsNotNone(os.getenv("SERVER_LOGGY_LEVEL"))
		self.assertIsInstance(validate_port(os.getenv("SERVER_LOGGY_LEVEL")),int)

	def test_STATION_LITERAL(self):

		self.assertIsNotNone(os.getenv("STATION_LITERAL"))
		self.assertIn(os.getenv("STATION_LITERAL"),B1)

	def test_ACCESS_LIST(self):

		self.assertIsNotNone(os.getenv("ACCESS_LIST"))
		access_list = loads(os.getenv("ACCESS_LIST"))
		self.assertIsInstance(access_list,dict)
		view = access_list.get("view")
		self.assertIsInstance(view,list)
		self.assertTrue(all(map(is_valid_ip4,view)))
		control = access_list.get("control")
		self.assertIsInstance(control,list)
		self.assertTrue(all(map(is_valid_ip4,control)))
		receive = access_list.get("receive")
		self.assertIsInstance(receive,list)
		self.assertTrue(all(map(is_valid_ip4,receive)))

	def test_DB_PATH(self):

		self.assertIsNotNone(os.getenv("DB_PATH"))
		self.assertTrue(os.path.isabs(os.getenv("DB_PATH")))

	def test_DB_LOGGY(self):

		self.assertIsNotNone(os.getenv("DB_LOGGY"))
		self.assertTrue(os.path.isabs(os.getenv("DB_LOGGY")))

	def test_DB_LOGGY_LEVEL(self):

		self.assertIsNotNone(os.getenv("DB_LOGGY_LEVEL"))
		self.assertIsInstance(validate_port(os.getenv("DB_LOGGY_LEVEL")),int)

	def test_DB_LOGGY_HANDOVER(self):

		self.assertIsNotNone(os.getenv("DB_LOGGY_HANDOVER"))
		self.assertIn(os.getenv("DB_LOGGY_HANDOVER"),( "True","False" ))

	def test_WORDS_TABLE(self):

		self.assertIsNotNone(os.getenv("WORDS_TABLE"))
		self.assertIsInstance(os.getenv("WORDS_TABLE"),str)

	def test_HISTORY_VIEW_TABLE(self):

		self.assertIsNotNone(os.getenv("HISTORY_VIEW_TABLE"))
		self.assertIsInstance(os.getenv("HISTORY_VIEW_TABLE"),str)

	def test_HISTORY_CONTROL_TABLE(self):

		self.assertIsNotNone(os.getenv("HISTORY_CONTROL_TABLE"))
		self.assertIsInstance(os.getenv("HISTORY_CONTROL_TABLE"),str)








if __name__ == "__main__" : unittest.main(verbosity=2)







