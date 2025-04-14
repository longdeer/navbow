import	os
import	unittest
import	NavtexBoWAnalyzer
from	NavtexBoWAnalyzer.scanner import byte_scan
from	NavtexBoWAnalyzer.scanner import sanit_scan








class SannerCase(unittest.TestCase):

	wd = os.path.join(NavtexBoWAnalyzer.__path__[0], "tests")
	# List of invalid messages:
	# WZ29
	# List of valid messages:
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
	# OL66


	def test_byte_scan_invalid(self):	self.assertIsNotNone(byte_scan(os.path.join(self.wd, "WZ29")))
	def test_byte_scan_valid(self):		self.assertIsNone(byte_scan(os.path.join(self.wd, "KA60")))
	def test_statescan_JA94(self):

		self.assertEqual(

			sanit_scan(os.path.join(self.wd, "JA94")),
			{
				"raw_lines": [

					"ZCZC JA94",
					"151930 UTC FEB",
					"CANCEL GERMAN NAV WARN 079/19",
					"NNNN",
				],
				"air_lines": [

					"ZCZC JA94",
					"151930 UTC FEB",
					"CANCEL GERMAN NAV WARN 079/19",
					"NNNN",
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


	def test_statescan_BA33(self):

		self.assertEqual(

			sanit_scan(os.path.join(self.wd, "BA33")),
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

					"ZCZC BA33",
					"181136 UTC MAR 19",
					"NORWEGIAN NAV. WARNING 198/2019",
					"CHART 73",
					"AREA LOFOTEN INNERSIDEN",
					"FESTVAAG LIGHT 68-10.2N 014-12.6E IS UNLIT.",
					"NNNN",
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


	def test_statescan_NA22(self):

		self.assertEqual(

			sanit_scan(os.path.join(self.wd, "IA76")),
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


	def test_statescan_IA76(self):

		self.assertEqual(

			sanit_scan(os.path.join(self.wd, "IA76")),
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







