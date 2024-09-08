import	re
import	unittest
from	datetime		import datetime
from	string			import ascii_letters
from	string			import ascii_uppercase
from	navtex_analyzer	import Navanalyzer








class Init(unittest.TestCase):

	valid_stations = ( char for char in ascii_letters if char not in "YyZz" )
	invalid_stations = "Y", "y", "Z", "z", "YyZz", 42, None, True, bool, type, ..., NotImplemented,
	valid_categories = (

		"A",
		"a",
		"AA",
		"Aa",
		"aA",
		"ABC",
		"ABc",
		"Abc",
		[ "A", "BC", "D" ],
		[ "A", "B", "C", "D" ],
		[ "ABCD" ],
		[ "AB", "CD" ],
	)
	invalid_categories = (

		"1",
		"A1",
		"BB1",
		"BB1111",
		"BBBBBBBBBCCCCCCCCDDDDDDDDD1",
		[ "A1" ],
		[ "A", "1" ],
		[ "A", 1 ],
		[ "B", "BBBBBBB", "BCCCCCCCCDDDDDDDDD1", ]
	)


	def setUp(self):
		self.test_case = Navanalyzer("K")


	def test_valid_stations(self):

		for station in self.valid_stations:
			with self.subTest(station=station):

				self.assertIsInstance(Navanalyzer(station=station), Navanalyzer)


	def test_invalid_station(self):

		for station in self.invalid_stations:
			with self.subTest(station=station):

				self.assertRaisesRegex(

					AssertionError,
					"Provided station identificator is invalid for NAVTEX",
					Navanalyzer,
					station=station
				)


	def test_valid_categories(self):

		for categories_case in self.valid_categories:
			with self.subTest(station="K", categories=categories_case):

				self.assertIsInstance(Navanalyzer(station="K", categories=categories_case), Navanalyzer)


	def test_invalid_categories(self):

		for categories_case in self.invalid_categories:
			with self.subTest(category=categories_case):

				self.assertRaisesRegex(

					AssertionError,
					"Provided messages categories are invalid for NAVTEX",
					Navanalyzer,
					station="K", categories=categories_case
				)


	def test_nocategories_init(self):

		self.assertEqual(self.test_case._station, "K")
		self.assertEqual(self.test_case._categories, ascii_uppercase)


	def test_header_pattern(self):
		self.assertIsInstance(Navanalyzer("K").NAVTEX_MESSAGE_HEADER, re.Pattern)
















class Members(unittest.TestCase):

	def setUp(self) : self.test_case = Navanalyzer("K")


	def test_lines_processing(self):

		one				= "1 2 3\n4 5 6\n7 8 9"
		first			= self.test_case.split_lines(one)
		proper_first	= self.test_case.get_proper_lines(first)

		self.assertEqual(first, [ "1 2 3","4 5 6","7 8 9" ])
		self.assertEqual(proper_first, [ "1 2 3","4 5 6","7 8 9" ])


		two				= "1 2 3\n4 5 6\n7 8 9\n"
		second			= self.test_case.split_lines(two)
		proper_second	= self.test_case.get_proper_lines(second)

		self.assertEqual(second, [ "1 2 3","4 5 6","7 8 9" ])
		self.assertEqual(proper_second, [ "1 2 3","4 5 6","7 8 9" ])


		three			= "1  2 3\n 4 5 6\n\t7 8 9"
		third			= self.test_case.split_lines(three)
		proper_third	= self.test_case.get_proper_lines(third)

		self.assertEqual(third, [ "1  2 3"," 4 5 6","\t7 8 9" ])
		self.assertEqual(proper_third, [ "1 2 3","4 5 6","7 8 9" ])


		four			= "1  2 3\n\n 4 5 6\n\n\t7 8 9"
		fourth			= self.test_case.split_lines(four)
		proper_fourth	= self.test_case.get_proper_lines(fourth)

		self.assertEqual(fourth, [ "1  2 3"," 4 5 6","\t7 8 9" ])
		self.assertEqual(proper_fourth, [ "1 2 3","4 5 6","7 8 9" ])




	def tests_CDT_processing(self):

		original = self.test_case.NAVTEX_MESSAGE_CDT
		self.test_case.NAVTEX_MESSAGE_CDT = re.compile(
			r"(?P<msg_day>[^\s]+) (?P<msg_time>[^\s]+) (?P<msg_month>[^\s]+) (?P<msg_year>[^\s]+)?"
		)

		one		= [ "2 0420 FEB 21" ]
		first	= self.test_case.process_CDT(one)

		self.assertIsInstance(first,tuple)
		self.assertEqual(len(first),2)
		self.assertIn(f"Incorrect date format in CDT line \"{one[0]}\"", first)
		self.assertIn(f"CDT line \"{one[0]}\" doesn't match current date", first)


		two		= [ "23 420 FEB 21" ]
		second	= self.test_case.process_CDT(two)

		self.assertIsInstance(second,tuple)
		self.assertEqual(len(second),2)
		self.assertIn(f"Incorrect time format in CDT line \"{two[0]}\"", second)
		self.assertIn(f"CDT line \"{two[0]}\" doesn't match current date", second)


		three	= [ "23 0420 FE 21" ]
		third	= self.test_case.process_CDT(three)

		self.assertIsInstance(third,tuple)
		self.assertEqual(len(third),2)
		self.assertIn(f"Incorrect date format in CDT line \"{three[0]}\"", third)
		self.assertIn(f"CDT line \"{three[0]}\" doesn't match current date", third)


		four	= [ "23 0420 FEB 2" ]
		fourth	= self.test_case.process_CDT(four)
		self.assertIsInstance(fourth,tuple)
		self.assertEqual(len(fourth),2)
		self.assertIn(f"Incorrect year format in CDT line \"{four[0]}\"", fourth)
		self.assertIn(f"CDT line \"{four[0]}\" doesn't match current date", fourth)


		five	= [ "DD HHMM MMM YY" ]
		fifth	= self.test_case.process_CDT(five)
		self.assertIsInstance(fifth,tuple)
		self.assertEqual(len(fifth),4)
		self.assertIn(f"Incorrect date format in CDT line \"{five[0]}\"", fifth)
		self.assertIn(f"Incorrect time format in CDT line \"{five[0]}\"", fifth)
		self.assertIn(f"Incorrect year format in CDT line \"{five[0]}\"", fifth)
		self.assertIn(f"CDT line \"{five[0]}\" doesn't match current date", fifth)


		self.test_case.NAVTEX_MESSAGE_CDT = original


		today	= datetime.now().strftime



		one		= [ f"020420 UTC FEB 21" ]
		first	= self.test_case.process_CDT(one)

		self.assertIsInstance(first,tuple)
		self.assertIn(f"CDT line \"{one[0]}\" doesn't match current date", first)


		two		= [ f"{today('%d')}{today('%H%M')} UTC {today('%b').upper()} {today('%Y')[2:]}" ]
		second	= self.test_case.process_CDT(two)

		self.assertIsNone(second)


		three	= [ today("%d/%m/%Y") ]
		third	= self.test_case.process_CDT(three)


		self.assertIsInstance(third,tuple)
		self.assertEqual(len(third),1)
		self.assertIn("No line looks like message creation timestamp", third)




	def test_invalid_BoW_invoke(self):

		for BoW in ( list(), tuple(), set(), 1, .1, False, True, None, ... ):
			with self.subTest(BoW=BoW):
				self.assertRaisesRegex(

					AssertionError,
					"Provided bag of NAVTEX words is invalid",
					self.test_case,
					message="ZCZC\nNNNN", BoW=BoW
				)




	def test_BoW_smooth_update(self):

		self.test_case.process_body(

			[
				"OOH EEH",
				"OOH AH AH",
				"TING TANG",
				"WALA WALA BING BANG"
			],
			{}
		)

		self.assertEqual(len(self.test_case.NEW_TEXT_WORDS), 8)

		self.assertIn("OOH",	self.test_case.NEW_TEXT_WORDS)
		self.assertIn("EEH",	self.test_case.NEW_TEXT_WORDS)
		self.assertIn("AH",		self.test_case.NEW_TEXT_WORDS)
		self.assertIn("TING",	self.test_case.NEW_TEXT_WORDS)
		self.assertIn("TANG",	self.test_case.NEW_TEXT_WORDS)
		self.assertIn("WALA",	self.test_case.NEW_TEXT_WORDS)
		self.assertIn("BING",	self.test_case.NEW_TEXT_WORDS)
		self.assertIn("BANG",	self.test_case.NEW_TEXT_WORDS)

		self.assertEqual(self.test_case.update_BoW({}), 8)




	def test_BoW_fraught_update(self):

		for BoW in ( list(), tuple(), set(), 1, .1, False, True, None, ... ):
			with self.subTest(BoW=BoW):
				self.assertRaisesRegex(

					AssertionError,
					"Provided bag of NAVTEX words is invalid",
					self.test_case,
					message="ZCZC\nNNNN", BoW=BoW
				)

		result = self.test_case.process_body(

			# first OOH - second O rus;
			# EEH - first E rus;
			# second AH - A rus;
			# TING - N rus;
			# first WALA - second A rus;
			# BANG - A rus.
			[
				"OОH ЕEH",
				"OOH AH АH",
				"TIИG TANG",
				"WALА WALA BING BАNG"
			],
			{}
		)

		self.assertEqual(len(self.test_case.NEW_TEXT_WORDS), 5)
		self.assertNotIn("OОH", self.test_case.NEW_TEXT_WORDS)		# second O rus
		self.assertNotIn("ЕEH", self.test_case.NEW_TEXT_WORDS)		# first E rus
		self.assertNotIn("АH", self.test_case.NEW_TEXT_WORDS)		# A rus
		self.assertNotIn("TIИG", self.test_case.NEW_TEXT_WORDS)		# N is rus
		self.assertNotIn("WALА", self.test_case.NEW_TEXT_WORDS)		# second A rus
		self.assertNotIn("BАNG", self.test_case.NEW_TEXT_WORDS)		# A rus
		self.assertIn("OOH", self.test_case.NEW_TEXT_WORDS)
		self.assertIn("AH", self.test_case.NEW_TEXT_WORDS)
		self.assertIn("TANG", self.test_case.NEW_TEXT_WORDS)
		self.assertIn("WALA", self.test_case.NEW_TEXT_WORDS)
		self.assertIn("BING", self.test_case.NEW_TEXT_WORDS)

		self.assertEqual(self.test_case.update_BoW({}), 5)

		self.assertIn(( 40,2,"OОH", "Not handled \"OОH\"" ),	result)
		self.assertIn(( 40,2,"ЕEH", "Not handled \"ЕEH\"" ),	result)
		self.assertIn(( 30,3,"OOH", "Unknown word \"OOH\"" ),	result)
		self.assertIn(( 30,3,"AH", "Unknown word \"AH\"" ),		result)
		self.assertIn(( 40,3,"АH", "Not handled \"АH\"" ),		result)
		self.assertIn(( 40,4,"TIИG", "Not handled \"TIИG\"" ),	result)
		self.assertIn(( 30,4,"TANG", "Unknown word \"TANG\"" ),	result)
		self.assertIn(( 40,5,"WALА", "Not handled \"WALА\"" ),	result)
		self.assertIn(( 30,5,"WALA", "Unknown word \"WALA\"" ),	result)
		self.assertIn(( 30,5,"BING", "Unknown word \"BING\"" ),	result)
		self.assertIn(( 40,5,"BАNG", "Not handled \"BАNG\"" ),	result)
















class Patterns(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.test_case = Navanalyzer("K")
		cls.valid_headers = "ZCZC KA01", "ZCZC KE15", "ZCZC KB00", "ZCZC KD00",
		cls.invalid_headers = "ZCZC KA1", "ZCZC K15", "ZCZC KB01", "ZCZC KD10", "ZCZ KD00", "KD10",
		cls.months = "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC",
		cls.numerical_patterns = {

			"num_int":		( "0", "69", "100500" ),
			"num_int_unit":	( "271500UTC", "518KHZ", "5M" ),
			"num_dec":		( "4.20", "0.5", "3,50", "0,0" ),
			"num_dec_unit":	( "2187.5KHZ", "1,5KM" ),
			"num_date":		( "31/01/2020", "20.04.2012", "11-11-11", "07\\25\\1998" ),
			"num_time":		( "21:00", "21:00UTC", "4:20", "4:20UTC" ),
			"num_range":	( "1-2", "1,5-2,0", "4.20-69", "1999-0,5" ),
			"num_phone":	( "+78152422182", "+7(8152)422182" ),
			"num_item":		(
			
				"154/21", "2/GW", "1/J8HC7", "27/00Z",
				"NO.13", "NO13", "NO-13", "NO:13", "NR.13", "NR13", "NR-13", "NR:13",
				"NO.13/1", "NO13/1", "NO-13/1", "NO:13/1", "NR.13/1", "NR13/1", "NR-13/1", "NR:13/1",
			),
		}
		cls.coordinatal_patterns = {

			"cord_point": (

				"74-14.06N",
				"033-20.00E",
				"69-20.7N",
				"53-52N",
				"006-22E",
				"21.4N",
				"151.1W",
				"33.0N",
			)
		}
		cls.alphabetic_patterns = {

			"alnum_symb_chars": (

				"UTC",
				"2/GW",
				"NORTH-EASTERN",
				"1138(INT",
				"24-HR",
				"-",
			),
			"alnum_abbr_chars": (

				"Y.20S",
				"NAV.WARNING",
				"Q.G.",
				"Q.G",
			)
		}
		# more than 3 brackets sounds ridiculous for NAVTEX...
		cls.templates = (

			"%s",
			"(%s", "((%s", "(((%s",
			"(%s)", "(%s))", "(%s)))",
			"((%s)",
			"(((%s)",
			"%s)", "%s))", "%s)))",
			"%s'",
			"%s')", "%s'))", "%s')))",
			"%s)'", "%s))'", "%s)))'",
			"%s\"",
			"%s\")", "%s\"))", "%s\")))",
			"%s)\"", "%s))\"", "%s)))\"",

			"%s.",
			"(%s.", "((%s.", "(((%s.",
			"(%s.)", "(%s.))", "(%s.)))",
			"((%s.)",
			"(((%s.)",
			"%s).", "%s)).", "%s))).",
			"%s.)", "%s.))", "%s.)))",
			"%s.'",
			"%s.')", "%s.'))", "%s.')))",
			"%s.)'", "%s.))'", "%s.)))'",
			"%s.\")", "%s.\"))", "%s.\")))",
			"%s.)\"", "%s.))\"", "%s.)))\"",

			"%s;",
			"%s);", "%s));", "%s)));",

			"%s:",
			"%s):", "%s)):", "%s))):",

			"%s,",
			"(%s,", "((%s,", "(((%s,",
			"%s),", "%s)),", "%s))),",



			"(%s", "'%s", "\"%s",
			"(%s)", "(%s.", "(%s,", "(%s:", "(%s;",
			"((%s)", "((%s.", "((%s,", "((%s:", "((%s;",
			"(((%s)", "(((%s.", "(((%s,", "(((%s:", "(((%s;",

			"'%s.", "'%s,", "'%s:", "'%s;", "'%s'",
			"\"%s.", "\"%s,", "\"%s:", "\"%s;", "\"%s\"",

			"'%s'.", "'%s',", "'%s':", "'%s';",
			"'%s').", "'%s'),", "'%s'):", "'%s');",
			"'%s')).", "'%s')),", "'%s')):", "'%s'));",
			"'%s'))).", "'%s'))),", "'%s'))):", "'%s')));",
			"('%s'.", "('%s',", "('%s':", "('%s';",
			"('%s').", "('%s'),", "('%s'):", "('%s');",
			"('%s')).", "('%s')),", "('%s')):", "('%s'));",
			"('%s'))).", "('%s'))),", "('%s'))):", "('%s')));",

			"\"%s\".", "\"%s\",", "\"%s\":", "\"%s\";",
			"\"%s\").", "\"%s\"),", "\"%s\"):", "\"%s\");",
			"\"%s\")).", "\"%s\")),", "\"%s\")):", "\"%s\"));",
			"\"%s\"))).", "\"%s\"))),", "\"%s\"))):", "\"%s\")));",
			"(\"%s\".", "(\"%s\",", "(\"%s\":", "(\"%s\";",
			"(\"%s\").", "(\"%s\"),", "(\"%s\"):", "(\"%s\");",
			"(\"%s\")).", "(\"%s\")),", "(\"%s\")):", "(\"%s\"));",
			"(\"%s\"))).", "(\"%s\"))),", "(\"%s\"))):", "(\"%s\")));",
		)


	def test_header_valid_pattern(self):

		for header in self.valid_headers:
			with self.subTest(header=header):
				self.assertTrue(self.test_case.NAVTEX_MESSAGE_HEADER.fullmatch(header))




	def test_header_invalid_pattern(self):

		for header in self.invalid_headers:
			with self.subTest(header=header):
				self.assertFalse(self.test_case.NAVTEX_MESSAGE_HEADER.fullmatch(header))




	def test_numerical_matching(self):

		for group,patterns in self.numerical_patterns.items():
			for pattern in patterns:
				for template in self.templates:
					current = template%pattern

					with self.subTest(pattern=current):

						match = self.test_case.TEXT_NUMERICAL.fullmatch(current)
						self.assertTrue(match)
						self.assertIsNotNone(match.group(group))




	def test_coordinatal_matching(self):

		for group,patterns in self.coordinatal_patterns.items():
			for pattern in patterns:
				for template in self.templates:
					current = template%pattern

					with self.subTest(pattern=current):

						match = self.test_case.TEXT_COORDINATAL.fullmatch(current)
						self.assertTrue(match)
						self.assertIsNotNone(match.group(group))




	def test_alphabetic_matching(self):

		for group,patterns in self.alphabetic_patterns.items():
			for pattern in patterns:
				for template in self.templates:
					current = template%pattern

					with self.subTest(pattern=current):

						match = self.test_case.TEXT_ALPHABETIC.fullmatch(current)
						self.assertTrue(match)
						self.assertIsNotNone(match.group(group))
						# No handling for various amount of dots, that could happen. So the easiest and
						# wisest way is to strip all dots, whether it's a part of abbreviation or just a
						# punctuation.
						self.assertEqual(match.group(group).rstrip("."), pattern.rstrip("."))




	def test_CDT_pattern(self):

		for m in self.months:

			p1	= f"191833 UTC {m}"
			p2	= f"191833 UTC {m} 07"

			with self.subTest(pattern=p1):
				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p1))

			with self.subTest(pattern=p2):
				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p2))


		for _d in range(32):

			d	= str(_d).zfill(2)
			p1	= f"{d}2048 UTC OCT"
			p2	= f"{d}2048 UTC OCT 11"

			with self.subTest(pattern=p1):
				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p1))

			with self.subTest(pattern=p2):
				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p2))


		for _HM in range(2400):

			HM	= str(_HM).zfill(4)
			p1	= f"01{HM} UTC JAN"
			p2	= f"01{HM} UTC JAN 22"

			with self.subTest(pattern=p1):
				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p1))

			with self.subTest(pattern=p2):
				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p2))


		for _Y in range(39):

			Y	= str(_Y).zfill(2)
			p1	= f"312359 UTC DEC"
			p2	= f"312359 UTC DEC {Y}"


			with self.subTest(d=d, HM=HM, m=m, Y=Y):

				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p1))
				self.assertIsNotNone(self.test_case.NAVTEX_MESSAGE_CDT.fullmatch(p2))

















class Message1(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.message1 = str(

			"\n"
			"ZCZC KB00\n"
			"051115 UTC MAR\n"
			"GALE WARNING MURMANSK NR85\n"
			"ON MURMAN COAST 01 MAR 17-21 UTC\n"
			"WIND NORTH-EASTERN NORTHERN GUST\n"
			"15-20 M/S\n"
			"NNNN\n"
		)
		cls.analyzer = Navanalyzer("K")
		cls.BoW = { "UTC": 1 }
		cls.analysis = cls.analyzer(cls.message1, cls.BoW)




	def test_proper_lines(self):

		self.assertIn("proper_lines", self.analysis)
		proper_lines = self.analysis["proper_lines"]
		self.assertIsInstance(proper_lines, list)
		self.assertEqual(len(proper_lines), 7)

		raw_lines = self.message1.split("\n")
		self.assertEqual(len(proper_lines[0]), len(raw_lines[1]))
		self.assertEqual(len(proper_lines[1]), len(raw_lines[2]))
		self.assertEqual(len(proper_lines[2]), len(raw_lines[3]))
		self.assertEqual(len(proper_lines[3]), len(raw_lines[4]))
		self.assertEqual(len(proper_lines[4]), len(raw_lines[5]))
		self.assertEqual(len(proper_lines[5]), len(raw_lines[6]))
		self.assertEqual(len(proper_lines[6]), len(raw_lines[7]))




	def test_proper_message(self):

		self.assertIn("proper_message", self.analysis)
		proper_message = self.analysis["proper_message"]
		self.assertIsInstance(proper_message, str)
		self.assertNotEqual(len(proper_message), len(self.message1))
		self.assertEqual(len(proper_message), 132)




	def test_is_structured(self):

		self.assertIn("is_structured", self.analysis)
		self.assertFalse(self.analysis["is_structured"])




	def test_is_sanitized(self):

		self.assertIn("is_sanitized", self.analysis)
		self.assertFalse(self.analysis["is_sanitized"])




	def test_header_issue(self):

		self.assertIn("header_issue", self.analysis)
		self.assertEqual(self.analysis["header_issue"], None)




	def test_CDT_issues(self):

		self.assertIn("CDT_issues", self.analysis)
		self.assertIn(

			"CDT line \"%s\" doesn't match current date"%(
				self.analysis["proper_lines"][1].rstrip("\n")
			),	self.analysis["CDT_issues"]
		)




	def test_body_issues(self):

		self.assertIn("body_issues", self.analysis)
		body_issues = self.analysis["body_issues"]

		self.assertIn((		10,2,"UTC", "Known word \"UTC\"" ), body_issues)
		self.assertIn((		30,2,"MAR", "Unknown word \"MAR\"" ), body_issues)
		self.assertIn((		30,3,"GALE", "Unknown word \"GALE\"" ), body_issues)
		self.assertIn((		30,3,"WARNING", "Unknown word \"WARNING\"" ), body_issues)
		self.assertIn((		30,3,"MURMANSK", "Unknown word \"MURMANSK\"" ), body_issues)
		self.assertIn((		10,3,"NR85", "Numerical item \"NR85\"" ), body_issues)
		self.assertIn((		30,4,"ON", "Unknown word \"ON\"" ), body_issues)
		self.assertIn((		30,4,"MURMAN", "Unknown word \"MURMAN\"" ), body_issues)
		self.assertIn((		30,4,"COAST", "Unknown word \"COAST\"" ), body_issues)
		self.assertIn((		10,4,"01", "Integer \"01\"" ), body_issues)
		self.assertIn((		30,4,"MAR", "Unknown word \"MAR\"" ), body_issues)
		self.assertIn((		10,4,"17-21", "Range \"17-21\"" ), body_issues)
		self.assertIn((		10,4,"UTC", "Known word \"UTC\"" ), body_issues)
		self.assertIn((		30,5,"WIND", "Unknown word \"WIND\"" ), body_issues)
		self.assertIn((		30,5,"NORTH-EASTERN", "Unknown word \"NORTH-EASTERN\"" ), body_issues)
		self.assertIn((		30,5,"NORTHERN", "Unknown word \"NORTHERN\"" ), body_issues)
		self.assertIn((		30,5,"GUST", "Unknown word \"GUST\"" ), body_issues)
		self.assertIn((		10,6,"15-20", "Range \"15-20\"" ), body_issues)
		self.assertIn((		30,6,"M/S", "Unknown word \"M/S\"" ), body_issues)
		self.assertNotIn((	30,6,"15-20 M/S=", "Excess \"=\"" ), body_issues)




	def test_EOS_issue(self):

		self.assertIn("EOS_issue", self.analysis)
		self.assertEqual(self.analysis["EOS_issue"], None)
















class Message2(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.message2 = str(

			"ZCZC KE35\n"
			"150330 UTC APR\n"
			"MURMANSK WEATHER FORECAST\n"
			"ON MURMAN COAST AT 06 UTC\n"
			"TO 18 UTC 02 APR WIND NORTHERN\n"
			"NORTH-EASTERN GUST 15-18 M/S\n"
			"AT TIMES SNOW VISIBILITY GOOD\n"
			"IN TO SNOW 1-2 KM SEAS 1,5-2,5 M\n"
			"NNNN"
		)
		cls.analyzer = Navanalyzer("K")
		cls.BoW = {

			"UTC":			0,
			"APR":			0,
			"MURMANSK":		0,
			"WEATHER":		0,
			"FORECAST":		0,
			"ON":			0,
			"MURMAN":		0,
			"COAST":		0,
			"AT":			0,
			"TO":			0,
			"WIND":			0,
			"NORTHERN":		0,
			"NORTH-EASTERN":0,
			"GUST":			0,
			"M/S":			0,
			"TIMES":		0,
			"SNOW":			0,
			"VISIBILITY":	0,
			"GOOD":			0,
			"IN":			0,
			"KM":			0,
			"SEAS":			0,
			"M":			0,
		}
		cls.analysis = cls.analyzer(cls.message2, cls.BoW)




	def test_proper_lines(self):

		self.assertIn("proper_lines", self.analysis)
		proper_lines = self.analysis["proper_lines"]
		self.assertIsInstance(proper_lines, list)
		self.assertEqual(len(proper_lines), 9)

		raw_lines = self.message2.split("\n")
		self.assertEqual(len(proper_lines[0]), len(raw_lines[0]))
		self.assertEqual(len(proper_lines[1]), len(raw_lines[1]))
		self.assertEqual(len(proper_lines[2]), len(raw_lines[2]))
		self.assertEqual(len(proper_lines[3]), len(raw_lines[3]))
		self.assertEqual(len(proper_lines[4]), len(raw_lines[4]))
		self.assertEqual(len(proper_lines[5]), len(raw_lines[5]))
		self.assertEqual(len(proper_lines[6]), len(raw_lines[6]))
		self.assertEqual(len(proper_lines[7]), len(raw_lines[7]))
		self.assertEqual(len(proper_lines[8]), len(raw_lines[8]))




	def test_proper_message(self):

		self.assertIn("proper_message", self.analysis)
		proper_message = self.analysis["proper_message"]
		self.assertIsInstance(proper_message, str)
		self.assertEqual(len(proper_message), len(self.message2))




	def test_is_structured(self):

		self.assertIn("is_structured", self.analysis)
		self.assertTrue(self.analysis["is_structured"])




	def test_is_sanitized(self):

		self.assertIn("is_sanitized", self.analysis)
		self.assertFalse(self.analysis["is_sanitized"])




	def test_header_issue(self):

		self.assertIn("header_issue", self.analysis)
		self.assertEqual(self.analysis["header_issue"], None)




	def test_CDT_issues(self):

		self.assertIn("CDT_issues", self.analysis)
		self.assertIn(

			"CDT line \"%s\" doesn't match current date"%(
				self.analysis["proper_lines"][1].rstrip("\n")
			),	self.analysis["CDT_issues"]
		)




	def test_body_issues(self):

		self.assertIn("body_issues", self.analysis)
		body_issues = self.analysis["body_issues"]

		self.assertIn(( 	10,2,"150330", "Integer \"150330\"" ), body_issues)
		self.assertIn(( 	20,2,"UTC", "Pending word \"UTC\"" ), body_issues)
		self.assertIn(( 	20,2,"APR", "Pending word \"APR\"" ), body_issues)
		self.assertIn(( 	20,3,"MURMANSK", "Pending word \"MURMANSK\"" ), body_issues)
		self.assertIn(( 	20,3,"WEATHER", "Pending word \"WEATHER\"" ), body_issues)
		self.assertIn(( 	20,3,"FORECAST", "Pending word \"FORECAST\"" ), body_issues)
		self.assertIn(( 	20,4,"ON", "Pending word \"ON\"" ), body_issues)
		self.assertIn(( 	20,4,"MURMAN", "Pending word \"MURMAN\"" ), body_issues)
		self.assertIn(( 	20,4,"COAST", "Pending word \"COAST\"" ), body_issues)
		self.assertIn(( 	20,4,"AT", "Pending word \"AT\"" ), body_issues)
		self.assertIn(( 	10,4,"06", "Integer \"06\"" ), body_issues)
		self.assertIn(( 	20,4,"UTC", "Pending word \"UTC\"" ), body_issues)
		self.assertIn(( 	20,5,"TO", "Pending word \"TO\"" ), body_issues)
		self.assertIn(( 	10,5,"18", "Integer \"18\"" ), body_issues)
		self.assertIn(( 	20,5,"UTC", "Pending word \"UTC\"" ), body_issues)
		self.assertIn(( 	10,5,"02", "Integer \"02\"" ), body_issues)
		self.assertIn(( 	20,5,"APR", "Pending word \"APR\"" ), body_issues)
		self.assertIn(( 	20,5,"WIND", "Pending word \"WIND\"" ), body_issues)
		self.assertIn(( 	20,5,"NORTHERN", "Pending word \"NORTHERN\"" ), body_issues)
		self.assertIn(( 	20,6,"NORTH-EASTERN", "Pending word \"NORTH-EASTERN\"" ), body_issues)
		self.assertIn(( 	20,6,"GUST", "Pending word \"GUST\"" ), body_issues)
		self.assertIn(( 	10,6,"15-18", "Range \"15-18\"" ), body_issues)
		self.assertIn(( 	20,6,"M/S", "Pending word \"M/S\"" ), body_issues)
		self.assertIn(( 	20,7,"AT", "Pending word \"AT\"" ), body_issues)
		self.assertIn(( 	20,7,"TIMES", "Pending word \"TIMES\"" ), body_issues)
		self.assertIn(( 	20,7,"SNOW", "Pending word \"SNOW\"" ), body_issues)
		self.assertIn(( 	20,7,"VISIBILITY", "Pending word \"VISIBILITY\"" ), body_issues)
		self.assertIn(( 	20,7,"GOOD", "Pending word \"GOOD\"" ), body_issues)
		self.assertIn(( 	20,8,"IN", "Pending word \"IN\"" ), body_issues)
		self.assertIn(( 	20,8,"TO", "Pending word \"TO\"" ), body_issues)
		self.assertIn(( 	20,8,"SNOW", "Pending word \"SNOW\"" ), body_issues)
		self.assertIn(( 	10,8,"1-2", "Range \"1-2\"" ), body_issues)
		self.assertIn(( 	20,8,"KM", "Pending word \"KM\"" ), body_issues)
		self.assertIn(( 	20,8,"SEAS", "Pending word \"SEAS\"" ), body_issues)
		self.assertIn(( 	10,8,"1,5-2,5", "Range \"1,5-2,5\"" ), body_issues)
		self.assertIn(( 	20,8,"M", "Pending word \"M\"" ), body_issues)
		self.assertNotIn((	30,8,"IN TO SNOW 1-2 KM SEAS 1,5-2,5 M=" "Excess \"=\"" ), body_issues)




	def test_EOS_issue(self):

		self.assertIn("EOS_issue", self.analysis)
		self.assertEqual(self.analysis["EOS_issue"], None)
















class Message3(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.message3 = str(

			"ZCZC KA28\n"
			"050530 UTC APR 24\n"
			"COASTAL WARNING MURMANSK 126\n"
			"BARENTS SEA\n"
			"1. ROCKET LAUNCHING 06 TO 14 APR 0930 TO 1100\n"
			"IN AREA DANGEROUS TO NAVIGATION BOUNDED BY\n"
			"74-14.06N 039-11.16E\n"
			"73-31.48N 044-22.53E\n"
			"69-45.00N 038-30.00E\n"
			"70-38.00N 033-20.00E\n"
			"2. CANCEL THIS MESSAGE 141200 APR 24\n"
			"3. CANCEL 117/24 AND THIS PARA=\n"
			"NNNN"
		)
		cls.analyzer = Navanalyzer("K")
		cls.BoW = { "UTC": 1 }
		cls.analysis = cls.analyzer(cls.message3, cls.BoW)




	def test_proper_lines(self):

		self.assertIn("proper_lines", self.analysis)
		proper_lines = self.analysis["proper_lines"]
		self.assertIsInstance(proper_lines, list)
		self.assertEqual(len(proper_lines), 13)

		raw_lines = self.message3.split("\n")
		self.assertEqual(len(proper_lines[0]),	len(raw_lines[0]))
		self.assertEqual(len(proper_lines[1]),	len(raw_lines[1]))
		self.assertEqual(len(proper_lines[2]),	len(raw_lines[2]))
		self.assertEqual(len(proper_lines[3]),	len(raw_lines[3]))
		self.assertEqual(len(proper_lines[4]),	len(raw_lines[4]))
		self.assertEqual(len(proper_lines[5]),	len(raw_lines[5]))
		self.assertEqual(len(proper_lines[6]),	len(raw_lines[6]))
		self.assertEqual(len(proper_lines[7]),	len(raw_lines[7]))
		self.assertEqual(len(proper_lines[8]),	len(raw_lines[8]))
		self.assertEqual(len(proper_lines[9]),	len(raw_lines[9]))
		self.assertEqual(len(proper_lines[10]),	len(raw_lines[10]))
		self.assertEqual(len(proper_lines[11]),	len(raw_lines[11]))
		self.assertEqual(len(proper_lines[12]),	len(raw_lines[12]))




	def test_proper_message(self):

		self.assertIn("proper_message", self.analysis)
		proper_message = self.analysis["proper_message"]
		self.assertIsInstance(proper_message, str)
		self.assertEqual(len(proper_message), len(self.message3))




	def test_is_structured(self):

		self.assertIn("is_structured", self.analysis)
		self.assertTrue(self.analysis["is_structured"])




	def test_is_sanitized(self):

		self.assertIn("is_sanitized", self.analysis)
		self.assertFalse(self.analysis["is_sanitized"])




	def test_header_issue(self):

		self.assertIn("header_issue", self.analysis)
		self.assertEqual(self.analysis["header_issue"], None)




	def test_CDT_issues(self):

		self.assertIn("CDT_issues", self.analysis)
		self.assertIn(

			"CDT line \"%s\" doesn't match current date"%(
				self.analysis["proper_lines"][1].rstrip("\n")
			),	self.analysis["CDT_issues"]
		)




	def test_body_issues(self):

		self.assertIn("body_issues", self.analysis)
		body_issues = self.analysis["body_issues"]

		self.assertIn(( 10,2,"050530", "Integer \"050530\"" ), body_issues)
		self.assertIn(( 10,2,"24", "Integer \"24\"" ), body_issues)
		self.assertIn(( 10,3,"126", "Integer \"126\"" ), body_issues)
		self.assertIn(( 10,5,"1", "Integer \"1\"" ), body_issues)
		self.assertIn(( 10,5,"06", "Integer \"06\"" ), body_issues)
		self.assertIn(( 10,5,"14", "Integer \"14\"" ), body_issues)
		self.assertIn(( 10,5,"0930", "Integer \"0930\"" ), body_issues)
		self.assertIn(( 10,5,"1100", "Integer \"1100\"" ), body_issues)
		self.assertIn(( 10,7,"74-14.06N", "Coordinatal point \"74-14.06N\"" ), body_issues)
		self.assertIn(( 10,7,"039-11.16E", "Coordinatal point \"039-11.16E\"" ), body_issues)
		self.assertIn(( 10,8,"73-31.48N", "Coordinatal point \"73-31.48N\"" ), body_issues)
		self.assertIn(( 10,8,"044-22.53E", "Coordinatal point \"044-22.53E\"" ), body_issues)
		self.assertIn(( 10,9,"69-45.00N", "Coordinatal point \"69-45.00N\"" ), body_issues)
		self.assertIn(( 10,9,"038-30.00E", "Coordinatal point \"038-30.00E\"" ), body_issues)
		self.assertIn(( 10,10,"70-38.00N", "Coordinatal point \"70-38.00N\"" ), body_issues)
		self.assertIn(( 10,10,"033-20.00E", "Coordinatal point \"033-20.00E\"" ), body_issues)
		self.assertIn(( 10,11,"2", "Integer \"2\"" ), body_issues)
		self.assertIn(( 10,11,"141200", "Integer \"141200\"" ), body_issues)
		self.assertIn(( 10,11,"24", "Integer \"24\"" ), body_issues)
		self.assertIn(( 10,12,"3", "Integer \"3\"" ), body_issues)
		self.assertIn(( 10,12,"117/24", "Numerical item \"117/24\"" ), body_issues)
		self.assertIn(( 30,12,"3. CANCEL 117/24 AND THIS PARA=", "Excess \"=\"" ), body_issues)




	def test_EOS_issue(self):

		self.assertIn("EOS_issue", self.analysis)
		self.assertEqual(self.analysis["EOS_issue"], None)
















class Message4(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.message4 = str(

			"\n"
			"ZCZC LA18\n"
			"140356 UTC AUG 22\n"
			"NORWEGIAN NAV.WARNING 280\n"
			"CHART 4\n"
			"AREA OSLOFJORDEN\n"
			"TORPENE LIGHTBUOY 59-46.1N 010-33.2E UNLIT.\n"
			"NNNN\n"
		)
		cls.analyzer = Navanalyzer("K")
		cls.BoW = { "UTC": 1 }
		cls.analysis = cls.analyzer(cls.message4, cls.BoW)




	def test_proper_lines(self):

		self.assertIn("proper_lines", self.analysis)
		proper_lines = self.analysis["proper_lines"]
		self.assertIsInstance(proper_lines, list)
		self.assertEqual(len(proper_lines), 7)

		raw_lines = self.message4.split("\n")
		self.assertEqual(len(proper_lines[0]),	len(raw_lines[1]))
		self.assertEqual(len(proper_lines[1]),	len(raw_lines[2]))
		self.assertEqual(len(proper_lines[2]),	len(raw_lines[3]))
		self.assertEqual(len(proper_lines[3]),	len(raw_lines[4]))
		self.assertEqual(len(proper_lines[4]),	len(raw_lines[5]))
		self.assertEqual(len(proper_lines[5]),	len(raw_lines[6]))
		self.assertEqual(len(proper_lines[6]),	len(raw_lines[7]))




	def test_proper_message(self):

		self.assertIn("proper_message", self.analysis)
		proper_message = self.analysis["proper_message"]
		self.assertIsInstance(proper_message, str)
		self.assertNotEqual(len(proper_message), len(self.message4))




	def test_is_structured(self):

		self.assertIn("is_structured", self.analysis)
		self.assertFalse(self.analysis["is_structured"])




	def test_is_sanitized(self):

		self.assertIn("is_sanitized", self.analysis)
		self.assertFalse(self.analysis["is_sanitized"])




	def test_header_issue(self):

		self.assertIn("header_issue", self.analysis)
		self.assertEqual(

			self.analysis["header_issue"],
			"Incorrect NAVTEX header \"%s\""%self.analysis["proper_lines"][0].rstrip("\n")
		)




	def test_CDT_issues(self):

		self.assertIn("CDT_issues", self.analysis)
		self.assertIn(

			"CDT line \"%s\" doesn't match current date"%(
				self.analysis["proper_lines"][1].rstrip("\n")
			),	self.analysis["CDT_issues"]
		)




	def test_body_issues(self):

		self.assertIn("body_issues", self.analysis)
		body_issues = self.analysis["body_issues"]

		self.assertIn((		10,2,"140356", "Integer \"140356\"" ), body_issues)
		self.assertIn((		10,2,"22", "Integer \"22\"" ), body_issues)
		self.assertIn((		30,3,"NORWEGIAN", "Unknown word \"NORWEGIAN\"" ), body_issues)
		self.assertIn((		30,3,"NAV.WARNING", "Unknown word \"NAV.WARNING\"" ), body_issues)
		self.assertIn((		10,3,"280", "Integer \"280\"" ), body_issues)
		self.assertIn((		30,4,"CHART", "Unknown word \"CHART\"" ), body_issues)
		self.assertIn((		10,4,"4", "Integer \"4\"" ), body_issues)
		self.assertIn((		30,5,"AREA", "Unknown word \"AREA\"" ), body_issues)
		self.assertIn((		30,5,"OSLOFJORDEN", "Unknown word \"OSLOFJORDEN\"" ), body_issues)
		self.assertIn((		30,6,"TORPENE", "Unknown word \"TORPENE\"" ), body_issues)
		self.assertIn((		30,6,"LIGHTBUOY", "Unknown word \"LIGHTBUOY\"" ), body_issues)
		self.assertIn((		10,6,"59-46.1N", "Coordinatal point \"59-46.1N\"" ), body_issues)
		self.assertIn((		10,6,"010-33.2E", "Coordinatal point \"010-33.2E\"" ), body_issues)
		self.assertIn((		30,6,"UNLIT", "Unknown word \"UNLIT\"" ), body_issues)
		self.assertNotIn((	30,6,"TORPENE LIGHTBUOY 59-46.1N 010-33.2E UNLIT.=", "Excess \"=\"" ), body_issues)




	def test_EOS_issue(self):

		self.assertIn("EOS_issue", self.analysis)
		self.assertEqual(self.analysis["EOS_issue"], None)
















class Message5(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.message5 = str(

			"ZCZC KD00\n"
			"011040 UTC SEP 23\n"
			"ALERT PHASE OPERATION IN PROGRES.\n"
			"SINCE  01 SEP 23 FOUND BOAT ADRIFT.\n"
			"ALL SHIPS ENTERING AND LEAVING THE KOLA\n"
			"BAY TO KEEP SHARP LOOKOUT OF POTENTIAL\n"
			"MAN OVERBOARD. REPORT ALL INFORMATION\n"
			"TO MRCC MURMANSK +78152422182\n"
			"LOL\n"
		)
		cls.analyzer = Navanalyzer("K")
		cls.BoW = { "UTC": 1 }
		cls.analysis = cls.analyzer(cls.message5, cls.BoW)




	def test_proper_lines(self):

		self.assertIn("proper_lines", self.analysis)
		proper_lines = self.analysis["proper_lines"]
		self.assertIsInstance(proper_lines, list)
		self.assertEqual(len(proper_lines), 9)

		raw_lines = self.message5.split("\n")
		self.assertEqual(len(proper_lines[0]),		len(raw_lines[0]))
		self.assertEqual(len(proper_lines[1]),		len(raw_lines[1]))
		self.assertEqual(len(proper_lines[2]),		len(raw_lines[2]))
		self.assertNotEqual(len(proper_lines[3]),	len(raw_lines[3]))
		self.assertEqual(len(proper_lines[4]),		len(raw_lines[4]))
		self.assertEqual(len(proper_lines[5]),		len(raw_lines[5]))
		self.assertEqual(len(proper_lines[6]),		len(raw_lines[6]))
		self.assertEqual(len(proper_lines[7]),		len(raw_lines[7]))
		self.assertEqual(len(proper_lines[8]),		len(raw_lines[8]))




	def test_proper_message(self):

		self.assertIn("proper_message", self.analysis)
		proper_message = self.analysis["proper_message"]
		self.assertIsInstance(proper_message, str)
		self.assertNotEqual(len(proper_message), len(self.message5))




	def test_is_structured(self):

		self.assertIn("is_structured", self.analysis)
		self.assertFalse(self.analysis["is_structured"])




	def test_is_sanitized(self):

		self.assertIn("is_sanitized", self.analysis)
		self.assertTrue(self.analysis["is_sanitized"])




	def test_header_issue(self):

		self.assertIn("header_issue", self.analysis)
		self.assertEqual(self.analysis["header_issue"], None)




	def test_CDT_issues(self):

		self.assertIn("CDT_issues", self.analysis)
		self.assertIn(

			"CDT line \"%s\" doesn't match current date"%(
				self.analysis["proper_lines"][1].rstrip("\n")
			),	self.analysis["CDT_issues"]
		)




	def test_body_issues(self):

		self.assertIn("body_issues", self.analysis)
		body_issues = self.analysis["body_issues"]

		self.assertIn(( 10,2,"011040", "Integer \"011040\"" ), body_issues)
		self.assertIn(( 10,2,"UTC", "Known word \"UTC\"" ), body_issues)
		self.assertIn(( 30,2,"SEP", "Unknown word \"SEP\"" ), body_issues)
		self.assertIn(( 10,2,"23", "Integer \"23\"" ), body_issues)
		self.assertIn(( 30,3,"ALERT", "Unknown word \"ALERT\"" ), body_issues)
		self.assertIn(( 30,3,"PHASE", "Unknown word \"PHASE\"" ), body_issues)
		self.assertIn(( 30,3,"OPERATION", "Unknown word \"OPERATION\"" ), body_issues)
		self.assertIn(( 30,3,"IN", "Unknown word \"IN\"" ), body_issues)
		self.assertIn(( 30,3,"PROGRES", "Unknown word \"PROGRES\"" ), body_issues)
		self.assertIn(( 30,4,"SINCE", "Unknown word \"SINCE\"" ), body_issues)
		self.assertIn(( 10,4,"01", "Integer \"01\"" ), body_issues)
		self.assertIn(( 30,4,"SEP", "Unknown word \"SEP\"" ), body_issues)
		self.assertIn(( 10,4,"23", "Integer \"23\"" ), body_issues)
		self.assertIn(( 30,4,"FOUND", "Unknown word \"FOUND\"" ), body_issues)
		self.assertIn(( 30,4,"BOAT", "Unknown word \"BOAT\"" ), body_issues)
		self.assertIn(( 30,4,"ADRIFT", "Unknown word \"ADRIFT\"" ), body_issues)
		self.assertIn(( 30,5,"ALL", "Unknown word \"ALL\"" ), body_issues)
		self.assertIn(( 30,5,"SHIPS", "Unknown word \"SHIPS\"" ), body_issues)
		self.assertIn(( 30,5,"ENTERING", "Unknown word \"ENTERING\"" ), body_issues)
		self.assertIn(( 30,5,"AND", "Unknown word \"AND\"" ), body_issues)
		self.assertIn(( 30,5,"LEAVING", "Unknown word \"LEAVING\"" ), body_issues)
		self.assertIn(( 30,5,"THE", "Unknown word \"THE\"" ), body_issues)
		self.assertIn(( 30,5,"KOLA", "Unknown word \"KOLA\"" ), body_issues)
		self.assertIn(( 30,6,"BAY", "Unknown word \"BAY\"" ), body_issues)
		self.assertIn(( 30,6,"TO", "Unknown word \"TO\"" ), body_issues)
		self.assertIn(( 30,6,"KEEP", "Unknown word \"KEEP\"" ), body_issues)
		self.assertIn(( 30,6,"SHARP", "Unknown word \"SHARP\"" ), body_issues)
		self.assertIn(( 30,6,"LOOKOUT", "Unknown word \"LOOKOUT\"" ), body_issues)
		self.assertIn(( 30,6,"OF", "Unknown word \"OF\"" ), body_issues)
		self.assertIn(( 30,6,"POTENTIAL", "Unknown word \"POTENTIAL\"" ), body_issues)
		self.assertIn(( 30,7,"MAN", "Unknown word \"MAN\"" ), body_issues)
		self.assertIn(( 30,7,"OVERBOARD", "Unknown word \"OVERBOARD\"" ), body_issues)
		self.assertIn(( 30,7,"REPORT", "Unknown word \"REPORT\"" ), body_issues)
		self.assertIn(( 30,7,"ALL", "Unknown word \"ALL\"" ), body_issues)
		self.assertIn(( 30,7,"INFORMATION", "Unknown word \"INFORMATION\"" ), body_issues)
		self.assertIn(( 30,8,"TO", "Unknown word \"TO\"" ), body_issues)
		self.assertIn(( 30,8,"MRCC", "Unknown word \"MRCC\"" ), body_issues)
		self.assertIn(( 30,8,"MURMANSK", "Unknown word \"MURMANSK\"" ), body_issues)
		self.assertIn(( 10,8,"+78152422182",	"Phone number \"+78152422182\"" ), body_issues)




	def test_EOS_issue(self):

		self.assertIn("EOS_issue", self.analysis)
		self.assertEqual(

			self.analysis["EOS_issue"],
			"Incorrect EOS line \"%s\""%self.analysis["proper_lines"][-1].rstrip("\n")
		)
















class Message6(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.message6 = str(

			"ZCZC MA97\n"
			"291351 UTC AUG\n"
			"NAVAREA I 238/22 \n"
			"ENGLAND EAST  COAST.\n"
			"\n"
			"THAMES ESTUARY APPROACHES.\n"
			"CHART BA 1138(INT 1561).\n"
			"WAVERIDER LIGHT-BUOY AND FOUR GUARD\n"
			"LIGHT-BUOYS, ALL FL (5) Y.20S,\n"
			"ESTABLISHED 51-42.5N 001-51.0E.\n"
			"WIDE BERTH REQUESTED.\n"
			"NNNN\n"
		)
		cls.analyzer = Navanalyzer("K")
		cls.BoW = {

			"NAVAREA":		0,
			"ESTUARY":		0,
			"BA":			0,
			"COAST":		1,
			"APPROACHES":	1,
			"CHART":		1,
			"WAVERIDER":	1,
			"AND":			1,
			"FOUR":			1,
			"GUARD":		1,
			"ALL":			1,
			"ESTABLISHED":	1,
			"WIDE":			1,
			"BERTH":		1,
			"REQUESTED":	1,
		}
		cls.analysis = cls.analyzer(cls.message6, cls.BoW)




	def test_proper_lines(self):

		self.assertIn("proper_lines", self.analysis)
		proper_lines = self.analysis["proper_lines"]
		self.assertIsInstance(proper_lines, list)
		self.assertEqual(len(proper_lines), 11)

		raw_lines = self.message6.split("\n")
		self.assertEqual(len(proper_lines[0]),		len(raw_lines[0]))
		self.assertEqual(len(proper_lines[1]),		len(raw_lines[1]))
		self.assertNotEqual(len(proper_lines[2]),	len(raw_lines[2]))
		self.assertNotEqual(len(proper_lines[3]),	len(raw_lines[3]))
		self.assertEqual(len(proper_lines[4]),		len(raw_lines[5]))
		self.assertEqual(len(proper_lines[5]),		len(raw_lines[6]))
		self.assertEqual(len(proper_lines[6]),		len(raw_lines[7]))
		self.assertEqual(len(proper_lines[7]),		len(raw_lines[8]))
		self.assertEqual(len(proper_lines[8]),		len(raw_lines[9]))
		self.assertEqual(len(proper_lines[9]),		len(raw_lines[10]))
		self.assertEqual(len(proper_lines[10]),		len(raw_lines[11]))




	def test_proper_message(self):

		self.assertIn("proper_message", self.analysis)
		proper_message = self.analysis["proper_message"]
		self.assertIsInstance(proper_message, str)
		self.assertNotEqual(len(proper_message), len(self.message6))




	def test_is_structured(self):

		self.assertIn("is_structured", self.analysis)
		self.assertFalse(self.analysis["is_structured"])




	def test_is_sanitized(self):

		self.assertIn("is_sanitized", self.analysis)
		self.assertTrue(self.analysis["is_sanitized"])




	def test_header_issue(self):

		self.assertIn("header_issue", self.analysis)
		self.assertEqual(

			self.analysis["header_issue"],
			"Incorrect NAVTEX header \"%s\""%self.analysis["proper_lines"][0].rstrip("\n")
		)




	def test_CDT_issues(self):

		self.assertIn("CDT_issues", self.analysis)
		self.assertIn(

			"CDT line \"%s\" doesn't match current date"%(
				self.analysis["proper_lines"][1].rstrip("\n")
			),	self.analysis["CDT_issues"]
		)




	def test_body_issues(self):

		self.assertIn("body_issues", self.analysis)
		body_issues = self.analysis["body_issues"]

		self.assertIn(( 10,2,"291351", "Integer \"291351\"" ), body_issues)
		self.assertIn(( 20,3,"NAVAREA", "Pending word \"NAVAREA\"" ), body_issues)
		self.assertIn(( 30,3,"I", "Unknown word \"I\"" ), body_issues)
		self.assertIn(( 10,3,"238/22", "Numerical item \"238/22\"" ), body_issues)
		self.assertIn(( 30,4,"ENGLAND", "Unknown word \"ENGLAND\"" ), body_issues)
		self.assertIn(( 30,4,"EAST", "Unknown word \"EAST\"" ), body_issues)
		self.assertIn(( 30,4,"EAST", "Unknown word \"EAST\"" ), body_issues)
		self.assertIn(( 10,4,"COAST", "Known word \"COAST\"" ), body_issues)
		self.assertIn(( 30,5,"THAMES", "Unknown word \"THAMES\"" ), body_issues)
		self.assertIn(( 20,5,"ESTUARY", "Pending word \"ESTUARY\"" ), body_issues)
		self.assertIn(( 10,5,"APPROACHES", "Known word \"APPROACHES\"" ), body_issues)
		self.assertIn(( 10,6,"CHART", "Known word \"CHART\"" ), body_issues)
		self.assertIn(( 20,6,"BA", "Pending word \"BA\"" ), body_issues)
		self.assertIn(( 30,6,"1138(INT", "Unknown word \"1138(INT\"" ), body_issues)
		self.assertIn(( 10,6,"1561", "Integer \"1561\"" ), body_issues)
		self.assertIn(( 10,7,"WAVERIDER", "Known word \"WAVERIDER\"" ), body_issues)
		self.assertIn(( 30,7,"LIGHT-BUOY", "Unknown word \"LIGHT-BUOY\"" ), body_issues)
		self.assertIn(( 10,7,"AND", "Known word \"AND\"" ), body_issues)
		self.assertIn(( 10,7,"FOUR", "Known word \"FOUR\"" ), body_issues)
		self.assertIn(( 10,7,"GUARD", "Known word \"GUARD\"" ), body_issues)
		self.assertIn(( 30,8,"LIGHT-BUOYS", "Unknown word \"LIGHT-BUOYS\"" ), body_issues)
		self.assertIn(( 10,8,"ALL", "Known word \"ALL\"" ), body_issues)
		self.assertIn(( 30,8,"FL", "Unknown word \"FL\"" ), body_issues)
		self.assertIn(( 10,8,"5", "Integer \"5\"" ), body_issues)
		self.assertIn(( 30,8,"Y.20S", "Unknown word \"Y.20S\"" ), body_issues)
		self.assertIn(( 10,9,"ESTABLISHED", "Known word \"ESTABLISHED\"" ), body_issues)
		self.assertIn(( 10,9,"51-42.5N", "Coordinatal point \"51-42.5N\"" ), body_issues)
		self.assertIn(( 10,9,"001-51.0E", "Coordinatal point \"001-51.0E\"" ), body_issues)
		self.assertIn(( 10,10,"WIDE", "Known word \"WIDE\"" ), body_issues)
		self.assertIn(( 10,10,"BERTH", "Known word \"BERTH\"" ), body_issues)
		self.assertIn(( 10,10,"REQUESTED", "Known word \"REQUESTED\"" ), body_issues)




	def test_EOS_issue(self):

		self.assertIn("EOS_issue", self.analysis)
		self.assertEqual(self.analysis["EOS_issue"], None)
















class Message7(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.message7 = str(

			"\n"
			"ZCZC SA38\n"
			"NAVTEX-HAMBURG (NCC)\n"
			"131120 UTC SEP 22\n"
			"NAV WARN NO. 428\n"
			"TSS TERSCHELLING-GERMAN BIGHT\n"
			"'TG 2/GW' LIGHTBUOY 53-52N 006-22E\n"
			"OFF STATION AND DAMAGED.\n"
			"NNNN\n"
		)
		cls.analyzer = Navanalyzer("K")
		cls.BoW = dict()
		cls.analysis = cls.analyzer(cls.message7, cls.BoW)




	def test_proper_lines(self):

		self.assertIn("proper_lines", self.analysis)
		proper_lines = self.analysis["proper_lines"]
		self.assertIsInstance(proper_lines, list)
		self.assertEqual(len(proper_lines), 8)

		raw_lines = self.message7.split("\n")
		self.assertEqual(len(proper_lines[0]),	len(raw_lines[1]))
		self.assertEqual(len(proper_lines[1]),	len(raw_lines[2]))
		self.assertEqual(len(proper_lines[2]),	len(raw_lines[3]))
		self.assertEqual(len(proper_lines[3]),	len(raw_lines[4]))
		self.assertEqual(len(proper_lines[4]),	len(raw_lines[5]))
		self.assertEqual(len(proper_lines[5]),	len(raw_lines[6]))
		self.assertEqual(len(proper_lines[6]),	len(raw_lines[7]))




	def test_proper_message(self):

		self.assertIn("proper_message", self.analysis)
		proper_message = self.analysis["proper_message"]
		self.assertIsInstance(proper_message, str)
		self.assertNotEqual(len(proper_message), len(self.message7))




	def test_is_structured(self):

		self.assertIn("is_structured", self.analysis)
		self.assertFalse(self.analysis["is_structured"])




	def test_is_sanitized(self):

		self.assertIn("is_sanitized", self.analysis)
		self.assertFalse(self.analysis["is_sanitized"])




	def test_header_issue(self):

		self.assertIn("header_issue", self.analysis)
		self.assertEqual(

			self.analysis["header_issue"],
			"Incorrect NAVTEX header \"%s\""%self.analysis["proper_lines"][0].rstrip("\n")
		)




	def test_CDT_issues(self):

		self.assertIn("CDT_issues", self.analysis)
		self.assertIn(

			"CDT line \"%s\" doesn't match current date"%(
				self.analysis["proper_lines"][2].rstrip("\n")
			),	self.analysis["CDT_issues"]
		)




	def test_body_issues(self):

		self.assertIn("body_issues", self.analysis)
		body_issues = self.analysis["body_issues"]

		self.assertIn(( 30,2,"NAVTEX-HAMBURG", "Unknown word \"NAVTEX-HAMBURG\"" ), body_issues)
		self.assertIn(( 30,2,"NCC", "Unknown word \"NCC\"" ), body_issues)
		self.assertIn(( 10,3,"131120", "Integer \"131120\"" ), body_issues)
		self.assertIn(( 30,3,"UTC", "Unknown word \"UTC\"" ), body_issues)
		self.assertIn(( 30,3,"SEP", "Unknown word \"SEP\"" ), body_issues)
		self.assertIn(( 10,3,"22", "Integer \"22\"" ), body_issues)
		self.assertIn(( 30,4,"NAV", "Unknown word \"NAV\"" ), body_issues)
		self.assertIn(( 30,4,"WARN", "Unknown word \"WARN\"" ), body_issues)
		self.assertIn(( 30,4,"NO", "Unknown word \"NO\"" ), body_issues)
		self.assertIn(( 10,4,"428", "Integer \"428\"" ), body_issues)
		self.assertIn(( 30,5,"TSS", "Unknown word \"TSS\"" ), body_issues)
		self.assertIn(( 30,5,"TERSCHELLING-GERMAN", "Unknown word \"TERSCHELLING-GERMAN\"" ), body_issues)
		self.assertIn(( 30,5,"BIGHT", "Unknown word \"BIGHT\"" ), body_issues)
		self.assertIn(( 30,6,"TG", "Unknown word \"TG\"" ), body_issues)
		self.assertIn(( 10,6,"2/GW", "Numerical item \"2/GW\"" ), body_issues)
		self.assertIn(( 30,6,"LIGHTBUOY", "Unknown word \"LIGHTBUOY\"" ), body_issues)
		self.assertIn(( 10,6,"53-52N", "Coordinatal point \"53-52N\"" ), body_issues)
		self.assertIn(( 10,6,"006-22E", "Coordinatal point \"006-22E\"" ), body_issues)
		self.assertIn(( 30,7,"OFF", "Unknown word \"OFF\"" ), body_issues)
		self.assertIn(( 30,7,"STATION", "Unknown word \"STATION\"" ), body_issues)
		self.assertIn(( 30,7,"AND", "Unknown word \"AND\"" ), body_issues)
		self.assertIn(( 30,7,"DAMAGED", "Unknown word \"DAMAGED\"" ), body_issues)




	def test_EOS_issue(self):

		self.assertIn("EOS_issue", self.analysis)
		self.assertEqual(self.analysis["EOS_issue"], None)











if	__name__ == "__main__" : unittest.main(verbosity=2)







