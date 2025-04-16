import	unittest
from	NavtexBoWAnalyzer		 import Navanalyzer
from	NavtexBoWAnalyzer.header import B1
from	NavtexBoWAnalyzer.header import B2








class AnalyzerCase(unittest.TestCase):

	def test_valid_station_init(self):

		for station in B1:

			self.assertIsInstance(Navanalyzer(station, dict()), Navanalyzer)
			self.assertIsInstance(Navanalyzer(station.lower(), dict()), Navanalyzer)


	def test_invalid_station_init(self):

		for invalid in "YZ":

			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				Navanalyzer,
				invalid, dict()
			)
			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				Navanalyzer,
				invalid.lower(), dict()
			)


	def test_invalid_length_station(self):

		for i in range(0,len(B1) -1,2):

			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				Navanalyzer,
				B1[i:i+2], dict()
			)


	def test_invalid_type_station(self):

		for invalid in (

			420, 69., True, False, None, ..., print, unittest, Navanalyzer,
			[ "A" ],( "B", ),{ "C" },{ "station": "D" }
		):
			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				Navanalyzer,
				invalid, dict()
			)


	def test_invalid_BoW_init(self):

		for invalid in (

			int(), float(), bool(), None, ..., print, unittest, Navanalyzer,
			[ "dict" ],( "dict", ),{ "dict" }
		):

			self.assertRaisesRegex(

				AssertionError,
				"Uncompatible bag of words type",
				Navanalyzer,
				"A", invalid
			)








if	__name__ == "__main__" : unittest.main(verbosity=2)







