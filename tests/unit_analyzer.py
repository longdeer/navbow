import	os
import	unittest
import	NavtexBoWAnalyzer
from	NavtexBoWAnalyzer		 import Navanalyzer
from	NavtexBoWAnalyzer.header import B1
from	NavtexBoWAnalyzer.header import B2








class AnalyzerCase(unittest.TestCase):


	wd = os.path.join(NavtexBoWAnalyzer.__path__[0], "tests")
	maxDiff = None


	def test_valid_station_init(self):

		for station in B1:

			self.assertIsInstance(Navanalyzer(station), Navanalyzer)
			self.assertIsInstance(Navanalyzer(station.lower()), Navanalyzer)


	def test_invalid_station_init(self):

		for invalid in "YZ":

			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				Navanalyzer,
				invalid
			)
			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				Navanalyzer,
				invalid.lower()
			)


	def test_invalid_length_station(self):

		for i in range(0,len(B1) -1,2):

			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				Navanalyzer,
				B1[i:i+2]
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
				invalid
			)








	def test_A_valid_header(self):

		analyzer = Navanalyzer("A")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC A{subject}{str(i).zfill(2)}"))


	def test_B_valid_header(self):

		analyzer = Navanalyzer("B")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC B{subject}{str(i).zfill(2)}"))


	def test_C_valid_header(self):

		analyzer = Navanalyzer("C")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC C{subject}{str(i).zfill(2)}"))


	def test_D_valid_header(self):

		analyzer = Navanalyzer("D")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC D{subject}{str(i).zfill(2)}"))


	def test_E_valid_header(self):

		analyzer = Navanalyzer("E")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC E{subject}{str(i).zfill(2)}"))


	def test_F_valid_header(self):

		analyzer = Navanalyzer("F")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC F{subject}{str(i).zfill(2)}"))


	def test_G_valid_header(self):

		analyzer = Navanalyzer("G")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC G{subject}{str(i).zfill(2)}"))


	def test_H_valid_header(self):

		analyzer = Navanalyzer("H")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC H{subject}{str(i).zfill(2)}"))


	def test_I_valid_header(self):

		analyzer = Navanalyzer("I")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC I{subject}{str(i).zfill(2)}"))


	def test_J_valid_header(self):

		analyzer = Navanalyzer("J")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC J{subject}{str(i).zfill(2)}"))


	def test_K_valid_header(self):

		analyzer = Navanalyzer("K")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC K{subject}{str(i).zfill(2)}"))


	def test_L_valid_header(self):

		analyzer = Navanalyzer("L")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC L{subject}{str(i).zfill(2)}"))


	def test_M_valid_header(self):

		analyzer = Navanalyzer("M")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC M{subject}{str(i).zfill(2)}"))


	def test_N_valid_header(self):

		analyzer = Navanalyzer("N")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC N{subject}{str(i).zfill(2)}"))


	def test_O_valid_header(self):

		analyzer = Navanalyzer("O")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC O{subject}{str(i).zfill(2)}"))


	def test_P_valid_header(self):

		analyzer = Navanalyzer("P")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC P{subject}{str(i).zfill(2)}"))


	def test_Q_valid_header(self):

		analyzer = Navanalyzer("Q")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC Q{subject}{str(i).zfill(2)}"))


	def test_R_valid_header(self):

		analyzer = Navanalyzer("R")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC R{subject}{str(i).zfill(2)}"))


	def test_S_valid_header(self):

		analyzer = Navanalyzer("S")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC S{subject}{str(i).zfill(2)}"))


	def test_T_valid_header(self):

		analyzer = Navanalyzer("T")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC T{subject}{str(i).zfill(2)}"))


	def test_U_valid_header(self):

		analyzer = Navanalyzer("U")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC U{subject}{str(i).zfill(2)}"))


	def test_V_valid_header(self):

		analyzer = Navanalyzer("V")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC V{subject}{str(i).zfill(2)}"))


	def test_W_valid_header(self):

		analyzer = Navanalyzer("W")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC W{subject}{str(i).zfill(2)}"))


	def test_X_valid_header(self):

		analyzer = Navanalyzer("X")

		for subject in B2:
			for i in range(100):

				self.assertTrue(analyzer.is_valid_header(f"ZCZC X{subject}{str(i).zfill(2)}"))


	def test_invalid_header(self):

		analyzer = Navanalyzer("A")

		for invalid in (

			"ZCZC", int(), float(), bool(), None, ..., print, unittest, Navanalyzer,
			[ "ZCZC AB00" ],( "ZCZC AB00", ),{ "ZCZC AB00" },{ "header": "ZCZC AB00" }
		):
			self.assertFalse(analyzer.is_valid_header(invalid))








	def test_analysis_1(self):

		analyzer = Navanalyzer("W")
		result = analyzer.with_mapping(os.path.join(self.wd, "WZ29"), dict())
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 2)
		self.assertEqual(result.get("state"), 0)
		self.assertIsInstance(result.get("message"), str)
		self.assertIn("*", result.get("message"))


	def test_analysis_2(self):

		analyzer = Navanalyzer("J")
		result = analyzer.with_mapping(os.path.join(self.wd, "JA94"), dict())
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 3)
		self.assertEqual(result.get("state"), 109) # 1 + 4 + 8 + 32 + 64
		self.assertIsInstance(result.get("lines"), list)
		self.assertEqual(

			result.get("lines"),
			[
				[ "ZCZC", "JA94" ],
				[ "151930", "UTC", "FEB" ],
				[ "CANCEL", "GERMAN", "NAV", "WARN", "079/19" ],
				[ "NNNN" ]
			]
		)
		self.assertIsInstance(result.get("analysis"), dict)
		self.assertIn("coords", result["analysis"])
		self.assertIsInstance(result["analysis"]["coords"], dict)
		self.assertFalse(len(result["analysis"]["coords"]))
		self.assertIn("alnums", result["analysis"])
		self.assertIsInstance(result["analysis"]["alnums"], dict)
		self.assertFalse(len(result["analysis"]["alnums"]))
		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"]["151930"][1],1)
		self.assertEqual(result["analysis"]["nums"]["079/19"][2],1)
		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"]["UTC"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["FEB"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["CANCEL"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["GERMAN"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["NAV"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["WARN"][2],1)
		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))
		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))








if	__name__ == "__main__" : unittest.main(verbosity=2)







