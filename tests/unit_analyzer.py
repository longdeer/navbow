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








	def test_A_valid_header(self):

		an = Navanalyzer("A", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC A{subject}{str(i).zfill(2)}"))


	def test_B_valid_header(self):

		an = Navanalyzer("B", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC B{subject}{str(i).zfill(2)}"))


	def test_C_valid_header(self):

		an = Navanalyzer("C", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC C{subject}{str(i).zfill(2)}"))


	def test_D_valid_header(self):

		an = Navanalyzer("D", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC D{subject}{str(i).zfill(2)}"))


	def test_E_valid_header(self):

		an = Navanalyzer("E", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC E{subject}{str(i).zfill(2)}"))


	def test_F_valid_header(self):

		an = Navanalyzer("F", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC F{subject}{str(i).zfill(2)}"))


	def test_G_valid_header(self):

		an = Navanalyzer("G", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC G{subject}{str(i).zfill(2)}"))


	def test_H_valid_header(self):

		an = Navanalyzer("H", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC H{subject}{str(i).zfill(2)}"))


	def test_I_valid_header(self):

		an = Navanalyzer("I", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC I{subject}{str(i).zfill(2)}"))


	def test_J_valid_header(self):

		an = Navanalyzer("J", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC J{subject}{str(i).zfill(2)}"))


	def test_K_valid_header(self):

		an = Navanalyzer("K", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC K{subject}{str(i).zfill(2)}"))


	def test_L_valid_header(self):

		an = Navanalyzer("L", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC L{subject}{str(i).zfill(2)}"))


	def test_M_valid_header(self):

		an = Navanalyzer("M", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC M{subject}{str(i).zfill(2)}"))


	def test_N_valid_header(self):

		an = Navanalyzer("N", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC N{subject}{str(i).zfill(2)}"))


	def test_O_valid_header(self):

		an = Navanalyzer("O", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC O{subject}{str(i).zfill(2)}"))


	def test_P_valid_header(self):

		an = Navanalyzer("P", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC P{subject}{str(i).zfill(2)}"))


	def test_Q_valid_header(self):

		an = Navanalyzer("Q", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC Q{subject}{str(i).zfill(2)}"))


	def test_R_valid_header(self):

		an = Navanalyzer("R", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC R{subject}{str(i).zfill(2)}"))


	def test_S_valid_header(self):

		an = Navanalyzer("S", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC S{subject}{str(i).zfill(2)}"))


	def test_T_valid_header(self):

		an = Navanalyzer("T", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC T{subject}{str(i).zfill(2)}"))


	def test_U_valid_header(self):

		an = Navanalyzer("U", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC U{subject}{str(i).zfill(2)}"))


	def test_V_valid_header(self):

		an = Navanalyzer("V", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC V{subject}{str(i).zfill(2)}"))


	def test_W_valid_header(self):

		an = Navanalyzer("W", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC W{subject}{str(i).zfill(2)}"))


	def test_X_valid_header(self):

		an = Navanalyzer("X", dict())

		for subject in B2:
			for i in range(100):

				self.assertTrue(an.is_valid_header(f"ZCZC X{subject}{str(i).zfill(2)}"))


	def test_invalid_header(self):

		an = Navanalyzer("A", dict())

		for invalid in (

			"ZCZC", int(), float(), bool(), None, ..., print, unittest, Navanalyzer,
			[ "ZCZC AB00" ],( "ZCZC AB00", ),{ "ZCZC AB00" },{ "header": "ZCZC AB00" }
		):
			self.assertFalse(an.is_valid_header(invalid))








	def test_BoW_state_int(self):

		bow = dict()
		an = Navanalyzer("B", bow)

		for i in range(-100,101):
			bow["WARNING"] = i

			if i: self.assertEqual(an.BoW_state("WARNING"),1)
			else: self.assertEqual(an.BoW_state("WARNING"),0)


	def test_BoW_state_obj(self):

		bow = dict()
		an = Navanalyzer("C", bow)

		for invalid in (

			"ZCZC", float(), True, None, ..., print, unittest, Navanalyzer,
			[ 1 ],( 1, ),{ 1 },{ "state": 1 }
		):
			bow["WARNING"] = invalid
			self.assertEqual(an.BoW_state("WARNING"),1)








if	__name__ == "__main__" : unittest.main(verbosity=2)







