import os
import sys

tests_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_root)
analyzer_root = os.path.join(project_root,"analyzer")
if(project_root not in sys.path): sys.path.insert(0,project_root)
if(analyzer_root not in sys.path): sys.path.insert(0,analyzer_root)

import	unittest
from	scanner import word_scan
from	scanner import byte_scan
from	scanner import sanit_state








class SannerCase(unittest.TestCase):

	maxDiff = None
	# Broken:
	# WZ29			+
	# Not sanit:
	# OL66
	# NA22			+
	# Bad EoS:
	# IA76			+
	# VA28
	# Bad header:
	# MZ56
	# Valid:
	# JA94			+
	# BA33			+
	# GA10
	# QA42
	# KA60			+
	# RA28
	# SE94

	@classmethod
	def setUpClass(cls):

		cls.KA60 = os.path.join(tests_root, "msg", "KA60")
		cls.JA94 = os.path.join(tests_root, "msg", "JA94")
		cls.BA33 = os.path.join(tests_root, "msg", "BA33")
		cls.NA22 = os.path.join(tests_root, "msg", "NA22")
		cls.IA76 = os.path.join(tests_root, "msg", "IA76")
		cls.empty_file = os.path.join(tests_root, "msg", "empty")
		cls.spaces_file = os.path.join(tests_root, "msg", "spaces")
		cls.corrupted_file = os.path.join(tests_root, "msg", "WZ29")


	def test_word_scan_001(self):

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


	def test_word_scan_002(self):

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


	def test_word_scan_003(self):

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


	def test_word_scan_004(self):

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


	def test_word_scan_005(self):

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


	def test_word_scan_006(self):

		lines = [

			[ "((((((((()))))))))", "('\"\"')", "(''\"\"()())" ],
			[ "''('\"()\"')''", "''''''''''", "\"\"\"\"\"\"\"\"\"\"" ],
		]
		self.assertEqual(word_scan(lines),({},[]))


	def test_word_scan_007(self):

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


	def test_word_scan_008(self):

		lines = []
		self.assertEqual(word_scan(lines),({},[]))


	def test_word_scan_009(self):

		lines = [[],[],[]]
		self.assertEqual(word_scan(lines),({},[]))


	def test_word_scan_010(self):

		lines = [

			[ "(", ")", "'", "'", "\"", "\"" ],
			[ "(", "'", "\"", ")", "'", "\"" ],
		]
		self.assertEqual(

			word_scan(lines),
			({},[( 2,"(" ),( 2,"'" ),( 2,"\"" ),( 2,")" ),( 2,"'" ),( 2,"\"" )])
		)


	def test_word_scan_011(self):

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


	def test_word_scan_012(self):

		lines = [[ "ANTICYCLONE'S", "INFLUENCE" ]]
		self.assertEqual(word_scan(lines),({ 1: [ "ANTICYCLONE'S", "INFLUENCE" ]},[( 1,"'" )]))


	def test_word_scan_013(self):

		lines = [[ "ANTICYCLONE'", "INFLUENCE" ]]
		self.assertEqual(word_scan(lines),({ 1: [ "ANTICYCLONE'", "INFLUENCE" ]},[( 1,"'" )]))


	def test_word_scan_014(self):

		lines = [[ "BUOY", "M2", "53", "29'N", "5", "26'W" ]]
		self.assertEqual(word_scan(lines),({ 1: [ "BUOY", "M2", "53", "29'N", "5", "26", "W" ]},[]))


	def test_word_scan_015(self):

		# Consecutive punctuations will be considered as words
		lines = [

			[ "BUOY.", "BUOY..", "BUOY.,", "BUOY.:", "BUOY:.",  ],
			[ "BUOY,", "BUOY,.", "BUOY,,", "BUOY,:", "BUOY:,",  ],
			[ "BUOY:", "BUOY::", "BUOY,,:", "BUOY.,:", "BUOY..:"  ],
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "BUOY", "BUOY.", "BUOY.", "BUOY.", "BUOY", "."  ],
					2: [ "BUOY", "BUOY", ".", "BUOY", ",", "BUOY", ":", "BUOY", ","  ],
					3: [ "BUOY", "BUOY", ":", "BUOY", ",", "BUOY.", ":", "BUOY.."  ]
				},
				[]
			)
		)


	def test_word_scan_016(self):

		lines = [[ "N-ERN", "ADRIATIC", "-", "BRIJUNI", "-", "CHRT:100-16"  ]]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "N-ERN", "ADRIATIC", "-", "BRIJUNI", "-", "CHRT", "100-16"  ]
				},
				[]
			)
		)


	def test_word_scan_017(self):

		lines = [

			[ "(NAV):", "(NAV).", "(NAV),", "(NAV)-" ],
			[ "'NAV':", "'NAV'.", "'NAV',", "'NAV'-" ],
			[ "\"NAV\":", "\"NAV\".", "\"NAV\",", "\"NAV\"-" ]
		]
		self.assertEqual(

			word_scan(lines),
			(
				{
					1: [ "NAV", "NAV", "NAV", "NAV" ],
					2: [ "NAV", "NAV", "NAV", "NAV" ],
					3: [ "NAV", "NAV", "NAV", "NAV" ]
				},
				[]
			)
		)








	def test_byte_scan_direct_NL(self):

		origin = "\nZCZC AZ42\nNO MESSAGE ON HAND\n"
		broken,message = byte_scan(origin)
		self.assertFalse(broken)
		self.assertEqual(message,origin)
		self.assertFalse("*" in message)

	def test_byte_scan_direct_CR(self):

		broken,message = byte_scan("\rZCZC AZ42\rNO MESSAGE ON HAND\r")
		self.assertFalse(broken)
		self.assertEqual(message,"\nZCZC AZ42\nNO MESSAGE ON HAND\n")
		self.assertFalse("*" in message)

	def test_byte_scan_direct_CRNL(self):

		broken,message = byte_scan("\r\nZCZC AZ42\r\nNO MESSAGE ON HAND\r\n")
		self.assertFalse(broken)
		self.assertEqual(message,"\nZCZC AZ42\nNO MESSAGE ON HAND\n")
		self.assertFalse("*" in message)

	def test_byte_scan_direct_NLCR(self):

		broken,message = byte_scan("\n\rZCZC AZ42\n\rNO MESSAGE ON HAND\n\r")
		self.assertFalse(broken)
		self.assertEqual(message,"\nZCZC AZ42\nNO MESSAGE ON HAND\n")
		self.assertFalse("*" in message)

	def test_byte_scan_direct_equal_mesh(self):

		broken,message = byte_scan("\r\n\n\rZCZC AZ42\r\r\n\nNO MESSAGE ON HAND\r\n\n\r")
		self.assertFalse(broken)
		self.assertEqual(message,"\n\nZCZC AZ42\n\n\nNO MESSAGE ON HAND\n\n")
		self.assertFalse("*" in message)

	def test_byte_scan_direct_inequal_mesh(self):

		broken,message = byte_scan("\r\n\r\n\rZCZC AZ42\r\r\n\r\nNO MESSAGE ON HAND\r\n\n\n\r")
		self.assertFalse(broken)
		self.assertEqual(message,"\n\n\nZCZC AZ42\n\n\nNO MESSAGE ON HAND\n\n\n")
		self.assertFalse("*" in message)




	def test_byte_scan_corrupted_file(self):

		broken,message = byte_scan(self.corrupted_file)
		self.assertTrue(broken)
		self.assertIsInstance(message,str)
		self.assertTrue(len(message))
		self.assertTrue("*" in message)

	def test_byte_scan_valid_file(self):

		broken,message = byte_scan(self.KA60)
		self.assertFalse(broken)
		self.assertIsInstance(message,str)
		self.assertTrue(len(message))
		self.assertFalse("*" in message)

	def test_byte_scan_empty_file(self):

		broken,message = byte_scan(self.empty_file)
		self.assertFalse(broken)
		self.assertIsInstance(message,str)
		self.assertFalse(len(message))
		self.assertFalse("*" in message)

	def test_byte_scan_spaces_file(self):

		broken,message = byte_scan(self.spaces_file)
		self.assertFalse(broken)
		self.assertIsInstance(message,str)
		self.assertTrue(len(message))
		self.assertFalse("*" in message)




	def test_byte_scan_corrupted_string(self):

		with open(self.corrupted_file) as F:

			broken,message = byte_scan(F.read())
			self.assertTrue(broken)
			self.assertIsInstance(message,str)
			self.assertTrue(len(message))
			self.assertTrue("*" in message)

	def test_byte_scan_valid_string(self):

		with open(self.KA60) as F:

			broken,message = byte_scan(F.read())
			self.assertFalse(broken)
			self.assertIsInstance(message,str)
			self.assertTrue(len(message))
			self.assertFalse("*" in message)

	def test_byte_scan_empty_string(self):

		with open(self.empty_file) as F:

			broken,message = byte_scan(F.read())
			self.assertFalse(broken)
			self.assertIsInstance(message,str)
			self.assertFalse(len(message))
			self.assertFalse("*" in message)

	def test_byte_scan_spaces_string(self):

		with open(self.spaces_file) as F:

			broken,message = byte_scan(F.read())
			self.assertFalse(broken)
			self.assertIsInstance(message,str)
			self.assertTrue(len(message))
			self.assertFalse("*" in message)




	def test_byte_scan_corrupted_bytes(self):

		with open(self.corrupted_file, "rb") as F:

			broken,message = byte_scan(F.read())
			self.assertTrue(broken)
			self.assertIsInstance(message,str)
			self.assertTrue(len(message))
			self.assertTrue("*" in message)

	def test_byte_scan_valid_bytes(self):

		with open(self.KA60, "rb") as F:

			broken,message = byte_scan(F.read())
			self.assertFalse(broken)
			self.assertIsInstance(message,str)
			self.assertTrue(len(message))
			self.assertFalse("*" in message)

	def test_byte_scan_empty_bytes(self):

		with open(self.empty_file, "rb") as F:

			broken,message = byte_scan(F.read())
			self.assertFalse(broken)
			self.assertIsInstance(message,str)
			self.assertFalse(len(message))
			self.assertFalse("*" in message)

	def test_byte_scan_spaces_bytes(self):

		with open(self.spaces_file, "rb") as F:

			broken,message = byte_scan(F.read())
			self.assertFalse(broken)
			self.assertIsInstance(message,str)
			self.assertTrue(len(message))
			self.assertFalse("*" in message)


	def test_byte_scan_others(self):

		for other in (

			int(), float(), bool(), None, ..., print, unittest,
			[ "file" ],( "file", ),{ "file" },{ "path": "file" }
		):
			broken,message = byte_scan(other)
			self.assertTrue(broken)
			self.assertIsInstance(message,str)
			self.assertFalse(len(message))








	def test_sanit_corrupted_file(self):

		scan = sanit_state(self.corrupted_file)
		self.assertIsInstance(scan, dict)
		self.assertEqual(len(scan),2)
		self.assertEqual(scan.get("sanit"),0)
		self.assertIsInstance(scan.get("message"),str)
		self.assertTrue(len(scan.get("message")))


	def test_sanit_corrupted_string(self):

		with open(self.corrupted_file) as F:

			scan = sanit_state(F.read())
			self.assertIsInstance(scan, dict)
			self.assertEqual(len(scan),2)
			self.assertEqual(scan.get("sanit"),0)
			self.assertIsInstance(scan.get("message"),str)
			self.assertTrue(len(scan.get("message")))


	def test_sanit_corrupted_bytes(self):

		with open(self.corrupted_file, "rb") as F:

			scan = sanit_state(F.read())
			self.assertIsInstance(scan, dict)
			self.assertEqual(len(scan),2)
			self.assertEqual(scan.get("sanit"),0)
			self.assertIsInstance(scan.get("message"),str)
			self.assertTrue(len(scan.get("message")))


	def test_sanit_empty_file(self):

		self.assertEqual(

			sanit_state(self.empty_file),
			{
				"raw_lines":	[ "" ],
				"air_lines":	[],
				"chunks":		set(),
				"symbols":		set(),
				"sanit":		0,
			}
		)


	def test_sanit_empty_string(self):

		with open(self.empty_file) as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines":	[ "" ],
					"air_lines":	[],
					"chunks":		set(),
					"symbols":		set(),
					"sanit":		0,
				}
			)


	def test_sanit_empty_bytes(self):

		with open(self.empty_file, "rb") as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines":	[ "" ],
					"air_lines":	[],
					"chunks":		set(),
					"symbols":		set(),
					"sanit":		0,
				}
			)


	def test_sanit_spaces_file(self):

		self.assertEqual(

			sanit_state(self.spaces_file),
			{
				"raw_lines":	[ "","\t","     "," \t \t","","" ],
				"air_lines":	[],
				"chunks":		set(),
				"symbols":		set(),
				"sanit":		0,
			}
		)


	def test_sanit_spaces_string(self):

		with open(self.spaces_file) as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines":	[ "","\t","     "," \t \t","","" ],
					"air_lines":	[],
					"chunks":		set(),
					"symbols":		set(),
					"sanit":		0,
				}
			)


	def test_sanit_spaces_bytes(self):

		with open(self.spaces_file, "rb") as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines":	[ "","\t","     "," \t \t","","" ],
					"air_lines":	[],
					"chunks":		set(),
					"symbols":		set(),
					"sanit":		0,
				}
			)


	def test_sanit_JA94_file(self):

		self.assertEqual(

			sanit_state(self.JA94),
			{
				"raw_lines": [

					"ZCZC JA94",
					"151930 UTC FEB",
					"CANCEL GERMAN NAV WARN 079/19",
					"NNNN",
					""
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


	def test_sanit_JA94_text(self):

		with open(self.JA94) as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"ZCZC JA94",
						"151930 UTC FEB",
						"CANCEL GERMAN NAV WARN 079/19",
						"NNNN",
						""
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


	def test_sanit_JA94_bytes(self):

		with open(self.JA94, "rb") as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"ZCZC JA94",
						"151930 UTC FEB",
						"CANCEL GERMAN NAV WARN 079/19",
						"NNNN",
						""
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


	def test_sanit_BA33_file(self):

		self.assertEqual(

			sanit_state(self.BA33),
			{
				"raw_lines": [

					"",
					"ZCZC BA33",
					"181136 UTC MAR 19",
					"NORWEGIAN NAV. WARNING 198/2019",
					"CHART 73",
					"AREA LOFOTEN INNERSIDEN",
					"FESTVAAG LIGHT 68-10.2N 014-12.6E IS UNLIT.",
					"NNNN",
					""
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


	def test_sanit_BA33_string(self):

		with open(self.BA33) as F:
		
			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"",
						"ZCZC BA33",
						"181136 UTC MAR 19",
						"NORWEGIAN NAV. WARNING 198/2019",
						"CHART 73",
						"AREA LOFOTEN INNERSIDEN",
						"FESTVAAG LIGHT 68-10.2N 014-12.6E IS UNLIT.",
						"NNNN",
						""
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


	def test_sanit_BA33_bytes(self):

		with open(self.BA33, "rb") as F:
		
			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"",
						"ZCZC BA33",
						"181136 UTC MAR 19",
						"NORWEGIAN NAV. WARNING 198/2019",
						"CHART 73",
						"AREA LOFOTEN INNERSIDEN",
						"FESTVAAG LIGHT 68-10.2N 014-12.6E IS UNLIT.",
						"NNNN",
						""
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


	def test_sanit_NA22_file(self):

		self.assertEqual(

			sanit_state(self.NA22),
			{
				"raw_lines": [

					"ZCZC NA22",
					"110905 UTC MAR 19",
					"NORWEGIAN NAV. WARNING 184/2019",
					"CHART  N36",
					"AREA GRIP",
					"HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE",
					"NNNN",
					""
				],
				"air_lines": [

					[ "ZCZC", "NA22" ],
					[ "110905", "UTC", "MAR", "19" ],
					[ "NORWEGIAN", "NAV.", "WARNING", "184/2019" ],
					[ "CHART", "N36" ],
					[ "AREA", "GRIP" ],
					[ "HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE" ],
					[ "NNNN" ]
				],
				"chunks": set((

					"ZCZC",
					"NA22",
					"UTC",
					"110905",
					"MAR",
					"19",
					"NORWEGIAN",
					"NAV.",
					"WARNING",
					"184/2019",
					"CHART",
					"N36",
					"AREA",
					"GRIP",
					"HILBAAAN",
					"RACON",
					"63-12.0N",
					"007-43.8E",
					"IS",
					"INOPERATIVE",
					"NNNN",
				)),
				"symbols":	set("-./0123456789ABCEGHILMNOPRSTUVWZ"),
				"sanit":	3,
			}
		)


	def test_sanit_NA22_string(self):

		with open(self.NA22) as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"ZCZC NA22",
						"110905 UTC MAR 19",
						"NORWEGIAN NAV. WARNING 184/2019",
						"CHART  N36",
						"AREA GRIP",
						"HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE",
						"NNNN",
						""
					],
					"air_lines": [

						[ "ZCZC", "NA22" ],
						[ "110905", "UTC", "MAR", "19" ],
						[ "NORWEGIAN", "NAV.", "WARNING", "184/2019" ],
						[ "CHART", "N36" ],
						[ "AREA", "GRIP" ],
						[ "HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE" ],
						[ "NNNN" ]
					],
					"chunks": set((

						"ZCZC",
						"NA22",
						"UTC",
						"110905",
						"MAR",
						"19",
						"NORWEGIAN",
						"NAV.",
						"WARNING",
						"184/2019",
						"CHART",
						"N36",
						"AREA",
						"GRIP",
						"HILBAAAN",
						"RACON",
						"63-12.0N",
						"007-43.8E",
						"IS",
						"INOPERATIVE",
						"NNNN",
					)),
					"symbols":	set("-./0123456789ABCEGHILMNOPRSTUVWZ"),
					"sanit":	3,
				}
			)


	def test_sanit_NA22_bytes(self):

		with open(self.NA22, "rb") as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"ZCZC NA22",
						"110905 UTC MAR 19",
						"NORWEGIAN NAV. WARNING 184/2019",
						"CHART  N36",
						"AREA GRIP",
						"HILBAAAN RACON 63-12.0N 007-43.8E IS INOPERATIVE",
						"NNNN",
						""
					],
					"air_lines": [

						[ "ZCZC", "NA22" ],
						[ "110905", "UTC", "MAR", "19" ],
						[ "NORWEGIAN", "NAV.", "WARNING", "184/2019" ],
						[ "CHART", "N36" ],
						[ "AREA", "GRIP" ],
						[ "HILBAAAN", "RACON", "63-12.0N", "007-43.8E", "IS", "INOPERATIVE" ],
						[ "NNNN" ]
					],
					"chunks": set((

						"ZCZC",
						"NA22",
						"UTC",
						"110905",
						"MAR",
						"19",
						"NORWEGIAN",
						"NAV.",
						"WARNING",
						"184/2019",
						"CHART",
						"N36",
						"AREA",
						"GRIP",
						"HILBAAAN",
						"RACON",
						"63-12.0N",
						"007-43.8E",
						"IS",
						"INOPERATIVE",
						"NNNN",
					)),
					"symbols":	set("-./0123456789ABCEGHILMNOPRSTUVWZ"),
					"sanit":	3,
				}
			)


	def test_sanit_IA76_file(self):

		self.assertEqual(

			sanit_state(self.IA76),
			{
				"raw_lines": [

					"ZCZC IA76",
					"210800 UTC JAN",
					"BALTIC ICE INFORMATION",
					"VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL 'ICEINFO'",
					"ON VHF OR",
					"PHONE +46 (0)10 492 76 00 AS FOLLOWS:",
					"WHEN PASSING LAT N60 ON VHF CH78.",
					"ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.",
					"DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.",
					"FOR INFORMATION ON RESTRICTIONS GO TO 'BALTICE.ORG'",
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
					"MOORED.",
					"BEFORE",
					"BOUND",
					"LAT",
					"ICE",
					"IA76",
					"PASSING",
					"LATEST",
					"JAN",
					"CH78.",
					"CH16",
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


	def test_sanit_IA76_string(self):

		with open(self.IA76) as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"ZCZC IA76",
						"210800 UTC JAN",
						"BALTIC ICE INFORMATION",
						"VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL 'ICEINFO'",
						"ON VHF OR",
						"PHONE +46 (0)10 492 76 00 AS FOLLOWS:",
						"WHEN PASSING LAT N60 ON VHF CH78.",
						"ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.",
						"DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.",
						"FOR INFORMATION ON RESTRICTIONS GO TO 'BALTICE.ORG'",
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
						"MOORED.",
						"BEFORE",
						"BOUND",
						"LAT",
						"ICE",
						"IA76",
						"PASSING",
						"LATEST",
						"JAN",
						"CH78.",
						"CH16",
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


	def test_sanit_IA76_bytes(self):

		with open(self.IA76, "rb") as F:

			self.assertEqual(

				sanit_state(F.read()),
				{
					"raw_lines": [

						"ZCZC IA76",
						"210800 UTC JAN",
						"BALTIC ICE INFORMATION",
						"VESSELS BOUND FOR PORTS SUBJECT TO TRAFFIC RESTRICTIONS SHALL CALL 'ICEINFO'",
						"ON VHF OR",
						"PHONE +46 (0)10 492 76 00 AS FOLLOWS:",
						"WHEN PASSING LAT N60 ON VHF CH78.",
						"ARRIVAL REPORT ON VHF CH16 WHEN THE SHIP IS WELL MOORED.",
						"DEPARTURE REPORT ON VHF CH16 LATEST 6 HOURS BEFORE DEPARTURE.",
						"FOR INFORMATION ON RESTRICTIONS GO TO 'BALTICE.ORG'",
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
						"MOORED.",
						"BEFORE",
						"BOUND",
						"LAT",
						"ICE",
						"IA76",
						"PASSING",
						"LATEST",
						"JAN",
						"CH78.",
						"CH16",
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








if __name__ == "__main__" : unittest.main(verbosity=2)







