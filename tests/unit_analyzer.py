import	os
import	unittest
import	NavtexBoWAnalyzer
from	NavtexBoWAnalyzer		 import Navanalyzer
from	NavtexBoWAnalyzer.header import B1
from	NavtexBoWAnalyzer.header import B2








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








	def test_states(self):

		analyzer = Navanalyzer("B")

		for state in [ 0 ] + list(range(1,65,2)):
			with self.subTest(state=state):

				self.assertEqual(

					analyzer.with_mapping(

						os.path.join(self.wd, "states", str(state)),
						{ "NAV": 1 }

					).get("state"),
					state
				)

		for state in list(range(81,96,2)):
			with self.subTest(state=state):

				self.assertEqual(

					analyzer.with_mapping(

						os.path.join(self.wd, "states", str(state)),
						{ "NAV": 1, "UTC": 1, "DEC": 1 }

					).get("state"),
					state
				)

		for state in list(range(97,128,2)):
			with self.subTest(state=state):

				self.assertEqual(

					analyzer.with_mapping(

						os.path.join(self.wd, "states", str(state)),
						{ "NAV": 1 }

					).get("state"),
					state
				)








	def test_analysis_WZ29(self):

		analyzer = Navanalyzer("W")
		result = analyzer.with_mapping(os.path.join(self.wd, "msg", "WZ29"), dict())
		self.assertIsInstance(result, dict)
		self.assertEqual(len(result), 2)
		self.assertEqual(result.get("state"), 0)
		self.assertIsInstance(result.get("message"), str)
		self.assertIn("*", result.get("message"))


	def test_analysis_JA94(self):

		analyzer = Navanalyzer("J")
		result = analyzer.with_mapping(os.path.join(self.wd, "msg", "JA94"), dict())
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


	def test_analysis_OL66(self):

		analyzer = Navanalyzer("O")
		result = analyzer.with_mapping(

			os.path.join(self.wd, "msg", "OL66"),
			{
				"CTF":		1,
				"SOUND":	1,
				"SOUTH":	1,
				"CONTACT":	1,
				"CANCEL":	0,
			}
		)
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
		self.assertEqual(result["analysis"]["nums"]["1"][3],1)
		self.assertEqual(result["analysis"]["nums"]["120600"][5],1)
		self.assertEqual(result["analysis"]["nums"]["130700"][5],1)
		self.assertEqual(result["analysis"]["nums"]["2"][6],1)
		self.assertEqual(result["analysis"]["nums"]["311"][8],1)
		self.assertEqual(result["analysis"]["nums"]["44"][8],1)
		self.assertEqual(result["analysis"]["nums"]["0"][8],1)
		self.assertEqual(result["analysis"]["nums"]["1923"][8],1)
		self.assertEqual(result["analysis"]["nums"]["956366"][8],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"]["OL66"][1],1)

		self.assertEqual(result["analysis"]["unknown"]["FOSNNI"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["SUBFACTS"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["AND"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["GUNFACTS"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["WARNING"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["ALL"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["TIMES"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["UTC"][2],1)

		self.assertEqual(result["analysis"]["unknown"]["DIVED"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["SUBMARINE"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["OPERATIONS"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["IN"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["PROGRESS"][3],1)

		self.assertEqual(result["analysis"]["unknown"]["INNER"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["INSIDE"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["OF"][4],3)
		self.assertEqual(result["analysis"]["unknown"]["SKYE"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["RUBHA"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["REIDH"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["NORTH"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["MALLAIG"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["BETWEEN"][4],1)

		self.assertEqual(result["analysis"]["unknown"]["AND"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["SEP"][5],1)

		self.assertEqual(result["analysis"]["unknown"]["LIVE"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["GUNNERY"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["FIRINGS"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["IN"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["PROGRESS"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["NIL"][6],1)

		self.assertEqual(result["analysis"]["unknown"]["FULL"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["DETAILS"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["IN"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["HM"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["COASTGUARD"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["RESCUE"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["CENTRES"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["VHF"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["AND"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["MF"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["BROADCASTS"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["OR"][7],1)

		self.assertEqual(result["analysis"]["unknown"]["PHONE"][8],1)

		self.assertEqual(result["analysis"]["unknown"]["CANCEL"][9],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"]["SOUND"][4],1)
		self.assertEqual(result["analysis"]["known"]["SOUTH"][4],1)
		self.assertEqual(result["analysis"]["known"]["CONTACT"][7],1)
		self.assertEqual(result["analysis"]["known"]["CTF"][8],1)

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))




	def test_analysis_QA42(self):

		analyzer = Navanalyzer("Q")
		result = analyzer.with_mapping(

			os.path.join(self.wd, "msg", "QA42"),
			{
				"CTF":			1,
				"SOUND":		1,
				"SOUTH":		1,
				"CONTACT":		1,
				"UNTIL":		1,
				"FURTHER":		1,
				"FROM":			1,
				"UTC":			1,
				"CONDUCTING":	1,
				"UNDERWATER":	1,
				"GAS":			1,
				"PIPELINE":		0,
				"CANCEL":		0,
			}
		)
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
		self.assertEqual(result["analysis"]["nums"]["092240"][1],1)
		self.assertEqual(result["analysis"]["nums"]["19"][1],1)

		self.assertEqual(result["analysis"]["nums"]["193/19"][3],1)

		self.assertEqual(result["analysis"]["nums"]["100-16"][4],1)

		self.assertEqual(result["analysis"]["nums"]["0700"][5],1)
		self.assertEqual(result["analysis"]["nums"]["1900"][5],1)
		self.assertEqual(result["analysis"]["nums"]["0500"][5],1)
		self.assertEqual(result["analysis"]["nums"]["1700"][5],1)

		self.assertEqual(result["analysis"]["nums"]["44"][7],1)
		self.assertEqual(result["analysis"]["nums"]["543"][7],1)
		self.assertEqual(result["analysis"]["nums"]["013"][7],1)
		self.assertEqual(result["analysis"]["nums"]["487"][7],1)

		self.assertEqual(result["analysis"]["nums"]["44"][8],1)
		self.assertEqual(result["analysis"]["nums"]["537"][8],1)
		self.assertEqual(result["analysis"]["nums"]["013"][8],1)
		self.assertEqual(result["analysis"]["nums"]["477"][8],1)

		self.assertEqual(result["analysis"]["nums"]["44"][9],1)
		self.assertEqual(result["analysis"]["nums"]["530"][9],1)
		self.assertEqual(result["analysis"]["nums"]["013"][9],1)
		self.assertEqual(result["analysis"]["nums"]["455"][9],1)

		self.assertEqual(result["analysis"]["nums"]["44"][10],1)
		self.assertEqual(result["analysis"]["nums"]["531"][10],1)
		self.assertEqual(result["analysis"]["nums"]["013"][10],1)
		self.assertEqual(result["analysis"]["nums"]["436"][10],1)

		self.assertEqual(result["analysis"]["nums"]["44"][11],1)
		self.assertEqual(result["analysis"]["nums"]["508"][11],1)
		self.assertEqual(result["analysis"]["nums"]["013"][11],1)
		self.assertEqual(result["analysis"]["nums"]["386"][11],1)

		self.assertEqual(result["analysis"]["nums"]["16"][12],1)

		self.assertEqual(result["analysis"]["nums"]["05"][13],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"]["JUN"][1],1)

		self.assertEqual(result["analysis"]["unknown"]["SPLIT"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["RADIO"][2],1)

		self.assertEqual(result["analysis"]["unknown"]["NAV"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["WNG"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["NR"][3],1)

		self.assertEqual(result["analysis"]["unknown"]["N-ERN"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["ADRIATIC"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][4],2)
		self.assertEqual(result["analysis"]["unknown"]["BRIJUNI"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["CHRT"][4],1)

		self.assertEqual(result["analysis"]["unknown"]["NOTICEFROM"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["LT"][5],2)
		self.assertEqual(result["analysis"]["unknown"]["TO"][5],2)
		self.assertEqual(result["analysis"]["unknown"]["M/V"][5],1)

		self.assertEqual(result["analysis"]["unknown"]["REFUL"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["PIPELINE"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["MAINTENANCE"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["WORKS"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["BETWEEN"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["POSITIONS"][6],1)

		self.assertEqual(result["analysis"]["unknown"]["A)"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["N"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["E"][7],1)

		self.assertEqual(result["analysis"]["unknown"]["B)"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["N"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["E"][8],1)

		self.assertEqual(result["analysis"]["unknown"]["C)"][9],1)
		self.assertEqual(result["analysis"]["unknown"]["N"][9],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][9],1)
		self.assertEqual(result["analysis"]["unknown"]["E"][9],1)

		self.assertEqual(result["analysis"]["unknown"]["D)"][10],1)
		self.assertEqual(result["analysis"]["unknown"]["N"][10],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][10],1)
		self.assertEqual(result["analysis"]["unknown"]["E"][10],1)

		self.assertEqual(result["analysis"]["unknown"]["E)"][11],1)
		self.assertEqual(result["analysis"]["unknown"]["N"][11],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][11],1)
		self.assertEqual(result["analysis"]["unknown"]["E"][11],1)

		self.assertEqual(result["analysis"]["unknown"]["VHF"][12],1)
		self.assertEqual(result["analysis"]["unknown"]["CH"][12],1)

		self.assertEqual(result["analysis"]["unknown"]["NAVIGATION"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["AND"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["FISHING"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["IN"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["RADIUS"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["MILES"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["THE"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["VESSEL"][13],1)
		self.assertEqual(result["analysis"]["unknown"]["PROHIBITED"][13],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"]["UTC"][1],1)
		self.assertEqual(result["analysis"]["known"]["UTC"][5],2)
		self.assertEqual(result["analysis"]["known"]["UNTIL"][5],1)
		self.assertEqual(result["analysis"]["known"]["FURTHER"][5],1)
		self.assertEqual(result["analysis"]["known"]["FROM"][5],1)
		self.assertEqual(result["analysis"]["known"]["GAS"][6],1)
		self.assertEqual(result["analysis"]["known"]["CONDUCTING"][6],1)
		self.assertEqual(result["analysis"]["known"]["UNDERWATER"][6],1)
		self.assertEqual(result["analysis"]["known"]["CONTACT"][12],1)
		self.assertEqual(result["analysis"]["known"]["FROM"][13],1)

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertEqual(result["analysis"]["punc"][")"][7],1)
		self.assertEqual(result["analysis"]["punc"][")"][8],1)
		self.assertEqual(result["analysis"]["punc"][")"][9],1)
		self.assertEqual(result["analysis"]["punc"][")"][10],1)
		self.assertEqual(result["analysis"]["punc"][")"][11],1)




	def test_analysis_SE94(self):

		analyzer = Navanalyzer("S")
		result = analyzer.with_mapping(

			os.path.join(self.wd, "msg", "SE94"),
			{
				"CTF":			1,
				"SOUND":		1,
				"SOUTH":		1,
				"CONTACT":		1,
				"UNTIL":		1,
				"FURTHER":		1,
				"FROM":			1,
				"UTC":			1,
				"CONDUCTING":	1,
				"UNDERWATER":	1,
				"GAS":			1,
				"PIPELINE":		0,
				"CANCEL":		0,
			}
		)
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
		self.assertEqual(result["analysis"]["nums"]["171900"][1],1)

		self.assertEqual(result["analysis"]["nums"]["18.11.2019"][2],1)
		self.assertEqual(result["analysis"]["nums"]["12"][2],1)

		self.assertEqual(result["analysis"]["nums"]["4"][3],1)
		self.assertEqual(result["analysis"]["nums"]["6"][3],1)

		self.assertEqual(result["analysis"]["nums"]["25"][5],1)

		self.assertEqual(result["analysis"]["nums"]["19.11.2019"][6],1)
		self.assertEqual(result["analysis"]["nums"]["00"][6],1)

		self.assertEqual(result["analysis"]["nums"]["6"][7],1)
		self.assertEqual(result["analysis"]["nums"]["7"][7],1)
		self.assertEqual(result["analysis"]["nums"]["5"][7],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)

		self.assertEqual(result["analysis"]["unknown"]["NAVTEX-HAMBURG"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["NCC"][1],1)

		self.assertEqual(result["analysis"]["unknown"]["WEATHERFORECAST"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["FOR"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["GERMAN"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["BIGHT"][2],1)

		self.assertEqual(result["analysis"]["unknown"]["NORTHEAST"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["TO"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["NORTH"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["INCREASING"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["ABOUT"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["EASTERN"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["PART"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["LATER"][3],1)

		self.assertEqual(result["analysis"]["unknown"]["DECREASING"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["A"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["LITTLE"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["AND"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["SHIFTING"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["EAST"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["EASTERN"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["PART"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["AT"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["TIMES"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["MISTY"][4],1)

		self.assertEqual(result["analysis"]["unknown"]["SEA"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["INCREASING"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["METRE"][5],1)

		self.assertEqual(result["analysis"]["unknown"]["OUTLOOK"][6],1)

		self.assertEqual(result["analysis"]["unknown"]["WESTERN"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["PART"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["NORTH"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["TO"][7],2)
		self.assertEqual(result["analysis"]["unknown"]["OTHERWISE"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["EAST"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["SOUTHEAST"][7],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"]["UNTIL"][2],1)
		self.assertEqual(result["analysis"]["known"]["UTC"][2],1)
		self.assertEqual(result["analysis"]["known"]["UNTIL"][6],1)
		self.assertEqual(result["analysis"]["known"]["UTC"][6],1)

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))




	def test_analysis_NA22(self):

		analyzer = Navanalyzer("M")
		result = analyzer.with_mapping(os.path.join(self.wd, "msg", "NA22"), dict())
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
		self.assertEqual(result["analysis"]["coords"]["63-12.0N"][5],1)
		self.assertEqual(result["analysis"]["coords"]["007-43.8E"][5],1)

		self.assertIn("alnums", result["analysis"])
		self.assertIsInstance(result["analysis"]["alnums"], dict)
		self.assertEqual(result["analysis"]["alnums"]["N36"][3],1)

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"]["110905"][1],1)
		self.assertEqual(result["analysis"]["nums"]["19"][1],1)
		self.assertEqual(result["analysis"]["nums"]["184/2019"][2],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"]["UTC"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["MAR"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["NORWEGIAN"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["NAV"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["WARNING"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["CHART"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["AREA"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["GRIP"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["HILBAAAN"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["RACON"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["IS"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["INOPERATIVE"][5],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))
		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))




	def test_analysis_IA76(self):

		analyzer = Navanalyzer("I")
		result = analyzer.with_mapping(os.path.join(self.wd, "msg", "IA76"), { "ICE": 1 })
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
		self.assertEqual(result["analysis"]["alnums"]["N60"][6],1)
		self.assertEqual(result["analysis"]["alnums"]["CH78"][6],1)
		self.assertEqual(result["analysis"]["alnums"]["CH16"][7],1)
		self.assertEqual(result["analysis"]["alnums"]["CH16"][8],1)

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"]["0"][5],1)
		self.assertEqual(result["analysis"]["nums"]["10"][5],1)
		self.assertEqual(result["analysis"]["nums"]["492"][5],1)
		self.assertEqual(result["analysis"]["nums"]["76"][5],1)
		self.assertEqual(result["analysis"]["nums"]["00"][5],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"]["UTC"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["JAN"][1],1)

		self.assertEqual(result["analysis"]["unknown"]["BALTIC"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["INFORMATION"][2],1)

		self.assertEqual(result["analysis"]["unknown"]["VESSELS"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["BOUND"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["FOR"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["PORTS"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["SUBJECT"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["TO"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["TRAFFIC"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["RESTRICTIONS"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["SHALL"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["CALL"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["ICEINFO"][3],1)

		self.assertEqual(result["analysis"]["unknown"]["ON"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["VHF"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["OR"][4],1)

		self.assertEqual(result["analysis"]["unknown"]["PHONE"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["+46"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["AS"][5],1)
		self.assertEqual(result["analysis"]["unknown"]["FOLLOWS"][5],1)

		self.assertEqual(result["analysis"]["unknown"]["WHEN"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["PASSING"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["LAT"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["ON"][6],1)
		self.assertEqual(result["analysis"]["unknown"]["VHF"][6],1)

		self.assertEqual(result["analysis"]["unknown"]["ARRIVAL"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["REPORT"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["ON"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["VHF"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["WHEN"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["THE"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["SHIP"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["IS"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["WELL"][7],1)
		self.assertEqual(result["analysis"]["unknown"]["MOORED"][7],1)

		self.assertEqual(result["analysis"]["unknown"]["DEPARTURE"][8],2)
		self.assertEqual(result["analysis"]["unknown"]["REPORT"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["ON"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["VHF"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["LATEST"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["HOURS"][8],1)
		self.assertEqual(result["analysis"]["unknown"]["BEFORE"][8],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"]["ICE"][2],1)

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))




	def test_analysis_VA28(self):

		analyzer = Navanalyzer("V")
		result = analyzer.with_mapping(os.path.join(self.wd, "msg", "VA28"), { "ICE": 1 })
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
		self.assertEqual(result["analysis"]["coords"]["52-56.5N"][4],1)
		self.assertEqual(result["analysis"]["coords"]["000-57.2E"][4],1)

		self.assertIn("alnums", result["analysis"])
		self.assertFalse(len(result["analysis"]["alnums"]))

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"]["050550"][1],1)
		self.assertEqual(result["analysis"]["nums"]["724"][2],1)
		self.assertEqual(result["analysis"]["nums"]["1"][3],1)
		self.assertEqual(result["analysis"]["nums"]["2"][4],1)
		self.assertEqual(result["analysis"]["nums"]["597"][4],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"]["UTC"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["AUG"][1],1)

		self.assertEqual(result["analysis"]["unknown"]["WZ"][2],1)

		self.assertEqual(result["analysis"]["unknown"]["GMDSS"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["HUMBER"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["COASTGUARD"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["MF"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["R/T"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["AND"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["DSC"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["SERVICES"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["FROM"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["LANGHAM"][3],1)
		self.assertEqual(result["analysis"]["unknown"]["SITE"][3],1)

		self.assertEqual(result["analysis"]["unknown"]["OFF"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["AIR"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["CANCEL"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["WZ"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["GA73"][4],1)
		self.assertEqual(result["analysis"]["unknown"]["VA10"][4],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))




	def test_analysis_MZ56(self):

		analyzer = Navanalyzer("V")
		result = analyzer.with_mapping(os.path.join(self.wd, "msg", "MZ56"), { "HAND": 1 })
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
		self.assertEqual(result["analysis"]["nums"]["011713"][1],1)
		self.assertEqual(result["analysis"]["nums"]["19"][1],1)
		self.assertEqual(result["analysis"]["nums"]["1"][2],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"]["UTC"][1],1)
		self.assertEqual(result["analysis"]["unknown"]["AUG"][1],1)

		self.assertEqual(result["analysis"]["unknown"]["NAVAREA"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["-"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["NO"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["MESSAGES"][2],1)
		self.assertEqual(result["analysis"]["unknown"]["ON"][2],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"]["HAND"][2],1)

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))








if __name__ == "__main__" : unittest.main(verbosity=2)







