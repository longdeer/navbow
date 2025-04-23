import	os
import	unittest
import	datetime
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

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC A{subject}{number}"),
					( "A", subject, number )
				)


	def test_B_valid_header(self):

		analyzer = Navanalyzer("B")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC B{subject}{number}"),
					( "B", subject, number )
				)


	def test_C_valid_header(self):

		analyzer = Navanalyzer("C")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC C{subject}{number}"),
					( "C", subject, number )
				)


	def test_D_valid_header(self):

		analyzer = Navanalyzer("D")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC D{subject}{number}"),
					( "D", subject, number )
				)


	def test_E_valid_header(self):

		analyzer = Navanalyzer("E")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC E{subject}{number}"),
					( "E", subject, number )
				)


	def test_F_valid_header(self):

		analyzer = Navanalyzer("F")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC F{subject}{number}"),
					( "F", subject, number )
				)


	def test_G_valid_header(self):

		analyzer = Navanalyzer("G")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC G{subject}{number}"),
					( "G", subject, number )
				)


	def test_H_valid_header(self):

		analyzer = Navanalyzer("H")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC H{subject}{number}"),
					( "H", subject, number )
				)


	def test_I_valid_header(self):

		analyzer = Navanalyzer("I")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC I{subject}{number}"),
					( "I", subject, number )
				)


	def test_J_valid_header(self):

		analyzer = Navanalyzer("J")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC J{subject}{number}"),
					( "J", subject, number )
				)


	def test_K_valid_header(self):

		analyzer = Navanalyzer("K")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC K{subject}{number}"),
					( "K", subject, number )
				)


	def test_L_valid_header(self):

		analyzer = Navanalyzer("L")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC L{subject}{number}"),
					( "L", subject, number )
				)


	def test_M_valid_header(self):

		analyzer = Navanalyzer("M")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC M{subject}{number}"),
					( "M", subject, number )
				)


	def test_N_valid_header(self):

		analyzer = Navanalyzer("N")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC N{subject}{number}"),
					( "N", subject, number )
				)


	def test_O_valid_header(self):

		analyzer = Navanalyzer("O")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC O{subject}{number}"),
					( "O", subject, number )
				)


	def test_P_valid_header(self):

		analyzer = Navanalyzer("P")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC P{subject}{number}"),
					( "P", subject, number )
				)


	def test_Q_valid_header(self):

		analyzer = Navanalyzer("Q")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC Q{subject}{number}"),
					( "Q", subject, number )
				)


	def test_R_valid_header(self):

		analyzer = Navanalyzer("R")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC R{subject}{number}"),
					( "R", subject, number )
				)


	def test_S_valid_header(self):

		analyzer = Navanalyzer("S")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC S{subject}{number}"),
					( "S", subject, number )
				)


	def test_T_valid_header(self):

		analyzer = Navanalyzer("T")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC T{subject}{number}"),
					( "T", subject, number )
				)


	def test_U_valid_header(self):

		analyzer = Navanalyzer("U")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC U{subject}{number}"),
					( "U", subject, number )
				)


	def test_V_valid_header(self):

		analyzer = Navanalyzer("V")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC V{subject}{number}"),
					( "V", subject, number )
				)


	def test_W_valid_header(self):

		analyzer = Navanalyzer("W")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC W{subject}{number}"),
					( "W", subject, number )
				)


	def test_X_valid_header(self):

		analyzer = Navanalyzer("X")

		for subject in B2:
			for i in range(100):

				number = str(i).zfill(2)
				self.assertEqual(

					analyzer.is_valid_header(f"ZCZC X{subject}{number}"),
					( "X", subject, number )
				)


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
		self.assertEqual(result["analysis"]["nums"][1]["151930"],1)
		self.assertEqual(result["analysis"]["nums"][2]["079/19"],1)
		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][1]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][1]["FEB"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["CANCEL"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["GERMAN"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["NAV"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["WARN"],1)
		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))
		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertFalse(len(result["analysis"]["pending"]))
		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))
		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "J","A","94" ))
		self.assertIn("cdt", result["analysis"])
		self.assertIsInstance(result["analysis"]["cdt"], datetime.datetime)
		self.assertEqual(

			result["analysis"]["cdt"].strftime("%m/%d/%Y %H%M"),
			f"02/15/{datetime.datetime.today().strftime('%Y')} 1930"
		)




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
		self.assertEqual(result["analysis"]["nums"][3]["1"],1)
		self.assertEqual(result["analysis"]["nums"][5]["120600"],1)
		self.assertEqual(result["analysis"]["nums"][5]["130700"],1)
		self.assertEqual(result["analysis"]["nums"][6]["2"],1)
		self.assertEqual(result["analysis"]["nums"][8]["311"],1)
		self.assertEqual(result["analysis"]["nums"][8]["44"],1)
		self.assertEqual(result["analysis"]["nums"][8]["0"],1)
		self.assertEqual(result["analysis"]["nums"][8]["1923"],1)
		self.assertEqual(result["analysis"]["nums"][8]["956366"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][1]["OL66"],1)

		self.assertEqual(result["analysis"]["unknown"][2]["FOSNNI"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["SUBFACTS"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["GUNFACTS"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["WARNING"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["ALL"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["TIMES"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["UTC"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["DIVED"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["SUBMARINE"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["OPERATIONS"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["PROGRESS"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["INNER"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["INSIDE"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["OF"],3)
		self.assertEqual(result["analysis"]["unknown"][4]["SKYE"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["RUBHA"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["REIDH"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["NORTH"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["MALLAIG"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["BETWEEN"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["SEP"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["LIVE"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["GUNNERY"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["FIRINGS"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["PROGRESS"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["NIL"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["FULL"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["DETAILS"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["HM"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["COASTGUARD"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["RESCUE"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["CENTRES"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["MF"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["BROADCASTS"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["OR"],1)

		self.assertEqual(result["analysis"]["unknown"][8]["PHONE"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][4]["SOUND"],1)
		self.assertEqual(result["analysis"]["known"][4]["SOUTH"],1)
		self.assertEqual(result["analysis"]["known"][7]["CONTACT"],1)
		self.assertEqual(result["analysis"]["known"][8]["CTF"],1)

		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertEqual(result["analysis"]["pending"][9]["CANCEL"],1)

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "O","L","66" ))

		self.assertNotIn("cdt", result["analysis"])




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
		self.assertEqual(result["analysis"]["nums"][1]["092240"],1)
		self.assertEqual(result["analysis"]["nums"][1]["19"],1)

		self.assertEqual(result["analysis"]["nums"][3]["193/19"],1)

		self.assertEqual(result["analysis"]["nums"][4]["100-16"],1)

		self.assertEqual(result["analysis"]["nums"][5]["0700"],1)
		self.assertEqual(result["analysis"]["nums"][5]["1900"],1)
		self.assertEqual(result["analysis"]["nums"][5]["0500"],1)
		self.assertEqual(result["analysis"]["nums"][5]["1700"],1)

		self.assertEqual(result["analysis"]["nums"][7]["44"],1)
		self.assertEqual(result["analysis"]["nums"][7]["543"],1)
		self.assertEqual(result["analysis"]["nums"][7]["013"],1)
		self.assertEqual(result["analysis"]["nums"][7]["487"],1)

		self.assertEqual(result["analysis"]["nums"][8]["44"],1)
		self.assertEqual(result["analysis"]["nums"][8]["537"],1)
		self.assertEqual(result["analysis"]["nums"][8]["013"],1)
		self.assertEqual(result["analysis"]["nums"][8]["477"],1)

		self.assertEqual(result["analysis"]["nums"][9]["44"],1)
		self.assertEqual(result["analysis"]["nums"][9]["530"],1)
		self.assertEqual(result["analysis"]["nums"][9]["013"],1)
		self.assertEqual(result["analysis"]["nums"][9]["455"],1)

		self.assertEqual(result["analysis"]["nums"][10]["44"],1)
		self.assertEqual(result["analysis"]["nums"][10]["531"],1)
		self.assertEqual(result["analysis"]["nums"][10]["013"],1)
		self.assertEqual(result["analysis"]["nums"][10]["436"],1)

		self.assertEqual(result["analysis"]["nums"][11]["44"],1)
		self.assertEqual(result["analysis"]["nums"][11]["508"],1)
		self.assertEqual(result["analysis"]["nums"][11]["013"],1)
		self.assertEqual(result["analysis"]["nums"][11]["386"],1)

		self.assertEqual(result["analysis"]["nums"][12]["16"],1)

		self.assertEqual(result["analysis"]["nums"][13]["05"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][1]["JUN"],1)

		self.assertEqual(result["analysis"]["unknown"][2]["SPLIT"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["RADIO"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["NAV"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["WNG"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["NR"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["N-ERN"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["ADRIATIC"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["-"],2)
		self.assertEqual(result["analysis"]["unknown"][4]["BRIJUNI"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["CHRT"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["NOTICEFROM"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["LT"],2)
		self.assertEqual(result["analysis"]["unknown"][5]["TO"],2)
		self.assertEqual(result["analysis"]["unknown"][5]["M/V"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["REFUL"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["MAINTENANCE"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["WORKS"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["BETWEEN"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["POSITIONS"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["A)"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][8]["B)"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][9]["C)"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][9]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][10]["D)"],1)
		self.assertEqual(result["analysis"]["unknown"][10]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][10]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][10]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][11]["E)"],1)
		self.assertEqual(result["analysis"]["unknown"][11]["N"],1)
		self.assertEqual(result["analysis"]["unknown"][11]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][11]["E"],1)

		self.assertEqual(result["analysis"]["unknown"][12]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][12]["CH"],1)

		self.assertEqual(result["analysis"]["unknown"][13]["NAVIGATION"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["FISHING"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["IN"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["RADIUS"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["MILES"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["THE"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["VESSEL"],1)
		self.assertEqual(result["analysis"]["unknown"][13]["PROHIBITED"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][1]["UTC"],1)
		self.assertEqual(result["analysis"]["known"][5]["UTC"],2)
		self.assertEqual(result["analysis"]["known"][5]["UNTIL"],1)
		self.assertEqual(result["analysis"]["known"][5]["FURTHER"],1)
		self.assertEqual(result["analysis"]["known"][5]["FROM"],1)
		self.assertEqual(result["analysis"]["known"][6]["GAS"],1)
		self.assertEqual(result["analysis"]["known"][6]["CONDUCTING"],1)
		self.assertEqual(result["analysis"]["known"][6]["UNDERWATER"],1)
		self.assertEqual(result["analysis"]["known"][12]["CONTACT"],1)
		self.assertEqual(result["analysis"]["known"][13]["FROM"],1)

		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertEqual(result["analysis"]["pending"][6]["PIPELINE"],1)

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertEqual(result["analysis"]["punc"][7][")"],1)
		self.assertEqual(result["analysis"]["punc"][8][")"],1)
		self.assertEqual(result["analysis"]["punc"][9][")"],1)
		self.assertEqual(result["analysis"]["punc"][10][")"],1)
		self.assertEqual(result["analysis"]["punc"][11][")"],1)

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "Q","A","42" ))

		self.assertIn("cdt", result["analysis"])
		self.assertIsInstance(result["analysis"]["cdt"], datetime.datetime)
		self.assertEqual(

			result["analysis"]["cdt"].strftime("%m/%d/%Y %H%M"),
			"06/09/2019 2240"
		)




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
		self.assertEqual(result["analysis"]["nums"][1]["171900"],1)

		self.assertEqual(result["analysis"]["nums"][2]["18.11.2019"],1)
		self.assertEqual(result["analysis"]["nums"][2]["12"],1)

		self.assertEqual(result["analysis"]["nums"][3]["4"],1)
		self.assertEqual(result["analysis"]["nums"][3]["6"],1)

		self.assertEqual(result["analysis"]["nums"][5]["25"],1)

		self.assertEqual(result["analysis"]["nums"][6]["19.11.2019"],1)
		self.assertEqual(result["analysis"]["nums"][6]["00"],1)

		self.assertEqual(result["analysis"]["nums"][7]["6"],1)
		self.assertEqual(result["analysis"]["nums"][7]["7"],1)
		self.assertEqual(result["analysis"]["nums"][7]["5"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)

		self.assertEqual(result["analysis"]["unknown"][1]["NAVTEX-HAMBURG"],1)
		self.assertEqual(result["analysis"]["unknown"][1]["NCC"],1)

		self.assertEqual(result["analysis"]["unknown"][2]["WEATHERFORECAST"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["FOR"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["GERMAN"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["BIGHT"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["NORTHEAST"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["TO"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["NORTH"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["INCREASING"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["ABOUT"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["EASTERN"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["PART"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["LATER"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["DECREASING"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["A"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["LITTLE"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["SHIFTING"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["EAST"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["EASTERN"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["PART"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["AT"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["TIMES"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["MISTY"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["SEA"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["INCREASING"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["METRE"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["OUTLOOK"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["WESTERN"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["PART"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["NORTH"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["TO"],2)
		self.assertEqual(result["analysis"]["unknown"][7]["OTHERWISE"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["EAST"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["SOUTHEAST"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][2]["UNTIL"],1)
		self.assertEqual(result["analysis"]["known"][2]["UTC"],1)
		self.assertEqual(result["analysis"]["known"][6]["UNTIL"],1)
		self.assertEqual(result["analysis"]["known"][6]["UTC"],1)

		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertFalse(len(result["analysis"]["pending"]))

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "S","E","94" ))

		self.assertNotIn("cdt", result["analysis"])




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
		self.assertEqual(result["analysis"]["coords"][5]["63-12.0N"],1)
		self.assertEqual(result["analysis"]["coords"][5]["007-43.8E"],1)

		self.assertIn("alnums", result["analysis"])
		self.assertIsInstance(result["analysis"]["alnums"], dict)
		self.assertEqual(result["analysis"]["alnums"][3]["N36"],1)

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"][1]["110905"],1)
		self.assertEqual(result["analysis"]["nums"][1]["19"],1)
		self.assertEqual(result["analysis"]["nums"][2]["184/2019"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][1]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][1]["MAR"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["NORWEGIAN"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["NAV"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["WARNING"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["CHART"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["AREA"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["GRIP"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["HILBAAAN"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["RACON"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["IS"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["INOPERATIVE"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))

		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertFalse(len(result["analysis"]["pending"]))

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))

		self.assertNotIn("header", result["analysis"])

		self.assertIn("cdt", result["analysis"])
		self.assertIsInstance(result["analysis"]["cdt"], datetime.datetime)
		self.assertEqual(

			result["analysis"]["cdt"].strftime("%m/%d/%Y %H%M"),
			"03/11/2019 0905"
		)




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
		self.assertEqual(result["analysis"]["alnums"][6]["N60"],1)
		self.assertEqual(result["analysis"]["alnums"][6]["CH78"],1)
		self.assertEqual(result["analysis"]["alnums"][7]["CH16"],1)
		self.assertEqual(result["analysis"]["alnums"][8]["CH16"],1)

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"][5]["0"],1)
		self.assertEqual(result["analysis"]["nums"][5]["10"],1)
		self.assertEqual(result["analysis"]["nums"][5]["492"],1)
		self.assertEqual(result["analysis"]["nums"][5]["76"],1)
		self.assertEqual(result["analysis"]["nums"][5]["00"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][1]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][1]["JAN"],1)

		self.assertEqual(result["analysis"]["unknown"][2]["BALTIC"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["INFORMATION"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["VESSELS"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["BOUND"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["FOR"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["PORTS"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["SUBJECT"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["TO"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["TRAFFIC"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["RESTRICTIONS"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["SHALL"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["CALL"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["ICEINFO"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["OR"],1)

		self.assertEqual(result["analysis"]["unknown"][5]["PHONE"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["+46"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["AS"],1)
		self.assertEqual(result["analysis"]["unknown"][5]["FOLLOWS"],1)

		self.assertEqual(result["analysis"]["unknown"][6]["WHEN"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["PASSING"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["LAT"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][6]["VHF"],1)

		self.assertEqual(result["analysis"]["unknown"][7]["ARRIVAL"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["REPORT"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["WHEN"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["THE"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["SHIP"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["IS"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["WELL"],1)
		self.assertEqual(result["analysis"]["unknown"][7]["MOORED"],1)

		self.assertEqual(result["analysis"]["unknown"][8]["DEPARTURE"],2)
		self.assertEqual(result["analysis"]["unknown"][8]["REPORT"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["ON"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["VHF"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["LATEST"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["HOURS"],1)
		self.assertEqual(result["analysis"]["unknown"][8]["BEFORE"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][2]["ICE"],1)

		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertFalse(len(result["analysis"]["pending"]))

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "I","A","76" ))

		self.assertIn("cdt", result["analysis"])
		self.assertIsInstance(result["analysis"]["cdt"], datetime.datetime)
		self.assertEqual(

			result["analysis"]["cdt"].strftime("%m/%d/%Y %H%M"),
			f"01/21/{datetime.datetime.today().strftime('%Y')} 0800"
		)




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
		self.assertEqual(result["analysis"]["coords"][4]["52-56.5N"],1)
		self.assertEqual(result["analysis"]["coords"][4]["000-57.2E"],1)

		self.assertIn("alnums", result["analysis"])
		self.assertFalse(len(result["analysis"]["alnums"]))

		self.assertIn("nums", result["analysis"])
		self.assertIsInstance(result["analysis"]["nums"], dict)
		self.assertEqual(result["analysis"]["nums"][1]["050550"],1)
		self.assertEqual(result["analysis"]["nums"][2]["724"],1)
		self.assertEqual(result["analysis"]["nums"][3]["1"],1)
		self.assertEqual(result["analysis"]["nums"][4]["2"],1)
		self.assertEqual(result["analysis"]["nums"][4]["597"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][1]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][1]["AUG"],1)

		self.assertEqual(result["analysis"]["unknown"][2]["WZ"],1)

		self.assertEqual(result["analysis"]["unknown"][3]["GMDSS"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["HUMBER"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["COASTGUARD"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["MF"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["R/T"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["AND"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["DSC"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["SERVICES"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["FROM"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["LANGHAM"],1)
		self.assertEqual(result["analysis"]["unknown"][3]["SITE"],1)

		self.assertEqual(result["analysis"]["unknown"][4]["OFF"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["AIR"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["CANCEL"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["WZ"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["GA73"],1)
		self.assertEqual(result["analysis"]["unknown"][4]["VA10"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertFalse(len(result["analysis"]["known"]))

		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertFalse(len(result["analysis"]["pending"]))

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))

		self.assertIn("header", result["analysis"])
		self.assertEqual(result["analysis"]["header"],( "V","A","28" ))

		self.assertIn("cdt", result["analysis"])
		self.assertIsInstance(result["analysis"]["cdt"], datetime.datetime)
		self.assertEqual(

			result["analysis"]["cdt"].strftime("%m/%d/%Y %H%M"),
			f"08/05/{datetime.datetime.today().strftime('%Y')} 0550"
		)




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
		self.assertEqual(result["analysis"]["nums"][1]["011713"],1)
		self.assertEqual(result["analysis"]["nums"][1]["19"],1)
		self.assertEqual(result["analysis"]["nums"][2]["1"],1)

		self.assertIn("unknown", result["analysis"])
		self.assertIsInstance(result["analysis"]["unknown"], dict)
		self.assertEqual(result["analysis"]["unknown"][1]["UTC"],1)
		self.assertEqual(result["analysis"]["unknown"][1]["AUG"],1)

		self.assertEqual(result["analysis"]["unknown"][2]["NAVAREA"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["-"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["NO"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["MESSAGES"],1)
		self.assertEqual(result["analysis"]["unknown"][2]["ON"],1)

		self.assertIn("known", result["analysis"])
		self.assertIsInstance(result["analysis"]["known"], dict)
		self.assertEqual(result["analysis"]["known"][2]["HAND"],1)

		self.assertIn("pending", result["analysis"])
		self.assertIsInstance(result["analysis"]["pending"], dict)
		self.assertFalse(len(result["analysis"]["pending"]))

		self.assertIn("punc", result["analysis"])
		self.assertIsInstance(result["analysis"]["punc"], dict)
		self.assertFalse(len(result["analysis"]["punc"]))

		self.assertNotIn("header", result["analysis"])

		self.assertIn("cdt", result["analysis"])
		self.assertIsInstance(result["analysis"]["cdt"], datetime.datetime)
		self.assertEqual(

			result["analysis"]["cdt"].strftime("%m/%d/%Y %H%M"),
			"08/01/2019 1713"
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







