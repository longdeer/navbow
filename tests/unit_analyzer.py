import os
import sys

tests_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_root)
analyzer_root = os.path.join(project_root,"analyzer")
if(project_root not in sys.path): sys.path.insert(0,project_root)
if(analyzer_root not in sys.path): sys.path.insert(0,analyzer_root)

import	unittest
from	datetime						import datetime
from	sqlite3							import connect
from	contextlib						import closing
from	collections						import defaultdict
from	pygwarts.magical.time_turner	import TimeTurner
from	analyzer						import NavtexAnalyzer
from	header							import B1
from	header							import B2








class AnalyzerCase(unittest.TestCase):

	# Broken:
	# WZ29			+
	# Not sanit:
	# OL66			+
	# NA22			+
	# Bad EoS:
	# IA76			+
	# VA28			+
	# Bad header:
	# MZ56			+
	# Valid:
	# JA94			+
	# BA33
	# GA10
	# QA42			+
	# KA60
	# RA28
	# SE94			+
	maxDiff = None

	@classmethod
	def tearDownClass(cls):

		cls.connection.close()
		if os.path.isfile(cls.db_path): os.remove(cls.db_path)
		if os.path.isfile(cls.db_loggy_path): os.remove(cls.db_loggy_path)

	@classmethod
	def setUpClass(cls):

		cls.MZ56 = os.path.join(tests_root, "msg", "MZ56")
		cls.VA28 = os.path.join(tests_root, "msg", "VA28")
		cls.IA76 = os.path.join(tests_root, "msg", "IA76")
		cls.NA22 = os.path.join(tests_root, "msg", "NA22")
		cls.SE94 = os.path.join(tests_root, "msg", "SE94")
		cls.QA42 = os.path.join(tests_root, "msg", "QA42")
		cls.OL66 = os.path.join(tests_root, "msg", "OL66")
		cls.JA94 = os.path.join(tests_root, "msg", "JA94")
		cls.empty_file = os.path.join(tests_root, "msg", "empty")
		cls.spaces_file = os.path.join(tests_root, "msg", "spaces")
		cls.corrupted_file = os.path.join(tests_root, "msg", "WZ29")
		cls.db_path = os.path.join(tests_root, "analyzer_test.sqlite3")
		cls.db_loggy_path = os.path.join(tests_root, "analyzer_test.loggy")
		cls.connection = connect(cls.db_path)
		cls.pseudo_message = "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG"
		os.environ["DB_PATH"] = cls.db_path
		os.environ["DB_LOGGY"] = cls.db_loggy_path
		os.environ["WORDS_TABLE"] = "navbow_test"


	def test_valid_station_init(self):

		for station in B1:

			self.assertIsInstance(NavtexAnalyzer(station), NavtexAnalyzer)
			self.assertIsInstance(NavtexAnalyzer(station.lower()), NavtexAnalyzer)


	def test_invalid_station_init(self):

		for invalid in "YZ":

			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				NavtexAnalyzer,
				invalid
			)
			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				NavtexAnalyzer,
				invalid.lower()
			)


	def test_invalid_length_station(self):

		for i in range(0,len(B1) -1,2):

			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				NavtexAnalyzer,
				B1[i:i+2]
			)


	def test_invalid_type_station(self):

		for invalid in (

			420, 69., True, False, None, ..., print, unittest, NavtexAnalyzer,
			[ "A" ],( "B", ),{ "C" },{ "station": "D" }
		):
			self.assertRaisesRegex(

				AssertionError,
				"Invalid station literal",
				NavtexAnalyzer,
				invalid
			)








	def test_A_valid_header(self):

		analyzer = NavtexAnalyzer("A")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC A{subject}00"),
					( "A", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC A{subject}{number}"),
					( "A", subject, number )
				)


	def test_B_valid_header(self):

		analyzer = NavtexAnalyzer("B")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC B{subject}00"),
					( "B", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC B{subject}{number}"),
					( "B", subject, number )
				)


	def test_C_valid_header(self):

		analyzer = NavtexAnalyzer("C")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC C{subject}00"),
					( "C", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC C{subject}{number}"),
					( "C", subject, number )
				)


	def test_D_valid_header(self):

		analyzer = NavtexAnalyzer("D")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC D{subject}00"),
					( "D", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC D{subject}{number}"),
					( "D", subject, number )
				)


	def test_E_valid_header(self):

		analyzer = NavtexAnalyzer("E")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC E{subject}00"),
					( "E", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC E{subject}{number}"),
					( "E", subject, number )
				)


	def test_F_valid_header(self):

		analyzer = NavtexAnalyzer("F")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC F{subject}00"),
					( "F", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC F{subject}{number}"),
					( "F", subject, number )
				)


	def test_G_valid_header(self):

		analyzer = NavtexAnalyzer("G")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC G{subject}00"),
					( "G", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC G{subject}{number}"),
					( "G", subject, number )
				)


	def test_H_valid_header(self):

		analyzer = NavtexAnalyzer("H")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC H{subject}00"),
					( "H", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC H{subject}{number}"),
					( "H", subject, number )
				)


	def test_I_valid_header(self):

		analyzer = NavtexAnalyzer("I")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC I{subject}00"),
					( "I", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC I{subject}{number}"),
					( "I", subject, number )
				)


	def test_J_valid_header(self):

		analyzer = NavtexAnalyzer("J")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC J{subject}00"),
					( "J", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC J{subject}{number}"),
					( "J", subject, number )
				)


	def test_K_valid_header(self):

		analyzer = NavtexAnalyzer("K")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC K{subject}00"),
					( "K", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC K{subject}{number}"),
					( "K", subject, number )
				)


	def test_L_valid_header(self):

		analyzer = NavtexAnalyzer("L")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC L{subject}00"),
					( "L", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC L{subject}{number}"),
					( "L", subject, number )
				)


	def test_M_valid_header(self):

		analyzer = NavtexAnalyzer("M")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC M{subject}00"),
					( "M", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC M{subject}{number}"),
					( "M", subject, number )
				)


	def test_N_valid_header(self):

		analyzer = NavtexAnalyzer("N")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC N{subject}00"),
					( "N", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC N{subject}{number}"),
					( "N", subject, number )
				)


	def test_O_valid_header(self):

		analyzer = NavtexAnalyzer("O")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC O{subject}00"),
					( "O", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC O{subject}{number}"),
					( "O", subject, number )
				)


	def test_P_valid_header(self):

		analyzer = NavtexAnalyzer("P")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC P{subject}00"),
					( "P", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC P{subject}{number}"),
					( "P", subject, number )
				)


	def test_Q_valid_header(self):

		analyzer = NavtexAnalyzer("Q")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC Q{subject}00"),
					( "Q", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC Q{subject}{number}"),
					( "Q", subject, number )
				)


	def test_R_valid_header(self):

		analyzer = NavtexAnalyzer("R")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC R{subject}00"),
					( "R", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC R{subject}{number}"),
					( "R", subject, number )
				)


	def test_S_valid_header(self):

		analyzer = NavtexAnalyzer("S")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC S{subject}00"),
					( "S", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC S{subject}{number}"),
					( "S", subject, number )
				)


	def test_T_valid_header(self):

		analyzer = NavtexAnalyzer("T")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC T{subject}00"),
					( "T", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC T{subject}{number}"),
					( "T", subject, number )
				)


	def test_U_valid_header(self):

		analyzer = NavtexAnalyzer("U")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC U{subject}00"),
					( "U", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC U{subject}{number}"),
					( "U", subject, number )
				)


	def test_V_valid_header(self):

		analyzer = NavtexAnalyzer("V")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC V{subject}00"),
					( "V", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC V{subject}{number}"),
					( "V", subject, number )
				)


	def test_W_valid_header(self):

		analyzer = NavtexAnalyzer("W")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC W{subject}00"),
					( "W", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC W{subject}{number}"),
					( "W", subject, number )
				)


	def test_X_valid_header(self):

		analyzer = NavtexAnalyzer("X")

		for subject in B2:
			if	subject in "ABDL":

				self.assertEqual(

					analyzer.validate_header(f"ZCZC X{subject}00"),
					( "X", subject, "00" )
				)
			for i in range(1,100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.validate_header(f"ZCZC X{subject}{number}"),
					( "X", subject, number )
				)




	def test_A_invalid_header(self):

		analyzer = NavtexAnalyzer("A")

		for invalid in (

			"ZCZC", "ZCZC AB1", "ZCZC AB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC AB00" ],( "ZCZC AB00", ),{ "ZCZC AB00" },{ "header": "ZCZC AB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC A{subject}00"))


	def test_B_invalid_header(self):

		analyzer = NavtexAnalyzer("B")

		for invalid in (

			"ZCZC", "ZCZC BB1", "ZCZC BB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC BB00" ],( "ZCZC BB00", ),{ "ZCZC BB00" },{ "header": "ZCZC BB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC B{subject}00"))


	def test_C_invalid_header(self):

		analyzer = NavtexAnalyzer("C")

		for invalid in (

			"ZCZC", "ZCZC CB1", "ZCZC CB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC CB00" ],( "ZCZC CB00", ),{ "ZCZC CB00" },{ "header": "ZCZC CB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC C{subject}00"))


	def test_D_invalid_header(self):

		analyzer = NavtexAnalyzer("D")

		for invalid in (

			"ZCZC", "ZCZC DB1", "ZCZC DB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC DB00" ],( "ZCZC DB00", ),{ "ZCZC DB00" },{ "header": "ZCZC DB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC D{subject}00"))


	def test_E_invalid_header(self):

		analyzer = NavtexAnalyzer("E")

		for invalid in (

			"ZCZC", "ZCZC EB1", "ZCZC EB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC EB00" ],( "ZCZC EB00", ),{ "ZCZC EB00" },{ "header": "ZCZC EB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC E{subject}00"))


	def test_F_invalid_header(self):

		analyzer = NavtexAnalyzer("F")

		for invalid in (

			"ZCZC", "ZCZC FB1", "ZCZC FB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC FB00" ],( "ZCZC FB00", ),{ "ZCZC FB00" },{ "header": "ZCZC FB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC F{subject}00"))


	def test_G_invalid_header(self):

		analyzer = NavtexAnalyzer("G")

		for invalid in (

			"ZCZC", "ZCZC GB1", "ZCZC GB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC GB00" ],( "ZCZC GB00", ),{ "ZCZC GB00" },{ "header": "ZCZC GB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC G{subject}00"))


	def test_H_invalid_header(self):

		analyzer = NavtexAnalyzer("H")

		for invalid in (

			"ZCZC", "ZCZC HB1", "ZCZC HB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC HB00" ],( "ZCZC HB00", ),{ "ZCZC HB00" },{ "header": "ZCZC HB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC H{subject}00"))


	def test_I_invalid_header(self):

		analyzer = NavtexAnalyzer("I")

		for invalid in (

			"ZCZC", "ZCZC IB1", "ZCZC IB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC IB00" ],( "ZCZC IB00", ),{ "ZCZC IB00" },{ "header": "ZCZC IB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC I{subject}00"))


	def test_J_invalid_header(self):

		analyzer = NavtexAnalyzer("J")

		for invalid in (

			"ZCZC", "ZCZC JB1", "ZCZC JB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC JB00" ],( "ZCZC JB00", ),{ "ZCZC JB00" },{ "header": "ZCZC JB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC J{subject}00"))


	def test_K_invalid_header(self):

		analyzer = NavtexAnalyzer("K")

		for invalid in (

			"ZCZC", "ZCZC KB1", "ZCZC KB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC KB00" ],( "ZCZC KB00", ),{ "ZCZC KB00" },{ "header": "ZCZC KB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC K{subject}00"))


	def test_L_invalid_header(self):

		analyzer = NavtexAnalyzer("L")

		for invalid in (

			"ZCZC", "ZCZC LB1", "ZCZC LB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC LB00" ],( "ZCZC LB00", ),{ "ZCZC LB00" },{ "header": "ZCZC LB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC L{subject}00"))


	def test_M_invalid_header(self):

		analyzer = NavtexAnalyzer("M")

		for invalid in (

			"ZCZC", "ZCZC MB1", "ZCZC MB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC MB00" ],( "ZCZC MB00", ),{ "ZCZC MB00" },{ "header": "ZCZC MB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC M{subject}00"))


	def test_N_invalid_header(self):

		analyzer = NavtexAnalyzer("N")

		for invalid in (

			"ZCZC", "ZCZC NB1", "ZCZC NB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC NB00" ],( "ZCZC NB00", ),{ "ZCZC NB00" },{ "header": "ZCZC NB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC N{subject}00"))


	def test_O_invalid_header(self):

		analyzer = NavtexAnalyzer("O")

		for invalid in (

			"ZCZC", "ZCZC OB1", "ZCZC OB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC OB00" ],( "ZCZC OB00", ),{ "ZCZC OB00" },{ "header": "ZCZC OB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC O{subject}00"))


	def test_P_invalid_header(self):

		analyzer = NavtexAnalyzer("P")

		for invalid in (

			"ZCZC", "ZCZC PB1", "ZCZC PB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC PB00" ],( "ZCZC PB00", ),{ "ZCZC PB00" },{ "header": "ZCZC PB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC P{subject}00"))


	def test_Q_invalid_header(self):

		analyzer = NavtexAnalyzer("Q")

		for invalid in (

			"ZCZC", "ZCZC QB1", "ZCZC QB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC QB00" ],( "ZCZC QB00", ),{ "ZCZC QB00" },{ "header": "ZCZC QB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC Q{subject}00"))


	def test_R_invalid_header(self):

		analyzer = NavtexAnalyzer("R")

		for invalid in (

			"ZCZC", "ZCZC RB1", "ZCZC RB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC RB00" ],( "ZCZC RB00", ),{ "ZCZC RB00" },{ "header": "ZCZC RB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC R{subject}00"))


	def test_S_invalid_header(self):

		analyzer = NavtexAnalyzer("S")

		for invalid in (

			"ZCZC", "ZCZC SB1", "ZCZC SB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC SB00" ],( "ZCZC SB00", ),{ "ZCZC SB00" },{ "header": "ZCZC SB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC S{subject}00"))


	def test_T_invalid_header(self):

		analyzer = NavtexAnalyzer("T")

		for invalid in (

			"ZCZC", "ZCZC TB1", "ZCZC TB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC TB00" ],( "ZCZC TB00", ),{ "ZCZC TB00" },{ "header": "ZCZC TB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC T{subject}00"))


	def test_U_invalid_header(self):

		analyzer = NavtexAnalyzer("U")

		for invalid in (

			"ZCZC", "ZCZC UB1", "ZCZC UB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC UB00" ],( "ZCZC UB00", ),{ "ZCZC UB00" },{ "header": "ZCZC UB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC U{subject}00"))


	def test_V_invalid_header(self):

		analyzer = NavtexAnalyzer("V")

		for invalid in (

			"ZCZC", "ZCZC VB1", "ZCZC VB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC VB00" ],( "ZCZC VB00", ),{ "ZCZC VB00" },{ "header": "ZCZC VB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC V{subject}00"))


	def test_W_invalid_header(self):

		analyzer = NavtexAnalyzer("W")

		for invalid in (

			"ZCZC", "ZCZC WB1", "ZCZC WB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC WB00" ],( "ZCZC WB00", ),{ "ZCZC WB00" },{ "header": "ZCZC WB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC W{subject}00"))


	def test_X_invalid_header(self):

		analyzer = NavtexAnalyzer("X")

		for invalid in (

			"ZCZC", "ZCZC XB1", "ZCZC XB100", int(), float(), bool(), None, ..., print, unittest, NavtexAnalyzer,
			[ "ZCZC XB00" ],( "ZCZC XB00", ),{ "ZCZC XB00" },{ "header": "ZCZC XB00" }
		):
			self.assertIsNone(analyzer.validate_header(invalid))

		for subject in "CEFGHIJKVWXYZ": self.assertIsNone(analyzer.validate_header(f"ZCZC X{subject}00"))








	def test_states(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

		analyzer = NavtexAnalyzer("B")

		for state in list(range(97,112,2)):
			with self.subTest(state=state):

				self.assertEqual(

					analyzer(os.path.join(tests_root, "states", str(state))).get("state"),
					state
				)


		with self.connection : self.connection.execute("INSERT INTO navbow_test VALUES ('NAV')")
		for state in [ 0 ] + list(range(1,65,2)) + list(range(97,128,2)):
			with self.subTest(state=state):

				self.assertEqual(

					analyzer(os.path.join(tests_root, "states", str(state))).get("state"),
					state
				)


		with self.connection : self.connection.execute("INSERT INTO navbow_test VALUES ('UTC'),('DEC')")
		for state in list(range(81,96,2)):
			with self.subTest(state=state):

				self.assertEqual(

					analyzer(os.path.join(tests_root, "states", str(state))).get("state"),
					state
				)








	def test_analysis_empty_file(self):

		analyzer = NavtexAnalyzer("W")
		self.assertEqual(

			analyzer(self.empty_file),
			{
				"message":	None,
				"state":	0
			}
		)


	def test_analysis_empty_string(self):

		analyzer = NavtexAnalyzer("W")
		with open(self.empty_file) as F:

			self.assertEqual(

				analyzer(F.read()),
				{
					"message":	None,
					"state":	0
				}
			)


	def test_analysis_empty_bytes(self):

		analyzer = NavtexAnalyzer("W")
		with open(self.empty_file, "rb") as F:

			self.assertEqual(

				analyzer(F.read()),
				{
					"message":	None,
					"state":	0
				}
			)


	def test_analysis_spaces_file(self):

		analyzer = NavtexAnalyzer("W")
		self.assertEqual(

			analyzer(self.spaces_file),
			{
				"message":	None,
				"state":	0
			}
		)


	def test_analysis_spaces_string(self):

		analyzer = NavtexAnalyzer("W")
		with open(self.spaces_file) as F:

			self.assertEqual(

				analyzer(F.read()),
				{
					"message":	None,
					"state":	0
				}
			)


	def test_analysis_spaces_bytes(self):

		analyzer = NavtexAnalyzer("W")
		with open(self.spaces_file, "rb") as F:

			self.assertEqual(

				analyzer(F.read()),
				{
					"message":	None,
					"state":	0
				}
			)


	def test_analysis_pseudo(self):

		analyzer = NavtexAnalyzer("V")
		target = {
			"analysis": {

				"coords":	defaultdict(lambda : defaultdict(int)),
				"alnums":	defaultdict(lambda : defaultdict(int)),
				"nums":		defaultdict(lambda : defaultdict(int)),
				"known":	defaultdict(lambda : defaultdict(int)),
				"unknown":	defaultdict(lambda : defaultdict(int)),
				"punct":	defaultdict(lambda : defaultdict(int))

			},
			"state": 33,
			"air": [

				[ "OOH", "EEH" ],
				[ "OOH", "AH", "AH" ],
				[ "TING", "TANG" ],
				[ "WALLA", "WALLA", "BING", "BANG" ]
			],
			"raw": [

				"OOH EEH",
				"OOH AH AH",
				"TING TANG",
				"WALLA WALLA BING BANG"
			],
		}
		target["analysis"]["unknown"][2]["OOH"] = 1
		target["analysis"]["unknown"][2]["AH"] = 2
		target["analysis"]["unknown"][3]["TING"] = 1
		target["analysis"]["unknown"][3]["TANG"] = 1
		result = analyzer(self.pseudo_message)
		self.assertEqual(result["raw"],target["raw"])
		self.assertEqual(result["air"],target["air"])
		self.assertEqual(result["state"],target["state"])
		self.assertEqual(

			result["analysis"]["coords"],
			target["analysis"]["coords"]
		)
		self.assertEqual(

			result["analysis"]["alnums"],
			target["analysis"]["alnums"]
		)
		self.assertEqual(

			result["analysis"]["nums"],
			target["analysis"]["nums"]
		)
		self.assertEqual(

			result["analysis"]["known"],
			target["analysis"]["known"]
		)
		self.assertEqual(

			result["analysis"]["punct"],
			target["analysis"]["punct"]
		)
		self.assertEqual(

			result["analysis"]["unknown"],
			target["analysis"]["unknown"]
		)


	def test_analysis_WZ29_file(self):

		analyzer = NavtexAnalyzer("W")
		result = analyzer(self.corrupted_file)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 2)
		self.assertEqual(result.get("state"), 0)
		self.assertIsInstance(result.get("message"), str)
		self.assertIn("*", result.get("message"))


	def test_analysis_JA94_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

		analyzer = NavtexAnalyzer("J")
		result = analyzer(self.JA94)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 109) # 1 + 4 + 8 + 32 + 64
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
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
		self.assertEqual(result["analysis"]["nums"][2]["151930"],1)
		self.assertEqual(result["analysis"]["nums"][3]["079/19"],1)
		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["FEB"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["CANCEL"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["GERMAN"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["NAV"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["WARN"],1)
		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))
		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertFalse(len(result["analysis"]["punct"]))
		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "J","A","94" ))
		self.assertIn("DTG", result["analysis"])
		self.assertIsInstance(result["analysis"]["DTG"], float)
		self.assertEqual(

			TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
			f"02/15/{TimeTurner().format('%Y')} 1930"
		)




	def test_analysis_OL66_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("CANCEL")
			""")

		analyzer = NavtexAnalyzer("O")
		result = analyzer(self.OL66)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 63) # 1 + 2 + 4 + 8 + 16 + 32
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
			[
				[ "ZCZC", "OL66" ],
				[ "OL66" ],
				[ "FOSNNI", "SUBFACTS", "AND", "GUNFACTS", "WARNING", "(ALL", "TIMES", "UTC):" ],
				[ "1.", "DIVED", "SUBMARINE", "OPERATIONS", "IN", "PROGRESS:" ],
				[
					"INNER", "SOUND", "-", "INSIDE", "OF", "SKYE", "SOUTH", "OF",
					"RUBHA", "REIDH", "NORTH", "OF", "MALLAIG.", "BETWEEN"
				],
				[ "120600", "AND", "130700", "SEP." ],
				[ "2.", "LIVE", "GUNNERY", "FIRINGS", "IN", "PROGRESS:", "NIL." ],
				[
					"FULL", "DETAILS", "IN", "HM", "COASTGUARD", "RESCUE",
					"CENTRES", "VHF", "AND", "MF", "BROADCASTS", "OR", "CONTACT"
				],
				[ "CTF", "311", "PHONE", "(44)(0)1923", "956366." ],
				[ "CANCEL", "OL65" ],
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
		self.assertEqual(result["analysis"]["nums"][4]["1"],1)
		self.assertEqual(result["analysis"]["nums"][6]["120600"],1)
		self.assertEqual(result["analysis"]["nums"][6]["130700"],1)
		self.assertEqual(result["analysis"]["nums"][7]["2"],1)
		self.assertEqual(result["analysis"]["nums"][9]["311"],1)
		self.assertEqual(result["analysis"]["nums"][9]["44"],1)
		self.assertEqual(result["analysis"]["nums"][9]["0"],1)
		self.assertEqual(result["analysis"]["nums"][9]["1923"],1)
		self.assertEqual(result["analysis"]["nums"][9]["956366"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][2]["OL66"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["FOSNNI"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["SUBFACTS"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["GUNFACTS"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["WARNING"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["ALL"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["TIMES"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["UTC"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["DIVED"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["SUBMARINE"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["OPERATIONS"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["PROGRESS"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["INNER"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["INSIDE"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["OF"],3)
		self.assertEqual(result["analysis"]["unknown"][5]["SKYE"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["RUBHA"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["REIDH"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["NORTH"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["MALLAIG"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["BETWEEN"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["SEP"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["LIVE"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["GUNNERY"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["FIRINGS"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["PROGRESS"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["NIL"],1)

		self.assertEqual(result["analysis"]["unknown"][8]["FULL"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["DETAILS"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["HM"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["COASTGUARD"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["RESCUE"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["CENTRES"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["MF"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["BROADCASTS"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["OR"],1)

		self.assertEqual(result["analysis"]["unknown"][9]["PHONE"],1)

		self.assertEqual(result["analysis"]["unknown"][10]["OL65"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][5]["SOUND"],1)
		self.assertEqual(result["analysis"]["known"][5]["SOUTH"],1)
		self.assertEqual(result["analysis"]["known"][8]["CONTACT"],1)
		self.assertEqual(result["analysis"]["known"][9]["CTF"],1)

		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertFalse(len(result["analysis"]["punct"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "O","L","66" ))

		self.assertNotIn("DTG", result["analysis"])




	def test_analysis_QA42_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("UNTIL"),
				("FURTHER"),
				("FROM"),
				("UTC"),
				("CONDUCTING"),
				("UNDERWATER"),
				("GAS")
			""")

		analyzer = NavtexAnalyzer("Q")
		result = analyzer(self.QA42)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 125) # 1 + 4 + 8 + 16 + 32 + 64
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
			[
				[ "ZCZC", "QA42" ],
				[ "092240", "UTC", "JUN", "19" ],
				[ "SPLIT", "RADIO" ],
				[ "NAV", "WNG", "NR", "193/19" ],
				[ "N-ERN", "ADRIATIC", "-", "BRIJUNI", "-", "CHRT:100-16" ],
				[
					"UNTIL", "FURTHER", "NOTICEFROM", "0700", "LT", "TO", "1900",
					"LT", "(FROM", "0500", "UTC", "TO", "1700", "UTC)M/V"
				],
				[
					"REFUL", "CONDUCTING", "UNDERWATER", "GAS", "PIPELINE",
					"MAINTENANCE", "WORKS", "BETWEEN", "POSITIONS:"
				],
				[ "A)", "44", "543", "N", "-", "013", "487", "E" ],
				[ "B)", "44", "537", "N", "-", "013", "477", "E" ],
				[ "C)", "44", "530", "N", "-", "013", "455", "E" ],
				[ "D)", "44", "531", "N", "-", "013", "436", "E" ],
				[ "E)", "44", "508", "N", "-", "013", "386", "E" ],
				[ "CONTACT", "VHF", "CH", "16." ],
				[
					"NAVIGATION", "AND", "FISHING", "IN", "RADIUS", "05",
					"MILES", "FROM", "THE", "VESSEL", "PROHIBITED."
				],
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
		self.assertEqual(result["analysis"]["nums"][2]["092240"],1)
		self.assertEqual(result["analysis"]["nums"][2]["19"],1)

		self.assertEqual(result["analysis"]["nums"][4]["193/19"],1)

		self.assertEqual(result["analysis"]["nums"][5]["100-16"],1)

		self.assertEqual(result["analysis"]["nums"][6]["0700"],1)
		self.assertEqual(result["analysis"]["nums"][6]["1900"],1)
		self.assertEqual(result["analysis"]["nums"][6]["0500"],1)
		self.assertEqual(result["analysis"]["nums"][6]["1700"],1)

		self.assertEqual(result["analysis"]["nums"][8]["44"],1)
		self.assertEqual(result["analysis"]["nums"][8]["543"],1)
		self.assertEqual(result["analysis"]["nums"][8]["013"],1)
		self.assertEqual(result["analysis"]["nums"][8]["487"],1)

		self.assertEqual(result["analysis"]["nums"][9]["44"],1)
		self.assertEqual(result["analysis"]["nums"][9]["537"],1)
		self.assertEqual(result["analysis"]["nums"][9]["013"],1)
		self.assertEqual(result["analysis"]["nums"][9]["477"],1)

		self.assertEqual(result["analysis"]["nums"][10]["44"],1)
		self.assertEqual(result["analysis"]["nums"][10]["530"],1)
		self.assertEqual(result["analysis"]["nums"][10]["013"],1)
		self.assertEqual(result["analysis"]["nums"][10]["455"],1)

		self.assertEqual(result["analysis"]["nums"][11]["44"],1)
		self.assertEqual(result["analysis"]["nums"][11]["531"],1)
		self.assertEqual(result["analysis"]["nums"][11]["013"],1)
		self.assertEqual(result["analysis"]["nums"][11]["436"],1)

		self.assertEqual(result["analysis"]["nums"][12]["44"],1)
		self.assertEqual(result["analysis"]["nums"][12]["508"],1)
		self.assertEqual(result["analysis"]["nums"][12]["013"],1)
		self.assertEqual(result["analysis"]["nums"][12]["386"],1)

		self.assertEqual(result["analysis"]["nums"][13]["16"],1)

		self.assertEqual(result["analysis"]["nums"][14]["05"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][2]["JUN"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["SPLIT"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["RADIO"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["NAV"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["WNG"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["NR"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["N-ERN"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["ADRIATIC"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["-"],2)
		self.assertEqual(result["analysis"]["unknown"][5]["BRIJUNI"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["CHRT"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["NOTICEFROM"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["LT"],2)
		self.assertEqual(result["analysis"]["unknown"][6]["TO"],2)
		self.assertEqual(result["analysis"]["unknown"][6]["M/V"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["REFUL"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["MAINTENANCE"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["WORKS"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["BETWEEN"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["POSITIONS"],1)

		self.assertEqual(result["analysis"]["unknown"][8]["A)"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][9]["B)"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][10]["C)"],1)
		self.assertEqual(result["analysis"]["unknown"][10]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][10]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][10]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][11]["D)"],1)
		self.assertEqual(result["analysis"]["unknown"][11]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][11]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][11]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][12]["E)"],1)
		self.assertEqual(result["analysis"]["unknown"][12]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][12]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][12]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][13]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["CH"],1)

		self.assertEqual(result["analysis"]["unknown"][14]["NAVIGATION"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["FISHING"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["RADIUS"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["MILES"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["THE"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["VESSEL"],1)
		self.assertEqual(result["analysis"]["unknown"][14]["PROHIBITED"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][2]["UTC"],1)
		self.assertEqual(result["analysis"]["known"][6]["UTC"],2)
		self.assertEqual(result["analysis"]["known"][6]["UNTIL"],1)
		self.assertEqual(result["analysis"]["known"][6]["FURTHER"],1)
		self.assertEqual(result["analysis"]["known"][6]["FROM"],1)
		self.assertEqual(result["analysis"]["known"][7]["GAS"],1)
		self.assertEqual(result["analysis"]["known"][7]["CONDUCTING"],1)
		self.assertEqual(result["analysis"]["known"][7]["UNDERWATER"],1)
		self.assertEqual(result["analysis"]["known"][13]["CONTACT"],1)
		self.assertEqual(result["analysis"]["known"][14]["FROM"],1)

		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertEqual(result["analysis"]["punct"][7][")"],1)
		self.assertEqual(result["analysis"]["punct"][8][")"],1)
		self.assertEqual(result["analysis"]["punct"][9][")"],1)
		self.assertEqual(result["analysis"]["punct"][10][")"],1)
		self.assertEqual(result["analysis"]["punct"][11][")"],1)

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "Q","A","42" ))

		self.assertIn("DTG", result["analysis"])
		self.assertIsInstance(result["analysis"]["DTG"], float)
		self.assertEqual(

			TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
			"06/09/2019 2240"
		)




	def test_analysis_SE94_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("UNTIL"),
				("FURTHER"),
				("FROM"),
				("UTC"),
				("CONDUCTING"),
				("UNDERWATER"),
				("GAS")
			""")

		analyzer = NavtexAnalyzer("S")
		result = analyzer(self.SE94)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 61) # 1 + 4 + 8 + 16 + 32
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
			[
				[ "ZCZC", "SE94" ],
				[ "171900", "NAVTEX-HAMBURG", "(NCC)" ],
				[ "WEATHERFORECAST", "FOR", "GERMAN", "BIGHT", "UNTIL", "18.11.2019", "12", "UTC:" ],
				[ "NORTHEAST", "TO", "NORTH", "4", "INCREASING", "ABOUT", "6", "EASTERN", "PART", "LATER" ],
				[
					"DECREASING", "A", "LITTLE", "AND", "SHIFTING",
					"EAST", "EASTERN", "PART", "AT", "TIMES", "MISTY"
				],
				[ "SEA", "INCREASING", "25", "METRE." ],
				[ "OUTLOOK", "UNTIL", "19.11.2019", "00", "UTC:" ],
				[ "WESTERN", "PART", "NORTH", "6", "TO", "7", "OTHERWISE", "EAST", "TO", "SOUTHEAST", "5." ],
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
		self.assertEqual(result["analysis"]["nums"][2]["171900"],1)

		self.assertEqual(result["analysis"]["nums"][3]["18.11.2019"],1)
		self.assertEqual(result["analysis"]["nums"][3]["12"],1)

		self.assertEqual(result["analysis"]["nums"][4]["4"],1)
		self.assertEqual(result["analysis"]["nums"][4]["6"],1)

		self.assertEqual(result["analysis"]["nums"][6]["25"],1)

		self.assertEqual(result["analysis"]["nums"][7]["19.11.2019"],1)
		self.assertEqual(result["analysis"]["nums"][7]["00"],1)

		self.assertEqual(result["analysis"]["nums"][8]["6"],1)
		self.assertEqual(result["analysis"]["nums"][8]["7"],1)
		self.assertEqual(result["analysis"]["nums"][8]["5"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)

		self.assertEqual(result["analysis"]["unknown"][2]["NAVTEX-HAMBURG"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["NCC"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["WEATHERFORECAST"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["FOR"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["GERMAN"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["BIGHT"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["NORTHEAST"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["TO"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["NORTH"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["INCREASING"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["ABOUT"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["EASTERN"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["PART"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["LATER"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["DECREASING"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["A"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["LITTLE"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["SHIFTING"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["EAST"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["EASTERN"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["PART"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["AT"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["TIMES"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["MISTY"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["SEA"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["INCREASING"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["METRE"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["OUTLOOK"],1)

		self.assertEqual(result["analysis"]["unknown"][8]["WESTERN"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["PART"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["NORTH"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["TO"],2)
		self.assertEqual(result["analysis"]["unknown"][8]["OTHERWISE"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["EAST"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["SOUTHEAST"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][3]["UNTIL"],1)
		self.assertEqual(result["analysis"]["known"][3]["UTC"],1)
		self.assertEqual(result["analysis"]["known"][7]["UNTIL"],1)
		self.assertEqual(result["analysis"]["known"][7]["UTC"],1)

		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertFalse(len(result["analysis"]["punct"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "S","E","94" ))

		self.assertNotIn("DTG", result["analysis"])




	def test_analysis_NA22_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

		analyzer = NavtexAnalyzer("M")
		result = analyzer(self.NA22)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 107) # 1 + 2 + 8 + 32 + 64
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
			[
				[ "ZCZC", "NA22" ],
				[ "110905", "UTC", "MAR", "19" ],
				[ "NORWEGIAN", "NAV.", "WARNING", "184/2019" ],
				[ "CHART", "N36" ],
				[ "AREA", "GRIP" ],
				[ "HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE" ],
				[ "NNNN" ]
			]
		)
		self.assertIsInstance(result.get("analysis"), dict)

		self.assertIn("coords", result["analysis"])
		self.assertIsInstance(result["analysis"]["coords"], dict)
		self.assertEqual(result["analysis"]["coords"][6]["63-12.0N"],1)
		self.assertEqual(result["analysis"]["coords"][6]["007-43.8E"],1)

		self.assertIn("alnums", result["analysis"])
		self.assertIsInstance(result["analysis"]["alnums"], dict)
		self.assertEqual(result["analysis"]["alnums"][4]["N36"],1)

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"][2]["110905"],1)
		self.assertEqual(result["analysis"]["nums"][2]["19"],1)
		self.assertEqual(result["analysis"]["nums"][3]["184/2019"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["MAR"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["NORWEGIAN"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["NAV"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["WARNING"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["CHART"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["AREA"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["GRIP"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["HILBAAAN"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["RACON"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["IS"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["INOPERATIVE"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))

		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertFalse(len(result["analysis"]["punct"]))

		self.assertNotIn("header", result["analysis"])

		self.assertIn("DTG", result["analysis"])
		self.assertIsInstance(result["analysis"]["DTG"], float)
		self.assertEqual(

			TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
			"03/11/2019 0905"
		)




	def test_analysis_IA76_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('ICE')")

		analyzer = NavtexAnalyzer("I")
		result = analyzer(self.IA76)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 117) # 1 + 4 + 16 + 32 + 64
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
			[
				[ "ZCZC", "IA76" ],
				[ "210800", "UTC", "JAN" ],
				[ "BALTIC", "ICE", "INFORMATION" ],
				[
					"VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO",
					"TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "'ICEINFO'"
				],
				[ "ON", "VHF", "OR" ],
				[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
				[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH78." ],
				[
					"ARRIVAL", "REPORT", "ON", "VHF", "CH16",
					"WHEN", "THE", "SHIP", "IS", "WELL", "MOORED."
				],
				[
					"DEPARTURE", "REPORT", "ON", "VHF", "CH16",
					"LATEST", "6", "HOURS", "BEFORE", "DEPARTURE."
				],
				[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "'BALTICE.ORG'" ],
			]
		)

		self.assertIsInstance(result.get("analysis"), dict)

		self.assertIn("coords", result["analysis"])
		self.assertIsInstance(result["analysis"]["coords"], dict)
		self.assertFalse(len(result["analysis"]["coords"]))

		self.assertIn("alnums", result["analysis"])
		self.assertIsInstance(result["analysis"]["alnums"], dict)
		self.assertEqual(result["analysis"]["alnums"][7]["N60"],1)
		self.assertEqual(result["analysis"]["alnums"][7]["CH78"],1)
		self.assertEqual(result["analysis"]["alnums"][8]["CH16"],1)
		self.assertEqual(result["analysis"]["alnums"][9]["CH16"],1)

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"][6]["0"],1)
		self.assertEqual(result["analysis"]["nums"][6]["10"],1)
		self.assertEqual(result["analysis"]["nums"][6]["492"],1)
		self.assertEqual(result["analysis"]["nums"][6]["76"],1)
		self.assertEqual(result["analysis"]["nums"][6]["00"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["JAN"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["BALTIC"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["INFORMATION"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["VESSELS"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["BOUND"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["FOR"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["PORTS"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["SUBJECT"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["TO"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["TRAFFIC"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["RESTRICTIONS"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["SHALL"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["CALL"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["ICEINFO"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["OR"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["PHONE"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["+46"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["AS"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["FOLLOWS"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["WHEN"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["PASSING"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["LAT"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["VHF"],1)

		self.assertEqual(result["analysis"]["unknown"][8]["ARRIVAL"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["REPORT"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["WHEN"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["THE"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["SHIP"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["IS"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["WELL"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["MOORED"],1)

		self.assertEqual(result["analysis"]["unknown"][9]["DEPARTURE"],2)
		self.assertEqual(result["analysis"]["unknown"][9]["REPORT"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["LATEST"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["HOURS"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["BEFORE"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][3]["ICE"],1)

		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertFalse(len(result["analysis"]["punct"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "I","A","76" ))

		self.assertIn("DTG", result["analysis"])
		self.assertIsInstance(result["analysis"]["DTG"], float)
		self.assertEqual(

			TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
			f"01/21/{TimeTurner().format('%Y')} 0800"
		)




	def test_analysis_VA28_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('ICE')")

		analyzer = NavtexAnalyzer("V")
		result = analyzer(self.VA28)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 101) # 1 + 4 + 32 + 64
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
			[
				[ "ZCZC", "VA28" ],
				[ "050550", "UTC", "AUG" ],
				[ "WZ", "724" ],
				[
					"GMDSS.", "HUMBER", "COASTGUARD.", "1.", "MF", "R/T",
					"AND", "DSC", "SERVICES", "FROM", "LANGHAM", "SITE"
				],
				[
					"52-56.5N", "000-57.2E.", "OFF", "AIR.", "2.",
					"CANCEL", "WZ", "597", "(GA73)", "(VA10)."
				],
				[ "NNN" ],
			]
		)

		self.assertIsInstance(result.get("analysis"), dict)

		self.assertIn("coords", result["analysis"])
		self.assertIsInstance(result["analysis"]["coords"], dict)
		self.assertEqual(result["analysis"]["coords"][5]["52-56.5N"],1)
		self.assertEqual(result["analysis"]["coords"][5]["000-57.2E"],1)

		self.assertIn("alnums", result["analysis"])
		self.assertFalse(len(result["analysis"]["alnums"]))

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"][2]["050550"],1)
		self.assertEqual(result["analysis"]["nums"][3]["724"],1)
		self.assertEqual(result["analysis"]["nums"][4]["1"],1)
		self.assertEqual(result["analysis"]["nums"][5]["2"],1)
		self.assertEqual(result["analysis"]["nums"][5]["597"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["AUG"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["WZ"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["GMDSS"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["HUMBER"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["COASTGUARD"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["MF"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["R/T"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["DSC"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["SERVICES"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["FROM"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["LANGHAM"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["SITE"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["OFF"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["AIR"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["CANCEL"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["WZ"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["GA73"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["VA10"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))

		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertFalse(len(result["analysis"]["punct"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "V","A","28" ))

		self.assertIn("DTG", result["analysis"])
		self.assertIsInstance(result["analysis"]["DTG"], float)
		self.assertEqual(

			TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
			f"08/05/{TimeTurner().format('%Y')} 0550"
		)




	def test_analysis_MZ56_file(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('HAND')")

		analyzer = NavtexAnalyzer("V")
		result = analyzer(self.MZ56)
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 4)
		self.assertEqual(result.get("state"), 121) # 1 + 8 + 16 + 32 + 64
		self.assertIsInstance(result.get("raw"), list)
		self.assertIsInstance(result.get("air"), list)
		self.assertEqual(

			result.get("air"),
			[
				[ "ZCZC", "MZ56" ],
				[ "011713", "UTC", "AUG", "19" ],
				[ "NAVAREA", "1", "-", "NO", "MESSAGES", "ON", "HAND" ],
				[ "NNNN" ],
			]
		)

		self.assertIsInstance(result.get("analysis"), dict)

		self.assertIn("coords", result["analysis"])
		self.assertIsInstance(result["analysis"]["coords"], dict)
		self.assertFalse(len(result["analysis"]["coords"]))

		self.assertIn("alnums", result["analysis"])
		self.assertFalse(len(result["analysis"]["alnums"]))

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"][2]["011713"],1)
		self.assertEqual(result["analysis"]["nums"][2]["19"],1)
		self.assertEqual(result["analysis"]["nums"][3]["1"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["AUG"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["NAVAREA"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["NO"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["MESSAGES"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["ON"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][3]["HAND"],1)

		self.assertIn("punct", result["analysis"])
		self.assertIsInstance(result["analysis"]["punct"], dict)
		self.assertFalse(len(result["analysis"]["punct"]))

		self.assertNotIn("header", result["analysis"])

		self.assertIn("DTG", result["analysis"])
		self.assertIsInstance(result["analysis"]["DTG"], float)
		self.assertEqual(

			TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
			"08/01/2019 1713"
		)








	def test_analysis_WZ29_string(self):

		analyzer = NavtexAnalyzer("W")
		with open(self.corrupted_file) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 2)
			self.assertEqual(result.get("state"), 0)
			self.assertIsInstance(result.get("message"), str)
			self.assertIn("*", result.get("message"))


	def test_analysis_JA94_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

		analyzer = NavtexAnalyzer("J")

		with open(self.JA94) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 109) # 1 + 4 + 8 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
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
			self.assertEqual(result["analysis"]["nums"][2]["151930"],1)
			self.assertEqual(result["analysis"]["nums"][3]["079/19"],1)
			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["FEB"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["CANCEL"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["GERMAN"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NAV"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["WARN"],1)
			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertFalse(len(result["analysis"]["known"]))
			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))
			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "J","A","94" ))
			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				f"02/15/{TimeTurner().format('%Y')} 1930"
			)




	def test_analysis_OL66_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("CANCEL")
			""")

		analyzer = NavtexAnalyzer("O")

		with open(self.OL66) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 63) # 1 + 2 + 4 + 8 + 16 + 32
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "OL66" ],
					[ "OL66" ],
					[ "FOSNNI", "SUBFACTS", "AND", "GUNFACTS", "WARNING", "(ALL", "TIMES", "UTC):" ],
					[ "1.", "DIVED", "SUBMARINE", "OPERATIONS", "IN", "PROGRESS:" ],
					[
						"INNER", "SOUND", "-", "INSIDE", "OF", "SKYE", "SOUTH", "OF",
						"RUBHA", "REIDH", "NORTH", "OF", "MALLAIG.", "BETWEEN"
					],
					[ "120600", "AND", "130700", "SEP." ],
					[ "2.", "LIVE", "GUNNERY", "FIRINGS", "IN", "PROGRESS:", "NIL." ],
					[
						"FULL", "DETAILS", "IN", "HM", "COASTGUARD", "RESCUE",
						"CENTRES", "VHF", "AND", "MF", "BROADCASTS", "OR", "CONTACT"
					],
					[ "CTF", "311", "PHONE", "(44)(0)1923", "956366." ],
					[ "CANCEL", "OL65" ],
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
			self.assertEqual(result["analysis"]["nums"][4]["1"],1)
			self.assertEqual(result["analysis"]["nums"][6]["120600"],1)
			self.assertEqual(result["analysis"]["nums"][6]["130700"],1)
			self.assertEqual(result["analysis"]["nums"][7]["2"],1)
			self.assertEqual(result["analysis"]["nums"][9]["311"],1)
			self.assertEqual(result["analysis"]["nums"][9]["44"],1)
			self.assertEqual(result["analysis"]["nums"][9]["0"],1)
			self.assertEqual(result["analysis"]["nums"][9]["1923"],1)
			self.assertEqual(result["analysis"]["nums"][9]["956366"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["OL66"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["FOSNNI"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["SUBFACTS"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["GUNFACTS"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["WARNING"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["ALL"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["TIMES"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["UTC"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["DIVED"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SUBMARINE"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["OPERATIONS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["PROGRESS"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["INNER"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["INSIDE"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["OF"],3)
			self.assertEqual(result["analysis"]["unknown"][5]["SKYE"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["RUBHA"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["REIDH"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["NORTH"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["MALLAIG"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["BETWEEN"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["SEP"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["LIVE"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["GUNNERY"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["FIRINGS"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["PROGRESS"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["NIL"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["FULL"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["DETAILS"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["HM"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["COASTGUARD"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["RESCUE"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["CENTRES"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["MF"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["BROADCASTS"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["OR"],1)

			self.assertEqual(result["analysis"]["unknown"][9]["PHONE"],1)

			self.assertEqual(result["analysis"]["unknown"][10]["OL65"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][5]["SOUND"],1)
			self.assertEqual(result["analysis"]["known"][5]["SOUTH"],1)
			self.assertEqual(result["analysis"]["known"][8]["CONTACT"],1)
			self.assertEqual(result["analysis"]["known"][9]["CTF"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "O","L","66" ))

			self.assertNotIn("DTG", result["analysis"])




	def test_analysis_QA42_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("UNTIL"),
				("FURTHER"),
				("FROM"),
				("UTC"),
				("CONDUCTING"),
				("UNDERWATER"),
				("GAS")
			""")

		analyzer = NavtexAnalyzer("Q")

		with open(self.QA42) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 125) # 1 + 4 + 8 + 16 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "QA42" ],
					[ "092240", "UTC", "JUN", "19" ],
					[ "SPLIT", "RADIO" ],
					[ "NAV", "WNG", "NR", "193/19" ],
					[ "N-ERN", "ADRIATIC", "-", "BRIJUNI", "-", "CHRT:100-16" ],
					[
						"UNTIL", "FURTHER", "NOTICEFROM", "0700", "LT", "TO", "1900",
						"LT", "(FROM", "0500", "UTC", "TO", "1700", "UTC)M/V"
					],
					[
						"REFUL", "CONDUCTING", "UNDERWATER", "GAS", "PIPELINE",
						"MAINTENANCE", "WORKS", "BETWEEN", "POSITIONS:"
					],
					[ "A)", "44", "543", "N", "-", "013", "487", "E" ],
					[ "B)", "44", "537", "N", "-", "013", "477", "E" ],
					[ "C)", "44", "530", "N", "-", "013", "455", "E" ],
					[ "D)", "44", "531", "N", "-", "013", "436", "E" ],
					[ "E)", "44", "508", "N", "-", "013", "386", "E" ],
					[ "CONTACT", "VHF", "CH", "16." ],
					[
						"NAVIGATION", "AND", "FISHING", "IN", "RADIUS", "05",
						"MILES", "FROM", "THE", "VESSEL", "PROHIBITED."
					],
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
			self.assertEqual(result["analysis"]["nums"][2]["092240"],1)
			self.assertEqual(result["analysis"]["nums"][2]["19"],1)

			self.assertEqual(result["analysis"]["nums"][4]["193/19"],1)

			self.assertEqual(result["analysis"]["nums"][5]["100-16"],1)

			self.assertEqual(result["analysis"]["nums"][6]["0700"],1)
			self.assertEqual(result["analysis"]["nums"][6]["1900"],1)
			self.assertEqual(result["analysis"]["nums"][6]["0500"],1)
			self.assertEqual(result["analysis"]["nums"][6]["1700"],1)

			self.assertEqual(result["analysis"]["nums"][8]["44"],1)
			self.assertEqual(result["analysis"]["nums"][8]["543"],1)
			self.assertEqual(result["analysis"]["nums"][8]["013"],1)
			self.assertEqual(result["analysis"]["nums"][8]["487"],1)

			self.assertEqual(result["analysis"]["nums"][9]["44"],1)
			self.assertEqual(result["analysis"]["nums"][9]["537"],1)
			self.assertEqual(result["analysis"]["nums"][9]["013"],1)
			self.assertEqual(result["analysis"]["nums"][9]["477"],1)

			self.assertEqual(result["analysis"]["nums"][10]["44"],1)
			self.assertEqual(result["analysis"]["nums"][10]["530"],1)
			self.assertEqual(result["analysis"]["nums"][10]["013"],1)
			self.assertEqual(result["analysis"]["nums"][10]["455"],1)

			self.assertEqual(result["analysis"]["nums"][11]["44"],1)
			self.assertEqual(result["analysis"]["nums"][11]["531"],1)
			self.assertEqual(result["analysis"]["nums"][11]["013"],1)
			self.assertEqual(result["analysis"]["nums"][11]["436"],1)

			self.assertEqual(result["analysis"]["nums"][12]["44"],1)
			self.assertEqual(result["analysis"]["nums"][12]["508"],1)
			self.assertEqual(result["analysis"]["nums"][12]["013"],1)
			self.assertEqual(result["analysis"]["nums"][12]["386"],1)

			self.assertEqual(result["analysis"]["nums"][13]["16"],1)

			self.assertEqual(result["analysis"]["nums"][14]["05"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["JUN"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["SPLIT"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["RADIO"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["NAV"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["WNG"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["NR"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["N-ERN"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["ADRIATIC"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["-"],2)
			self.assertEqual(result["analysis"]["unknown"][5]["BRIJUNI"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["CHRT"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["NOTICEFROM"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["LT"],2)
			self.assertEqual(result["analysis"]["unknown"][6]["TO"],2)
			self.assertEqual(result["analysis"]["unknown"][6]["M/V"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["REFUL"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["MAINTENANCE"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["WORKS"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["BETWEEN"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["POSITIONS"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["A)"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][9]["B)"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][10]["C)"],1)
			self.assertEqual(result["analysis"]["unknown"][10]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][10]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][10]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][11]["D)"],1)
			self.assertEqual(result["analysis"]["unknown"][11]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][11]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][11]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][12]["E)"],1)
			self.assertEqual(result["analysis"]["unknown"][12]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][12]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][12]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][13]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][13]["CH"],1)

			self.assertEqual(result["analysis"]["unknown"][14]["NAVIGATION"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["FISHING"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["RADIUS"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["MILES"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["THE"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["VESSEL"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["PROHIBITED"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["known"][6]["UTC"],2)
			self.assertEqual(result["analysis"]["known"][6]["UNTIL"],1)
			self.assertEqual(result["analysis"]["known"][6]["FURTHER"],1)
			self.assertEqual(result["analysis"]["known"][6]["FROM"],1)
			self.assertEqual(result["analysis"]["known"][7]["GAS"],1)
			self.assertEqual(result["analysis"]["known"][7]["CONDUCTING"],1)
			self.assertEqual(result["analysis"]["known"][7]["UNDERWATER"],1)
			self.assertEqual(result["analysis"]["known"][13]["CONTACT"],1)
			self.assertEqual(result["analysis"]["known"][14]["FROM"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertEqual(result["analysis"]["punct"][7][")"],1)
			self.assertEqual(result["analysis"]["punct"][8][")"],1)
			self.assertEqual(result["analysis"]["punct"][9][")"],1)
			self.assertEqual(result["analysis"]["punct"][10][")"],1)
			self.assertEqual(result["analysis"]["punct"][11][")"],1)

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "Q","A","42" ))

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				"06/09/2019 2240"
			)




	def test_analysis_SE94_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("UNTIL"),
				("FURTHER"),
				("FROM"),
				("UTC"),
				("CONDUCTING"),
				("UNDERWATER"),
				("GAS")
			""")

		analyzer = NavtexAnalyzer("S")

		with open(self.SE94) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 61) # 1 + 4 + 8 + 16 + 32
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "SE94" ],
					[ "171900", "NAVTEX-HAMBURG", "(NCC)" ],
					[ "WEATHERFORECAST", "FOR", "GERMAN", "BIGHT", "UNTIL", "18.11.2019", "12", "UTC:" ],
					[ "NORTHEAST", "TO", "NORTH", "4", "INCREASING", "ABOUT", "6", "EASTERN", "PART", "LATER" ],
					[
						"DECREASING", "A", "LITTLE", "AND", "SHIFTING",
						"EAST", "EASTERN", "PART", "AT", "TIMES", "MISTY"
					],
					[ "SEA", "INCREASING", "25", "METRE." ],
					[ "OUTLOOK", "UNTIL", "19.11.2019", "00", "UTC:" ],
					[ "WESTERN", "PART", "NORTH", "6", "TO", "7", "OTHERWISE", "EAST", "TO", "SOUTHEAST", "5." ],
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
			self.assertEqual(result["analysis"]["nums"][2]["171900"],1)

			self.assertEqual(result["analysis"]["nums"][3]["18.11.2019"],1)
			self.assertEqual(result["analysis"]["nums"][3]["12"],1)

			self.assertEqual(result["analysis"]["nums"][4]["4"],1)
			self.assertEqual(result["analysis"]["nums"][4]["6"],1)

			self.assertEqual(result["analysis"]["nums"][6]["25"],1)

			self.assertEqual(result["analysis"]["nums"][7]["19.11.2019"],1)
			self.assertEqual(result["analysis"]["nums"][7]["00"],1)

			self.assertEqual(result["analysis"]["nums"][8]["6"],1)
			self.assertEqual(result["analysis"]["nums"][8]["7"],1)
			self.assertEqual(result["analysis"]["nums"][8]["5"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)

			self.assertEqual(result["analysis"]["unknown"][2]["NAVTEX-HAMBURG"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["NCC"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["WEATHERFORECAST"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["FOR"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["GERMAN"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["BIGHT"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["NORTHEAST"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["TO"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["NORTH"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["INCREASING"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["ABOUT"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["EASTERN"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["PART"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["LATER"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["DECREASING"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["A"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["LITTLE"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["SHIFTING"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["EAST"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["EASTERN"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["PART"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AT"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["TIMES"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["MISTY"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["SEA"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["INCREASING"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["METRE"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["OUTLOOK"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["WESTERN"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["PART"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["NORTH"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["TO"],2)
			self.assertEqual(result["analysis"]["unknown"][8]["OTHERWISE"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["EAST"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["SOUTHEAST"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][3]["UNTIL"],1)
			self.assertEqual(result["analysis"]["known"][3]["UTC"],1)
			self.assertEqual(result["analysis"]["known"][7]["UNTIL"],1)
			self.assertEqual(result["analysis"]["known"][7]["UTC"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "S","E","94" ))

			self.assertNotIn("DTG", result["analysis"])




	def test_analysis_NA22_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

		analyzer = NavtexAnalyzer("M")

		with open(self.NA22) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 107) # 1 + 2 + 8 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "NA22" ],
					[ "110905", "UTC", "MAR", "19" ],
					[ "NORWEGIAN", "NAV.", "WARNING", "184/2019" ],
					[ "CHART", "N36" ],
					[ "AREA", "GRIP" ],
					[ "HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE" ],
					[ "NNNN" ]
				]
			)
			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertEqual(result["analysis"]["coords"][6]["63-12.0N"],1)
			self.assertEqual(result["analysis"]["coords"][6]["007-43.8E"],1)

			self.assertIn("alnums", result["analysis"])
			self.assertIsInstance(result["analysis"]["alnums"], dict)
			self.assertEqual(result["analysis"]["alnums"][4]["N36"],1)

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][2]["110905"],1)
			self.assertEqual(result["analysis"]["nums"][2]["19"],1)
			self.assertEqual(result["analysis"]["nums"][3]["184/2019"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["MAR"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NORWEGIAN"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NAV"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["WARNING"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["CHART"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AREA"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["GRIP"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["HILBAAAN"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["RACON"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["IS"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["INOPERATIVE"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertFalse(len(result["analysis"]["known"]))

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertNotIn("header", result["analysis"])

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				"03/11/2019 0905"
			)




	def test_analysis_IA76_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('ICE')")

		analyzer = NavtexAnalyzer("I")

		with open(self.IA76) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 117) # 1 + 4 + 16 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "IA76" ],
					[ "210800", "UTC", "JAN" ],
					[ "BALTIC", "ICE", "INFORMATION" ],
					[
						"VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO",
						"TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "'ICEINFO'"
					],
					[ "ON", "VHF", "OR" ],
					[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
					[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH78." ],
					[
						"ARRIVAL", "REPORT", "ON", "VHF", "CH16",
						"WHEN", "THE", "SHIP", "IS", "WELL", "MOORED."
					],
					[
						"DEPARTURE", "REPORT", "ON", "VHF", "CH16",
						"LATEST", "6", "HOURS", "BEFORE", "DEPARTURE."
					],
					[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "'BALTICE.ORG'" ],
				]
			)

			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertFalse(len(result["analysis"]["coords"]))

			self.assertIn("alnums", result["analysis"])
			self.assertIsInstance(result["analysis"]["alnums"], dict)
			self.assertEqual(result["analysis"]["alnums"][7]["N60"],1)
			self.assertEqual(result["analysis"]["alnums"][7]["CH78"],1)
			self.assertEqual(result["analysis"]["alnums"][8]["CH16"],1)
			self.assertEqual(result["analysis"]["alnums"][9]["CH16"],1)

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][6]["0"],1)
			self.assertEqual(result["analysis"]["nums"][6]["10"],1)
			self.assertEqual(result["analysis"]["nums"][6]["492"],1)
			self.assertEqual(result["analysis"]["nums"][6]["76"],1)
			self.assertEqual(result["analysis"]["nums"][6]["00"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["JAN"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["BALTIC"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["INFORMATION"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["VESSELS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["BOUND"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["FOR"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["PORTS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SUBJECT"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["TO"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["TRAFFIC"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["RESTRICTIONS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SHALL"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["CALL"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["ICEINFO"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["OR"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["PHONE"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["+46"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["AS"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["FOLLOWS"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["WHEN"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["PASSING"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["LAT"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["VHF"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["ARRIVAL"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["REPORT"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["WHEN"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["THE"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["SHIP"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["IS"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["WELL"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["MOORED"],1)

			self.assertEqual(result["analysis"]["unknown"][9]["DEPARTURE"],2)
			self.assertEqual(result["analysis"]["unknown"][9]["REPORT"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["LATEST"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["HOURS"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["BEFORE"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][3]["ICE"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "I","A","76" ))

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				f"01/21/{TimeTurner().format('%Y')} 0800"
			)




	def test_analysis_VA28_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('ICE')")

		analyzer = NavtexAnalyzer("V")

		with open(self.VA28) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 101) # 1 + 4 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "VA28" ],
					[ "050550", "UTC", "AUG" ],
					[ "WZ", "724" ],
					[
						"GMDSS.", "HUMBER", "COASTGUARD.", "1.", "MF", "R/T",
						"AND", "DSC", "SERVICES", "FROM", "LANGHAM", "SITE"
					],
					[
						"52-56.5N", "000-57.2E.", "OFF", "AIR.", "2.",
						"CANCEL", "WZ", "597", "(GA73)", "(VA10)."
					],
					[ "NNN" ],
				]
			)

			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertEqual(result["analysis"]["coords"][5]["52-56.5N"],1)
			self.assertEqual(result["analysis"]["coords"][5]["000-57.2E"],1)

			self.assertIn("alnums", result["analysis"])
			self.assertFalse(len(result["analysis"]["alnums"]))

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][2]["050550"],1)
			self.assertEqual(result["analysis"]["nums"][3]["724"],1)
			self.assertEqual(result["analysis"]["nums"][4]["1"],1)
			self.assertEqual(result["analysis"]["nums"][5]["2"],1)
			self.assertEqual(result["analysis"]["nums"][5]["597"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["AUG"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["WZ"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["GMDSS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["HUMBER"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["COASTGUARD"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["MF"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["R/T"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["DSC"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SERVICES"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["FROM"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["LANGHAM"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SITE"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["OFF"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AIR"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["CANCEL"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["WZ"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["GA73"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["VA10"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertFalse(len(result["analysis"]["known"]))

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "V","A","28" ))

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				f"08/05/{TimeTurner().format('%Y')} 0550"
			)




	def test_analysis_MZ56_string(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('HAND')")

		analyzer = NavtexAnalyzer("V")

		with open(self.MZ56) as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 121) # 1 + 8 + 16 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "MZ56" ],
					[ "011713", "UTC", "AUG", "19" ],
					[ "NAVAREA", "1", "-", "NO", "MESSAGES", "ON", "HAND" ],
					[ "NNNN" ],
				]
			)

			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertFalse(len(result["analysis"]["coords"]))

			self.assertIn("alnums", result["analysis"])
			self.assertFalse(len(result["analysis"]["alnums"]))

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][2]["011713"],1)
			self.assertEqual(result["analysis"]["nums"][2]["19"],1)
			self.assertEqual(result["analysis"]["nums"][3]["1"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["AUG"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["NAVAREA"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NO"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["MESSAGES"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["ON"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][3]["HAND"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertNotIn("header", result["analysis"])

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				"08/01/2019 1713"
			)








	def test_analysis_WZ29_bytes(self):

		analyzer = NavtexAnalyzer("W")
		with open(self.corrupted_file, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 2)
			self.assertEqual(result.get("state"), 0)
			self.assertIsInstance(result.get("message"), str)
			self.assertIn("*", result.get("message"))


	def test_analysis_JA94_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

		analyzer = NavtexAnalyzer("J")

		with open(self.JA94, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 109) # 1 + 4 + 8 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
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
			self.assertEqual(result["analysis"]["nums"][2]["151930"],1)
			self.assertEqual(result["analysis"]["nums"][3]["079/19"],1)
			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["FEB"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["CANCEL"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["GERMAN"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NAV"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["WARN"],1)
			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertFalse(len(result["analysis"]["known"]))
			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))
			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "J","A","94" ))
			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				f"02/15/{TimeTurner().format('%Y')} 1930"
			)




	def test_analysis_OL66_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("CANCEL")
			""")

		analyzer = NavtexAnalyzer("O")

		with open(self.OL66, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 63) # 1 + 2 + 4 + 8 + 16 + 32
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "OL66" ],
					[ "OL66" ],
					[ "FOSNNI", "SUBFACTS", "AND", "GUNFACTS", "WARNING", "(ALL", "TIMES", "UTC):" ],
					[ "1.", "DIVED", "SUBMARINE", "OPERATIONS", "IN", "PROGRESS:" ],
					[
						"INNER", "SOUND", "-", "INSIDE", "OF", "SKYE", "SOUTH", "OF",
						"RUBHA", "REIDH", "NORTH", "OF", "MALLAIG.", "BETWEEN"
					],
					[ "120600", "AND", "130700", "SEP." ],
					[ "2.", "LIVE", "GUNNERY", "FIRINGS", "IN", "PROGRESS:", "NIL." ],
					[
						"FULL", "DETAILS", "IN", "HM", "COASTGUARD", "RESCUE",
						"CENTRES", "VHF", "AND", "MF", "BROADCASTS", "OR", "CONTACT"
					],
					[ "CTF", "311", "PHONE", "(44)(0)1923", "956366." ],
					[ "CANCEL", "OL65" ],
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
			self.assertEqual(result["analysis"]["nums"][4]["1"],1)
			self.assertEqual(result["analysis"]["nums"][6]["120600"],1)
			self.assertEqual(result["analysis"]["nums"][6]["130700"],1)
			self.assertEqual(result["analysis"]["nums"][7]["2"],1)
			self.assertEqual(result["analysis"]["nums"][9]["311"],1)
			self.assertEqual(result["analysis"]["nums"][9]["44"],1)
			self.assertEqual(result["analysis"]["nums"][9]["0"],1)
			self.assertEqual(result["analysis"]["nums"][9]["1923"],1)
			self.assertEqual(result["analysis"]["nums"][9]["956366"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["OL66"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["FOSNNI"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["SUBFACTS"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["GUNFACTS"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["WARNING"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["ALL"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["TIMES"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["UTC"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["DIVED"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SUBMARINE"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["OPERATIONS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["PROGRESS"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["INNER"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["INSIDE"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["OF"],3)
			self.assertEqual(result["analysis"]["unknown"][5]["SKYE"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["RUBHA"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["REIDH"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["NORTH"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["MALLAIG"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["BETWEEN"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["SEP"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["LIVE"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["GUNNERY"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["FIRINGS"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["PROGRESS"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["NIL"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["FULL"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["DETAILS"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["HM"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["COASTGUARD"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["RESCUE"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["CENTRES"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["MF"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["BROADCASTS"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["OR"],1)

			self.assertEqual(result["analysis"]["unknown"][9]["PHONE"],1)

			self.assertEqual(result["analysis"]["unknown"][10]["OL65"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][5]["SOUND"],1)
			self.assertEqual(result["analysis"]["known"][5]["SOUTH"],1)
			self.assertEqual(result["analysis"]["known"][8]["CONTACT"],1)
			self.assertEqual(result["analysis"]["known"][9]["CTF"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "O","L","66" ))

			self.assertNotIn("DTG", result["analysis"])




	def test_analysis_QA42_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("UNTIL"),
				("FURTHER"),
				("FROM"),
				("UTC"),
				("CONDUCTING"),
				("UNDERWATER"),
				("GAS")
			""")

		analyzer = NavtexAnalyzer("Q")

		with open(self.QA42, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 125) # 1 + 4 + 8 + 16 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "QA42" ],
					[ "092240", "UTC", "JUN", "19" ],
					[ "SPLIT", "RADIO" ],
					[ "NAV", "WNG", "NR", "193/19" ],
					[ "N-ERN", "ADRIATIC", "-", "BRIJUNI", "-", "CHRT:100-16" ],
					[
						"UNTIL", "FURTHER", "NOTICEFROM", "0700", "LT", "TO", "1900",
						"LT", "(FROM", "0500", "UTC", "TO", "1700", "UTC)M/V"
					],
					[
						"REFUL", "CONDUCTING", "UNDERWATER", "GAS", "PIPELINE",
						"MAINTENANCE", "WORKS", "BETWEEN", "POSITIONS:"
					],
					[ "A)", "44", "543", "N", "-", "013", "487", "E" ],
					[ "B)", "44", "537", "N", "-", "013", "477", "E" ],
					[ "C)", "44", "530", "N", "-", "013", "455", "E" ],
					[ "D)", "44", "531", "N", "-", "013", "436", "E" ],
					[ "E)", "44", "508", "N", "-", "013", "386", "E" ],
					[ "CONTACT", "VHF", "CH", "16." ],
					[
						"NAVIGATION", "AND", "FISHING", "IN", "RADIUS", "05",
						"MILES", "FROM", "THE", "VESSEL", "PROHIBITED."
					],
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
			self.assertEqual(result["analysis"]["nums"][2]["092240"],1)
			self.assertEqual(result["analysis"]["nums"][2]["19"],1)

			self.assertEqual(result["analysis"]["nums"][4]["193/19"],1)

			self.assertEqual(result["analysis"]["nums"][5]["100-16"],1)

			self.assertEqual(result["analysis"]["nums"][6]["0700"],1)
			self.assertEqual(result["analysis"]["nums"][6]["1900"],1)
			self.assertEqual(result["analysis"]["nums"][6]["0500"],1)
			self.assertEqual(result["analysis"]["nums"][6]["1700"],1)

			self.assertEqual(result["analysis"]["nums"][8]["44"],1)
			self.assertEqual(result["analysis"]["nums"][8]["543"],1)
			self.assertEqual(result["analysis"]["nums"][8]["013"],1)
			self.assertEqual(result["analysis"]["nums"][8]["487"],1)

			self.assertEqual(result["analysis"]["nums"][9]["44"],1)
			self.assertEqual(result["analysis"]["nums"][9]["537"],1)
			self.assertEqual(result["analysis"]["nums"][9]["013"],1)
			self.assertEqual(result["analysis"]["nums"][9]["477"],1)

			self.assertEqual(result["analysis"]["nums"][10]["44"],1)
			self.assertEqual(result["analysis"]["nums"][10]["530"],1)
			self.assertEqual(result["analysis"]["nums"][10]["013"],1)
			self.assertEqual(result["analysis"]["nums"][10]["455"],1)

			self.assertEqual(result["analysis"]["nums"][11]["44"],1)
			self.assertEqual(result["analysis"]["nums"][11]["531"],1)
			self.assertEqual(result["analysis"]["nums"][11]["013"],1)
			self.assertEqual(result["analysis"]["nums"][11]["436"],1)

			self.assertEqual(result["analysis"]["nums"][12]["44"],1)
			self.assertEqual(result["analysis"]["nums"][12]["508"],1)
			self.assertEqual(result["analysis"]["nums"][12]["013"],1)
			self.assertEqual(result["analysis"]["nums"][12]["386"],1)

			self.assertEqual(result["analysis"]["nums"][13]["16"],1)

			self.assertEqual(result["analysis"]["nums"][14]["05"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["JUN"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["SPLIT"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["RADIO"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["NAV"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["WNG"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["NR"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["N-ERN"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["ADRIATIC"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["-"],2)
			self.assertEqual(result["analysis"]["unknown"][5]["BRIJUNI"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["CHRT"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["NOTICEFROM"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["LT"],2)
			self.assertEqual(result["analysis"]["unknown"][6]["TO"],2)
			self.assertEqual(result["analysis"]["unknown"][6]["M/V"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["REFUL"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["MAINTENANCE"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["WORKS"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["BETWEEN"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["POSITIONS"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["A)"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][9]["B)"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][10]["C)"],1)
			self.assertEqual(result["analysis"]["unknown"][10]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][10]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][10]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][11]["D)"],1)
			self.assertEqual(result["analysis"]["unknown"][11]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][11]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][11]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][12]["E)"],1)
			self.assertEqual(result["analysis"]["unknown"][12]["N"],1)
			self.assertEqual(result["analysis"]["unknown"][12]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][12]["E"],1)

			self.assertEqual(result["analysis"]["unknown"][13]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][13]["CH"],1)

			self.assertEqual(result["analysis"]["unknown"][14]["NAVIGATION"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["FISHING"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["IN"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["RADIUS"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["MILES"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["THE"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["VESSEL"],1)
			self.assertEqual(result["analysis"]["unknown"][14]["PROHIBITED"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["known"][6]["UTC"],2)
			self.assertEqual(result["analysis"]["known"][6]["UNTIL"],1)
			self.assertEqual(result["analysis"]["known"][6]["FURTHER"],1)
			self.assertEqual(result["analysis"]["known"][6]["FROM"],1)
			self.assertEqual(result["analysis"]["known"][7]["GAS"],1)
			self.assertEqual(result["analysis"]["known"][7]["CONDUCTING"],1)
			self.assertEqual(result["analysis"]["known"][7]["UNDERWATER"],1)
			self.assertEqual(result["analysis"]["known"][13]["CONTACT"],1)
			self.assertEqual(result["analysis"]["known"][14]["FROM"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertEqual(result["analysis"]["punct"][7][")"],1)
			self.assertEqual(result["analysis"]["punct"][8][")"],1)
			self.assertEqual(result["analysis"]["punct"][9][")"],1)
			self.assertEqual(result["analysis"]["punct"][10][")"],1)
			self.assertEqual(result["analysis"]["punct"][11][")"],1)

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "Q","A","42" ))

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				"06/09/2019 2240"
			)




	def test_analysis_SE94_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("""INSERT INTO navbow_test VALUES
				("CTF"),
				("SOUND"),
				("SOUTH"),
				("CONTACT"),
				("UNTIL"),
				("FURTHER"),
				("FROM"),
				("UTC"),
				("CONDUCTING"),
				("UNDERWATER"),
				("GAS")
			""")

		analyzer = NavtexAnalyzer("S")

		with open(self.SE94, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 61) # 1 + 4 + 8 + 16 + 32
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "SE94" ],
					[ "171900", "NAVTEX-HAMBURG", "(NCC)" ],
					[ "WEATHERFORECAST", "FOR", "GERMAN", "BIGHT", "UNTIL", "18.11.2019", "12", "UTC:" ],
					[ "NORTHEAST", "TO", "NORTH", "4", "INCREASING", "ABOUT", "6", "EASTERN", "PART", "LATER" ],
					[
						"DECREASING", "A", "LITTLE", "AND", "SHIFTING",
						"EAST", "EASTERN", "PART", "AT", "TIMES", "MISTY"
					],
					[ "SEA", "INCREASING", "25", "METRE." ],
					[ "OUTLOOK", "UNTIL", "19.11.2019", "00", "UTC:" ],
					[ "WESTERN", "PART", "NORTH", "6", "TO", "7", "OTHERWISE", "EAST", "TO", "SOUTHEAST", "5." ],
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
			self.assertEqual(result["analysis"]["nums"][2]["171900"],1)

			self.assertEqual(result["analysis"]["nums"][3]["18.11.2019"],1)
			self.assertEqual(result["analysis"]["nums"][3]["12"],1)

			self.assertEqual(result["analysis"]["nums"][4]["4"],1)
			self.assertEqual(result["analysis"]["nums"][4]["6"],1)

			self.assertEqual(result["analysis"]["nums"][6]["25"],1)

			self.assertEqual(result["analysis"]["nums"][7]["19.11.2019"],1)
			self.assertEqual(result["analysis"]["nums"][7]["00"],1)

			self.assertEqual(result["analysis"]["nums"][8]["6"],1)
			self.assertEqual(result["analysis"]["nums"][8]["7"],1)
			self.assertEqual(result["analysis"]["nums"][8]["5"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)

			self.assertEqual(result["analysis"]["unknown"][2]["NAVTEX-HAMBURG"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["NCC"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["WEATHERFORECAST"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["FOR"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["GERMAN"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["BIGHT"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["NORTHEAST"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["TO"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["NORTH"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["INCREASING"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["ABOUT"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["EASTERN"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["PART"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["LATER"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["DECREASING"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["A"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["LITTLE"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["SHIFTING"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["EAST"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["EASTERN"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["PART"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AT"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["TIMES"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["MISTY"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["SEA"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["INCREASING"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["METRE"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["OUTLOOK"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["WESTERN"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["PART"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["NORTH"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["TO"],2)
			self.assertEqual(result["analysis"]["unknown"][8]["OTHERWISE"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["EAST"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["SOUTHEAST"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][3]["UNTIL"],1)
			self.assertEqual(result["analysis"]["known"][3]["UTC"],1)
			self.assertEqual(result["analysis"]["known"][7]["UNTIL"],1)
			self.assertEqual(result["analysis"]["known"][7]["UTC"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "S","E","94" ))

			self.assertNotIn("DTG", result["analysis"])




	def test_analysis_NA22_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")

		analyzer = NavtexAnalyzer("M")

		with open(self.NA22, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 107) # 1 + 2 + 8 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "NA22" ],
					[ "110905", "UTC", "MAR", "19" ],
					[ "NORWEGIAN", "NAV.", "WARNING", "184/2019" ],
					[ "CHART", "N36" ],
					[ "AREA", "GRIP" ],
					[ "HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE" ],
					[ "NNNN" ]
				]
			)
			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertEqual(result["analysis"]["coords"][6]["63-12.0N"],1)
			self.assertEqual(result["analysis"]["coords"][6]["007-43.8E"],1)

			self.assertIn("alnums", result["analysis"])
			self.assertIsInstance(result["analysis"]["alnums"], dict)
			self.assertEqual(result["analysis"]["alnums"][4]["N36"],1)

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][2]["110905"],1)
			self.assertEqual(result["analysis"]["nums"][2]["19"],1)
			self.assertEqual(result["analysis"]["nums"][3]["184/2019"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["MAR"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NORWEGIAN"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NAV"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["WARNING"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["CHART"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AREA"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["GRIP"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["HILBAAAN"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["RACON"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["IS"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["INOPERATIVE"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertFalse(len(result["analysis"]["known"]))

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertNotIn("header", result["analysis"])

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				"03/11/2019 0905"
			)




	def test_analysis_IA76_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('ICE')")

		analyzer = NavtexAnalyzer("I")

		with open(self.IA76, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 117) # 1 + 4 + 16 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "IA76" ],
					[ "210800", "UTC", "JAN" ],
					[ "BALTIC", "ICE", "INFORMATION" ],
					[
						"VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO",
						"TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "'ICEINFO'"
					],
					[ "ON", "VHF", "OR" ],
					[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
					[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH78." ],
					[
						"ARRIVAL", "REPORT", "ON", "VHF", "CH16",
						"WHEN", "THE", "SHIP", "IS", "WELL", "MOORED."
					],
					[
						"DEPARTURE", "REPORT", "ON", "VHF", "CH16",
						"LATEST", "6", "HOURS", "BEFORE", "DEPARTURE."
					],
					[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "'BALTICE.ORG'" ],
				]
			)

			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertFalse(len(result["analysis"]["coords"]))

			self.assertIn("alnums", result["analysis"])
			self.assertIsInstance(result["analysis"]["alnums"], dict)
			self.assertEqual(result["analysis"]["alnums"][7]["N60"],1)
			self.assertEqual(result["analysis"]["alnums"][7]["CH78"],1)
			self.assertEqual(result["analysis"]["alnums"][8]["CH16"],1)
			self.assertEqual(result["analysis"]["alnums"][9]["CH16"],1)

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][6]["0"],1)
			self.assertEqual(result["analysis"]["nums"][6]["10"],1)
			self.assertEqual(result["analysis"]["nums"][6]["492"],1)
			self.assertEqual(result["analysis"]["nums"][6]["76"],1)
			self.assertEqual(result["analysis"]["nums"][6]["00"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["JAN"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["BALTIC"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["INFORMATION"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["VESSELS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["BOUND"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["FOR"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["PORTS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SUBJECT"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["TO"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["TRAFFIC"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["RESTRICTIONS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SHALL"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["CALL"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["ICEINFO"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["OR"],1)

			self.assertEqual(result["analysis"]["unknown"][6]["PHONE"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["+46"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["AS"],1)
			self.assertEqual(result["analysis"]["unknown"][6]["FOLLOWS"],1)

			self.assertEqual(result["analysis"]["unknown"][7]["WHEN"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["PASSING"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["LAT"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][7]["VHF"],1)

			self.assertEqual(result["analysis"]["unknown"][8]["ARRIVAL"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["REPORT"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["WHEN"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["THE"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["SHIP"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["IS"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["WELL"],1)
			self.assertEqual(result["analysis"]["unknown"][8]["MOORED"],1)

			self.assertEqual(result["analysis"]["unknown"][9]["DEPARTURE"],2)
			self.assertEqual(result["analysis"]["unknown"][9]["REPORT"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["ON"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["VHF"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["LATEST"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["HOURS"],1)
			self.assertEqual(result["analysis"]["unknown"][9]["BEFORE"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][3]["ICE"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "I","A","76" ))

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				f"01/21/{TimeTurner().format('%Y')} 0800"
			)




	def test_analysis_VA28_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('ICE')")

		analyzer = NavtexAnalyzer("V")

		with open(self.VA28, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 101) # 1 + 4 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "VA28" ],
					[ "050550", "UTC", "AUG" ],
					[ "WZ", "724" ],
					[
						"GMDSS.", "HUMBER", "COASTGUARD.", "1.", "MF", "R/T",
						"AND", "DSC", "SERVICES", "FROM", "LANGHAM", "SITE"
					],
					[
						"52-56.5N", "000-57.2E.", "OFF", "AIR.", "2.",
						"CANCEL", "WZ", "597", "(GA73)", "(VA10)."
					],
					[ "NNN" ],
				]
			)

			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertEqual(result["analysis"]["coords"][5]["52-56.5N"],1)
			self.assertEqual(result["analysis"]["coords"][5]["000-57.2E"],1)

			self.assertIn("alnums", result["analysis"])
			self.assertFalse(len(result["analysis"]["alnums"]))

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][2]["050550"],1)
			self.assertEqual(result["analysis"]["nums"][3]["724"],1)
			self.assertEqual(result["analysis"]["nums"][4]["1"],1)
			self.assertEqual(result["analysis"]["nums"][5]["2"],1)
			self.assertEqual(result["analysis"]["nums"][5]["597"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["AUG"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["WZ"],1)

			self.assertEqual(result["analysis"]["unknown"][4]["GMDSS"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["HUMBER"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["COASTGUARD"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["MF"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["R/T"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["AND"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["DSC"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SERVICES"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["FROM"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["LANGHAM"],1)
			self.assertEqual(result["analysis"]["unknown"][4]["SITE"],1)

			self.assertEqual(result["analysis"]["unknown"][5]["OFF"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["AIR"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["CANCEL"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["WZ"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["GA73"],1)
			self.assertEqual(result["analysis"]["unknown"][5]["VA10"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertFalse(len(result["analysis"]["known"]))

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertIn("header", result["analysis"])
			self.assertEqual(result["analysis"]["header"],( "V","A","28" ))

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				f"08/05/{TimeTurner().format('%Y')} 0550"
			)




	def test_analysis_MZ56_bytes(self):

		with self.connection:

			self.connection.execute("DROP TABLE IF EXISTS navbow_test")
			self.connection.execute("CREATE TABLE navbow_test (word TEXT UNIQUE NOT NULL PRIMARY KEY)")
			self.connection.execute("INSERT INTO navbow_test VALUES ('HAND')")

		analyzer = NavtexAnalyzer("V")

		with open(self.MZ56, "rb") as F:

			result = analyzer(F.read())
			self.assertIsInstance(result, dict)
			self.assertEqual(len(result), 4)
			self.assertEqual(result.get("state"), 121) # 1 + 8 + 16 + 32 + 64
			self.assertIsInstance(result.get("raw"), list)
			self.assertIsInstance(result.get("air"), list)
			self.assertEqual(

				result.get("air"),
				[
					[ "ZCZC", "MZ56" ],
					[ "011713", "UTC", "AUG", "19" ],
					[ "NAVAREA", "1", "-", "NO", "MESSAGES", "ON", "HAND" ],
					[ "NNNN" ],
				]
			)

			self.assertIsInstance(result.get("analysis"), dict)

			self.assertIn("coords", result["analysis"])
			self.assertIsInstance(result["analysis"]["coords"], dict)
			self.assertFalse(len(result["analysis"]["coords"]))

			self.assertIn("alnums", result["analysis"])
			self.assertFalse(len(result["analysis"]["alnums"]))

			self.assertIn("nums", result["analysis"])
			self.assertIsInstance(result["analysis"]["nums"], dict)
			self.assertEqual(result["analysis"]["nums"][2]["011713"],1)
			self.assertEqual(result["analysis"]["nums"][2]["19"],1)
			self.assertEqual(result["analysis"]["nums"][3]["1"],1)

			self.assertIn("unknown", result["analysis"])
			self.assertIsInstance(result["analysis"]["unknown"], dict)
			self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)
			self.assertEqual(result["analysis"]["unknown"][2]["AUG"],1)

			self.assertEqual(result["analysis"]["unknown"][3]["NAVAREA"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["-"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["NO"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["MESSAGES"],1)
			self.assertEqual(result["analysis"]["unknown"][3]["ON"],1)

			self.assertIn("known", result["analysis"])
			self.assertIsInstance(result["analysis"]["known"], dict)
			self.assertEqual(result["analysis"]["known"][3]["HAND"],1)

			self.assertIn("punct", result["analysis"])
			self.assertIsInstance(result["analysis"]["punct"], dict)
			self.assertFalse(len(result["analysis"]["punct"]))

			self.assertNotIn("header", result["analysis"])

			self.assertIn("DTG", result["analysis"])
			self.assertIsInstance(result["analysis"]["DTG"], float)
			self.assertEqual(

				TimeTurner(result["analysis"]["DTG"]).format("%m/%d/%Y %H%M"),
				"08/01/2019 1713"
			)








	def test_pretty_air_valid1(self):

		analyzer = NavtexAnalyzer("I")
		the_day = TimeTurner()
		m = the_day.b.upper()
		d = f"{the_day.d}0800"
		r = str()
		target = {

			"analysis":	{

				"header":	( "I", "A", "76" ),
				"DTG":		the_day.epoch,
				"unknown":	{},
				"punct":	{}
			},
			"state":	93,
			"air":		[
				[ "ZCZC", "IA76" ],
				[ d, "UTC", m ],
				[ "BALTIC", "ICE", "INFORMATION" ],
				[ "VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO", "TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "ICEINFO" ],
				[ "ON", "VHF", "OR" ],
				[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
				[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH78." ],
				[ "ARRIVAL", "REPORT", "ON", "VHF", "CH16", "WHEN", "THE", "SHIP", "IS", "WELL", "MOORED." ],
				[ "DEPARTURE", "REPORT", "ON", "VHF", "CH16", "LATEST", "6", "HOURS", "BEFORE", "DEPARTURE." ],
				[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "BALTICE.ORG" ],
				[ "NNNN" ]
			]
		}
		self.assertEqual(
			analyzer.pretty_air(target),
			(	"1    ZCZC IA76\n"
				"2    %s UTC %s\n"
				"3    BALTIC ICE INFORMATION\n"
				"4    VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL ICEINFO\n"
				"5    ON VHF OR\n"
				"6    PHONE +46 (0)10 492 76 00 AS FOLLOWS:\n"
				"7    WHEN PASSING LAT N60 ON VHF CH78.\n"
				"8    ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.\n"
				"9    DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.\n"
				"10   FOR INFORMATION ON RESTRICTIONS GO TO BALTICE.ORG\n"
				"11   NNNN"
			)%(d,m)
		)


	def test_pretty_air_valid2(self):

		analyzer = NavtexAnalyzer("J")
		the_day = TimeTurner(days=1)
		m = the_day.b.upper()
		d = f"{the_day.d}0800"
		r = str()
		target = {

			"analysis":	{

				"DTG":		the_day.epoch,
				"unknown":	{ 4: { "VHF": 1 }, 8: { "VHF": 2, "CH16": 1 }},
				"punct":	{ 5: { ")": 1 }, 9: { "(": 2 }}
			},
			"state":	113,
			"air":		[
				[ d, "UTC", m ],
				[ "BALTIC", "ICE", "INFORMATION" ],
				[ "VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO", "TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "ICEINFO" ],
				[ "ON", "VHF", "OR" ],
				[ "PHONE", "+46", "(0)10", "492)", "76", "00", "AS", "FOLLOWS:" ],
				[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH78." ],
				[ "ARRIVAL", "REPORT", "ON", "VHF", "CH16", "WHEN", "THE", "SHIP", "IS", "WELL", "MOORED." ],
				[ "DEPARTURE", "REPORT", "ON", "VHF", "CH16", "LATEST", "6", "HOURS", "BEFORE", "DEPARTURE." ],
				[ "FOR", "INFORMATION", "ON", "((RESTRICTIONS", "GO", "TO", "BALTICE.ORG" ]
			]
		}
		self.assertEqual(
			analyzer.pretty_air(target),
			(	"1    %s UTC %s\n"
				"2    BALTIC ICE INFORMATION\n"
				"3    VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL ICEINFO\n"
				"4    ON VHF OR\n"
				"5    PHONE +46 (0)10 492) 76 00 AS FOLLOWS:\n"
				"6    WHEN PASSING LAT N60 ON VHF CH78.\n"
				"7    ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.\n"
				"8    DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.\n"
				"9    FOR INFORMATION ON ((RESTRICTIONS GO TO BALTICE.ORG\n"
				"\ninvalid header (ZCZC)"
				"\nmessage is outdated"
				"\nunknown word \"VHF\" at line 4"
				"\nunknown word \"CH16\" at line 8"
				"\nunknown 2 words \"VHF\" at line 8"
				"\nunmatched \")\" at line 5"
				"\nunmatched 2 \"(\" at line 9"
				"\ninvalid EoS (NNNN)"
			)%(d,m)
		)


	def test_pretty_air_valid3(self):

		analyzer = NavtexAnalyzer("I")
		the_day = TimeTurner()
		m = the_day.b.upper()
		d = f"{the_day.d}0800"
		r = str()
		target = {

			"analysis":	{

				"header":	( "I", "A", "76" ),
				"DTG":		the_day.epoch,
				"unknown":	{ 1: "word" },
				"punct":	{ 2: "coma" }
			},
			"state":	93,
			"air":		[
				[ "ZCZC", "IA76" ],
				[ d, "UTC", m ],
				[ "BALTIC", "ICE", "INFORMATION" ],
				[ "VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO", "TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "ICEINFO" ],
				[ "ON", "VHF", "OR" ],
				[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
				[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH78." ],
				[ "ARRIVAL", "REPORT", "ON", "VHF", "CH16", "WHEN", "THE", "SHIP", "IS", "WELL", "MOORED." ],
				[ "DEPARTURE", "REPORT", "ON", "VHF", "CH16", "LATEST", "6", "HOURS", "BEFORE", "DEPARTURE." ],
				[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "BALTICE.ORG" ],
				[ "NNNN" ]
			]
		}
		self.assertEqual(
			analyzer.pretty_air(target),
			(	"1    ZCZC IA76\n"
				"2    %s UTC %s\n"
				"3    BALTIC ICE INFORMATION\n"
				"4    VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL ICEINFO\n"
				"5    ON VHF OR\n"
				"6    PHONE +46 (0)10 492 76 00 AS FOLLOWS:\n"
				"7    WHEN PASSING LAT N60 ON VHF CH78.\n"
				"8    ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.\n"
				"9    DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.\n"
				"10   FOR INFORMATION ON RESTRICTIONS GO TO BALTICE.ORG\n"
				"11   NNNN\n"
				"\nunknown words check failed due to TypeError: "
				"string indices must be integers, not 'str'"
				"\nunmatched punctuation check failed due to TypeError: "
				"string indices must be integers, not 'str'"
			)%(d,m)
		)


	def test_pretty_air_valid4(self):

		analyzer = NavtexAnalyzer("I")
		target = {

			"analysis":	{

				"header":	( "I", "A", "76" ),
				"unknown":	{ 1: "word" },
				"punct":	{ 2: "coma" }
			},
			"state":	93,
			"air":		[
				[ "ZCZC", "IA76" ],
				[ "BALTIC", "ICE", "INFORMATION" ],
				[ "VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO", "TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "ICEINFO" ],
				[ "ON", "VHF", "OR" ],
				[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
				[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH78." ],
				[ "ARRIVAL", "REPORT", "ON", "VHF", "CH16", "WHEN", "THE", "SHIP", "IS", "WELL", "MOORED." ],
				[ "DEPARTURE", "REPORT", "ON", "VHF", "CH16", "LATEST", "6", "HOURS", "BEFORE", "DEPARTURE." ],
				[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "BALTICE.ORG" ],
				[ "NNNN" ]
			]
		}
		self.assertEqual(
			analyzer.pretty_air(target),
			(	"1    ZCZC IA76\n"
				"2    BALTIC ICE INFORMATION\n"
				"3    VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL ICEINFO\n"
				"4    ON VHF OR\n"
				"5    PHONE +46 (0)10 492 76 00 AS FOLLOWS:\n"
				"6    WHEN PASSING LAT N60 ON VHF CH78.\n"
				"7    ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.\n"
				"8    DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.\n"
				"9    FOR INFORMATION ON RESTRICTIONS GO TO BALTICE.ORG\n"
				"10   NNNN\n"
				"\npublish date and time not found"
				"\nunknown words check failed due to TypeError: "
				"string indices must be integers, not 'str'"
				"\nunmatched punctuation check failed due to TypeError: "
				"string indices must be integers, not 'str'"
			)
		)


	def test_pretty_air_invalid(self):

		analyzer = NavtexAnalyzer("L")
		for invalid in (

			"", "lines", 42, 69., True, False, None, ..., print, unittest, NavtexAnalyzer,
			([ "OOH", "EEH" ],[ "OOH", "AH", "AH" ]),
			(( "OOH", "EEH" ),( "OOH", "AH", "AH" )),
			[( "OOH", "EEH" ),( "OOH", "AH", "AH" )],
			{ "OOH", "EEH", "AH" },
			{ "OOH": "EEH" },
			{ "state": 93 },
			{ "state": 93, "air": []},
			{ "state": 93, "air": [], "analysis": {}},
			{ "state": 93, "air": [], "analysis": { "DTG": TimeTurner().epoch }},
			{
				"state":	93,
				"air":		[],
				"analysis":	{
					"DTG":		TimeTurner().epoch,
					"unknown":	{}
				}
			}
		):
			with self.subTest(invalid=invalid):
				self.assertRaises(AssertionError, analyzer.pretty_air, invalid)




	def test_pretty_DTG_valid(self):

		analyzer = NavtexAnalyzer("D")
		target1 = datetime.today()
		target2 = TimeTurner(days=1)
		target3 = TimeTurner(days=-1)
		self.assertEqual(analyzer.pretty_DTG(target1),"")
		self.assertEqual(analyzer.pretty_DTG(target2),"\nmessage is outdated")
		self.assertEqual(analyzer.pretty_DTG(target3.epoch),"\nmessage is outdated")
		self.assertEqual(analyzer.pretty_DTG(None),"\npublish date and time not found")


	def test_pretty_DTG_invalid(self):

		analyzer = NavtexAnalyzer("D")
		for invalid in (

			"", "lines", ..., print, unittest, NavtexAnalyzer,
			([ "OOH", "EEH" ],[ "OOH", "AH", "AH" ]),
			(( "OOH", "EEH" ),( "OOH", "AH", "AH" )),
			[( "OOH", "EEH" ),( "OOH", "AH", "AH" )],
			{ "OOH", "EEH", "AH" },
			{ "OOH": "EEH" }
		):
			with self.subTest(invalid=invalid):
				self.assertRegex(analyzer.pretty_DTG(invalid), "\ndatetime group check failed due to ")




	def test_pretty_unknown_valid(self):

		analyzer = NavtexAnalyzer("M")
		target = {

			5:	{ "ISING": 1 },
			10:	{ "GOAST": 2 }
		}
		self.assertEqual(

			analyzer.pretty_unknown(target),
			"\nunknown word \"ISING\" at line 5"
			"\nunknown 2 words \"GOAST\" at line 10"
		)


	def test_pretty_unknown_empty(self):

		target = dict()
		analyzer = NavtexAnalyzer("M")
		self.assertEqual(analyzer.pretty_unknown(target),"")


	def test_pretty_unknown_invalid(self):

		analyzer = NavtexAnalyzer("M")
		for invalid in (

			"lines", 42, 69., True, False, None, ..., print, unittest, NavtexAnalyzer,
			([ "OOH", "EEH" ],[ "OOH", "AH", "AH" ]),
			(( "OOH", "EEH" ),( "OOH", "AH", "AH" )),
			[( "OOH", "EEH" ),( "OOH", "AH", "AH" )],
			{ "OOH", "EEH", "AH" },
			{ "OOH": "EEH" },
			{ 5: { "ISING": 1, "GOAST": None }},
			{ 5: { "ISING": 1, "GOAST": print }},
		):
			self.assertRegex(analyzer.pretty_unknown(invalid),"\nunknown words check failed due to ")




	def test_pretty_punct_valid(self):

		analyzer = NavtexAnalyzer("N")
		target = {

			4:	{ "'": 1 },
			7:	{ ")": 2 }
		}
		self.assertEqual(

			analyzer.pretty_punct(target),
			"\nunmatched \"'\" at line 4"
			"\nunmatched 2 \")\" at line 7"
		)


	def test_pretty_punct_empty(self):

		target = dict()
		analyzer = NavtexAnalyzer("N")
		self.assertEqual(analyzer.pretty_punct(target),"")


	def test_pretty_punct_invalid(self):

		analyzer = NavtexAnalyzer("N")
		for invalid in (

			"lines", 42, 69., True, False, None, ..., print, unittest, NavtexAnalyzer,
			([ "OOH", "EEH" ],[ "OOH", "AH", "AH" ]),
			(( "OOH", "EEH" ),( "OOH", "AH", "AH" )),
			[( "OOH", "EEH" ),( "OOH", "AH", "AH" )],
			{ "OOH", "EEH", "AH" },
			{ "OOH": "EEH" }
		):
			self.assertRegex(analyzer.pretty_punct(invalid),"\nunmatched punctuation check failed due to ")








if __name__ == "__main__" : unittest.main(verbosity=2)







