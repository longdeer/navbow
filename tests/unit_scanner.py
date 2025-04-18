import	os
import	unittest
import	NavtexBoWAnalyzer
from	NavtexBoWAnalyzer.scanner import word_scan
from	NavtexBoWAnalyzer.scanner import byte_scan
from	NavtexBoWAnalyzer.scanner import sanit_state








class SannerCase(unittest.TestCase):

	wd = os.path.join(NavtexBoWAnalyzer.__path__[0], "tests")
	# Invalid:
	# WZ29
	# Not sanit:
	# OL66
	# Valid:
	# JA94
	# BA33
	# NA22
	# GA10
	# IA76
	# QA42
	# KA60
	# MZ56
	# VA28
	# RA28
	# SE94


	def test_word_scan_1(self):

		lines = [

			[ "151930", "UTC", "FEB" ],
			[ "CANCEL", "GERMAN", "NAV", "WARN", "079'19" ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "151930", "UTC", "FEB" ],
					2: [ "CANCEL", "GERMAN", "NAV", "WARN", "079'19" ],
				},
				[( 2,"'" )]
			)
		)


	def test_word_scan_2(self):

		lines = [

			[ "(151930)", "((UTC))", "'FEB'" ],
			[ "('CANCEL')", "'('GERMAN')'", "\"NAV\"", "(\"WARN\")", "079'19" ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "151930", "UTC", "FEB" ],
					2: [ "CANCEL", "GERMAN", "NAV", "WARN", "079'19" ],
				},
				[( 2,"'" )]
			)
		)


	def test_word_scan_3(self):

		lines = [

			[ "(151930", "UTC)", "(FEB" ],
			[ "CANCEL", "(GERMAN))", "(\"NAV", "WARN\")", "\"(079'19)\"" ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "151930", "UTC", "FEB" ],
					2: [ "CANCEL", "GERMAN", "NAV", "WARN", "079'19)\"" ],
				},
				[( 2,"\"" ),( 2,"(" ),( 2,"'" ),( 2,")" ),( 2,"\"" )]
			)
		)


	def test_word_scan_4(self):

		lines = [

			[ "(151930", "UTC))", "(FEB" ],
			[ "(CANCEL", "(GERMAN))", "(\"NAV", "WARN)", "(079'19)\"" ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "151930", "UTC", "FEB" ],
					2: [ "CANCEL", "GERMAN", "NAV", "WARN)", "079'19)\"" ],
				},
				[
					( 1,")" ),( 1,"(" ),( 2,"(" ),( 2,"\"" ),( 2,")" ),
					( 2,"(" ),( 2,"'" ),( 2,")" ),( 2,"\"" )
				]
			)
		)


	def test_word_scan_5(self):

		lines = [

			[ "((151930", "UTC)", "(FEB" ],
			[ "CANCEL", "'(GERMAN))", "\"(NAV", "WARN\")", "\"(079'19\")" ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "151930", "UTC", "FEB" ],
					2: [ "CANCEL", "GERMAN", "NAV", "WARN\")", "079'19\")" ],
				},
				[
					( 1,"(" ),( 1,"(" ),( 2,"'" ),( 2,")" ),( 2,"\"" ),( 2,"(" ),( 2,"\"" ),
					( 2,")" ),( 2,"\"" ),( 2,"(" ),( 2,"'" ),( 2,"\"" ),( 2,")" )
				]
			)
		)


	def test_word_scan_6(self):

		lines = [

			[ "((((((((()))))))))", "('\"\"')", "(''\"\"()())" ],
			[ "''('\"()\"')''", "''''''''''", "\"\"\"\"\"\"\"\"\"\"" ],
		]
		self.assertEqual(word_scan(lines),({},[]))


	def test_word_scan_7(self):

		lines = [[ "CTF", "311", "PHONE", "(44)(0)1923", "956366." ]]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "CTF", "311", "PHONE", "44", "0", "1923", "956366" ],
				},
				[]
			)
		)


	def test_word_scan_8(self):

		lines = []
		self.assertEqual(word_scan(lines),({},[]))


	def test_word_scan_9(self):

		lines = [[],[],[]]
		self.assertEqual(word_scan(lines),({},[]))


	def test_word_scan_10(self):

		lines = [

			[ "(", ")", "'", "'", "\"", "\"" ],
			[ "(", "'", "\"", ")", "'", "\"" ],
		]
		self.assertEqual(

			word_scan(lines),
			({},[( 2,"(" ),( 2,"'" ),( 2,"\"" ),( 2,")" ),( 2,"'" ),( 2,"\"" )])
		)


	def test_word_scan_11(self):

		lines = [

			[ "GUNNERY", "EXERCISES", "IN", "'", "R", "154", "'" ],
			[ "AND", "'", "R", "157", "'", "(CHART", "7066Z)" ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "GUNNERY", "EXERCISES", "IN", "R", "154" ],
					2: [ "AND", "R", "157", "CHART", "7066Z" ],
				},
				[]
			)
		)


	def test_word_scan_12(self):

		lines = [[ "ANTICYCLONE'S", "INFLUENCE" ]]
		self.assertEqual(word_scan(lines),({ 1: [ "ANTICYCLONE'S", "INFLUENCE" ]},[( 1,"'" )]))


	def test_word_scan_13(self):

		lines = [[ "ANTICYCLONE'", "INFLUENCE" ]]
		self.assertEqual(word_scan(lines),({ 1: [ "ANTICYCLONE'", "INFLUENCE" ]},[( 1,"'" )]))


	def test_word_scan_14(self):

		lines = [[ "BUOY", "M2", "53", "29'N", "5", "26'W" ]]
		self.assertEqual(word_scan(lines),({ 1: [ "BUOY", "M2", "53", "29'N", "5", "26", "W" ]},[]))


	def test_word_scan_15(self):

		lines = [

			[ "BUOY.", "BUOY..", "BUOY.,", "BUOY.:", "BUOY:.",  ],
			[ "BUOY,", "BUOY,.", "BUOY,,", "BUOY,:", "BUOY:,",  ],
			[ "BUOY:", "BUOY::", "BUOY,,:", "BUOY.,:", "BUOY..:",  ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "BUOY", "BUOY.", "BUOY.", "BUOY.", "BUOY:",  ],
					2: [ "BUOY", "BUOY,", "BUOY,", "BUOY,", "BUOY:",  ],
					3: [ "BUOY", "BUOY:", "BUOY,,", "BUOY.,", "BUOY..",  ],
				},
				[]
			)
		)








	def test_byte_scan_invalid(self):

		broken,message = byte_scan(os.path.join(self.wd, "WZ29"))
		self.assertTrue(broken)
		self.assertIsInstance(message,str)
		self.assertTrue(len(message))

	def test_byte_scan_valid(self):

		broken,message = byte_scan(os.path.join(self.wd, "KA60"))
		self.assertFalse(broken)
		self.assertIsInstance(message,str)
		self.assertTrue(len(message))

	def test_byte_scan_others(self):

		for other in (

			int(), float(), bool(), None, ..., print, unittest,
			[ "file" ],( "file", ),{ "file" },{ "path": "file" }
		):
			broken,message = byte_scan(other)
			self.assertTrue(broken)
			self.assertIsInstance(message,str)
			self.assertFalse(len(message))

	def test_byte_scan_empty(self):

		broken,message = byte_scan(os.path.join(self.wd, "empty"))
		self.assertFalse(broken)
		self.assertIsInstance(message,str)
		self.assertFalse(len(message))

	def test_byte_scan_spaces(self):

		broken,message = byte_scan(os.path.join(self.wd, "spaces"))
		self.assertFalse(broken)
		self.assertIsInstance(message,str)
		self.assertTrue(len(message))








	def test_sanit_invalid(self):

		scan = sanit_state(os.path.join(self.wd, "WZ29"))
		self.assertIsInstance(scan, dict)
		self.assertEqual(len(scan),2)
		self.assertEqual(scan.get("sanit"),0)
		self.assertIsInstance(scan.get("message"),str)
		self.assertTrue(len(scan.get("message")))


	def test_sanit_empty(self):

		self.assertEqual(

			sanit_state(os.path.join(self.wd, "empty")),
			{
				"raw_lines":	[],
				"air_lines":	[],
				"chunks":		set(),
				"symbols":		set(),
				"sanit":		0,
			}
		)


	def test_sanit_spaces(self):

		self.assertEqual(

			sanit_state(os.path.join(self.wd, "spaces")),
			{
				"raw_lines":	[],
				"air_lines":	[],
				"chunks":		set(),
				"symbols":		set(),
				"sanit":		0,
			}
		)


	def test_sanit_JA94(self):

		self.assertEqual(

			sanit_state(os.path.join(self.wd, "JA94")),
			{
				"raw_lines": [

					"ZCZC JA94",
					"151930 UTC FEB",
					"CANCEL GERMAN NAV WARN 079/19",
					"NNNN",
				],
				"air_lines": [

					[ "ZCZC", "JA94" ],
					[ "151930", "UTC", "FEB" ],
					[ "CANCEL", "GERMAN", "NAV", "WARN", "079/19" ],
					[ "NNNN" ]
				],
				"chunks": set((

					"079/19",
					"JA94",
					"NAV",
					"FEB",
					"CANCEL",
					"ZCZC",
					"NNNN",
					"UTC",
					"GERMAN",
					"WARN",
					"151930",
				)),
				"symbols":	set("B/M3TUEF5CL4J1WNV079GARZ"),
				"sanit":	1,
			}
		)


	def test_sanit_BA33(self):

		self.assertEqual(

			sanit_state(os.path.join(self.wd, "BA33")),
			{
				"raw_lines": [

					"ZCZC BA33",
					"181136 UTC MAR 19",
					"NORWEGIAN NAV. WARNING 198/2019",
					"CHART 73",
					"AREA LOFOTEN INNERSIDEN",
					"FESTVAAG LIGHT 68-10.2N 014-12.6E IS UNLIT.",
					"NNNN",

				],
				"air_lines": [

					[ "ZCZC", "BA33" ],
					[ "181136", "UTC", "MAR", "19" ],
					[ "NORWEGIAN", "NAV.", "WARNING", "198/2019" ],
					[ "CHART", "73" ],
					[ "AREA", "LOFOTEN", "INNERSIDEN" ],
					[ "FESTVAAG", "LIGHT", "68-10.2N", "014-12.6E", "IS", "UNLIT." ],
					[ "NNNN" ]
				],
				"chunks": set((

					"181136",
					"19",
					"UTC",
					"WARNING",
					"NORWEGIAN",
					"CHART",
					"NAV.",
					"LIGHT",
					"AREA",
					"014-12.6E",
					"LOFOTEN",
					"ZCZC",
					"IS",
					"MAR",
					"68-10.2N",
					"198/2019",
					"BA33",
					"FESTVAAG",
					"NNNN",
					"73",
					"UNLIT.",
					"INNERSIDEN",
				)),
				"symbols":	set("73.ECMBR-8FZNV/L0UG2O69W1DTASH4I"),
				"sanit":	1,
			}
		)


	def test_sanit_NA22(self):

		self.assertEqual(

			sanit_state(os.path.join(self.wd, "IA76")),
			{
				"raw_lines": [

					"ZCZC IA76",
					"210800 UTC JAN",
					"BALTIC ICE INFORMATION",
					"VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL 'ICEINFO'",
					"ON VHF OR",
					"PHONE +46 (0)10 492 76 00 AS FOLLOWS:",
					"WHEN PASSING LAT N60 ON VHF CH 78.",
					"ARRIVAL REPORT ON VHF CH 16 WHEN THE SHIP IS WELL MOORED.",
					"DEPARTURE REPORT ON VHF CH 16 LATEST 6 HOURS BEFORE DEPARTURE.",
					"FOR INFORMATION ON RESTRICTIONS GO TO 'BALTICE.ORG'",
					"NNNN",
				],
				"air_lines": [

					[ "ZCZC", "IA76" ],
					[ "210800", "UTC", "JAN" ],
					[ "BALTIC", "ICE", "INFORMATION" ],
					[
						"VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO",
						"TRAFFIC", "RESTRICTIONS","SHALL", "CALL", "'ICEINFO'"
					],
					[ "ON", "VHF", "OR" ],
					[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
					[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH", "78." ],
					[
						"ARRIVAL", "REPORT", "ON", "VHF", "CH", "16",
						"WHEN", "THE","SHIP", "IS", "WELL", "MOORED."
					],
					[
						"DEPARTURE", "REPORT", "ON", "VHF", "CH", "16",
						"LATEST", "6", "HOURS", "BEFORE", "DEPARTURE."
					],
					[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "'BALTICE.ORG'" ],
					[ "NNNN" ]
				],
				"chunks": set((

					"+46",
					"UTC",
					"PORTS",
					"ZCZC",
					"INFORMATION",
					"PHONE",
					"76",
					"DEPARTURE",
					"'ICEINFO'",
					"210800",
					"ON",
					"16",
					"'BALTICE.ORG'",
					"00",
					"BALTIC",
					"AS",
					"TRAFFIC",
					"WHEN",
					"WELL",
					"OR",
					"THE",
					"6",
					"N60",
					"RESTRICTIONS",
					"CALL",
					"SHALL",
					"SHIP",
					"VHF",
					"IS",
					"ARRIVAL",
					"REPORT",
					"VESSELS",
					"(0)10",
					"NNNN",
					"MOORED.",
					"BEFORE",
					"BOUND",
					"LAT",
					"ICE",
					"IA76",
					"PASSING",
					"LATEST",
					"JAN",
					"78.",
					"CH",
					"GO",
					"TO",
					"FOR",
					"DEPARTURE.",
					"FOLLOWS:",
					"HOURS",
					"492",
					"SUBJECT",
				)),
				"symbols":	set("(9PRZDG+:6A0WM.SU48C2H1FJE)T7BIOLN'V"),
				"sanit":	1,
			}
		)


	def test_sanit_IA76(self):

		self.assertEqual(

			sanit_state(os.path.join(self.wd, "IA76")),
			{
				"raw_lines": [

					"ZCZC IA76",
					"210800 UTC JAN",
					"BALTIC ICE INFORMATION",
					"VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL 'ICEINFO'",
					"ON VHF OR",
					"PHONE +46 (0)10 492 76 00 AS FOLLOWS:",
					"WHEN PASSING LAT N60 ON VHF CH 78.",
					"ARRIVAL REPORT ON VHF CH 16 WHEN THE SHIP IS WELL MOORED.",
					"DEPARTURE REPORT ON VHF CH 16 LATEST 6 HOURS BEFORE DEPARTURE.",
					"FOR INFORMATION ON RESTRICTIONS GO TO 'BALTICE.ORG'",
					"NNNN",
				],
				"air_lines": [

					[ "ZCZC", "IA76" ],
					[ "210800", "UTC", "JAN" ],
					[ "BALTIC", "ICE", "INFORMATION" ],
					[
						"VESSELS", "BOUND", "FOR", "PORTS", "SUBJECT", "TO",
						"TRAFFIC", "RESTRICTIONS", "SHALL", "CALL", "'ICEINFO'"
					],
					[ "ON", "VHF", "OR" ],
					[ "PHONE", "+46", "(0)10", "492", "76", "00", "AS", "FOLLOWS:" ],
					[ "WHEN", "PASSING", "LAT", "N60", "ON", "VHF", "CH", "78." ],
					[
						"ARRIVAL", "REPORT", "ON", "VHF", "CH", "16",
						"WHEN", "THE", "SHIP", "IS", "WELL", "MOORED."
					],
					[
						"DEPARTURE", "REPORT", "ON", "VHF", "CH", "16",
						"LATEST", "6", "HOURS", "BEFORE", "DEPARTURE."
					],
					[ "FOR", "INFORMATION", "ON", "RESTRICTIONS", "GO", "TO", "'BALTICE.ORG'" ],
					[ "NNNN" ]
				],
				"chunks": set((

					"+46",
					"UTC",
					"PORTS",
					"ZCZC",
					"INFORMATION",
					"PHONE",
					"76",
					"DEPARTURE",
					"'ICEINFO'",
					"210800",
					"ON",
					"16",
					"'BALTICE.ORG'",
					"00",
					"BALTIC",
					"AS",
					"TRAFFIC",
					"WHEN",
					"WELL",
					"OR",
					"THE",
					"6",
					"N60",
					"RESTRICTIONS",
					"CALL",
					"SHALL",
					"SHIP",
					"VHF",
					"IS",
					"ARRIVAL",
					"REPORT",
					"VESSELS",
					"(0)10",
					"NNNN",
					"MOORED.",
					"BEFORE",
					"BOUND",
					"LAT",
					"ICE",
					"IA76",
					"PASSING",
					"LATEST",
					"JAN",
					"78.",
					"CH",
					"GO",
					"TO",
					"FOR",
					"DEPARTURE.",
					"FOLLOWS:",
					"HOURS",
					"492",
					"SUBJECT",
				)),
				"symbols":	set("(9PRZDG+:6A0WM.SU48C2H1FJE)T7BIOLN'V"),
				"sanit":	1,
			}
		)








if	__name__ == "__main__" : unittest.main(verbosity=2)







