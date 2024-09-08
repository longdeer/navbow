from re					import VERBOSE
from re					import compile	as pmake
from string				import ascii_letters
from string				import ascii_uppercase
from datetime			import datetime
from typing				import List
from typing				import Tuple
from typing				import Dict
from collections.abc	import Mapping








class Navanalyzer:

	"""
		Navtex messages analyzer solution

		BoW			-	Bag of Words, the hash table of NAVTEX words, that are used in messages,
						to check spelling against; it is assumed to be just a dict or a
						pygwarts.irma.shelve.LibraryShelf instance
		station		-	current station litera
		categories	-	the most significant for current station message categories, that are to be
						checked, might be provided as a string or as an array of characters/strings
	"""

	def process_header(self, header_line :str) -> None | str :

			"""
				Process NAVTEX header
				If header is valid, None returned, otherwise corresponding message string
			"""

			try:

				header = self.NAVTEX_MESSAGE_HEADER.fullmatch(header_line).group("msg_id")
				if	not hasattr(self, "check") or not isinstance(self.check, dict) : return header
				self.check["header_id"] = header

			except	AttributeError: return f"Incorrect NAVTEX header \"{header_line}\""




	def process_CDT(self, message_body_lines :List[str]) -> None | Tuple[str]:

			"""
				CDT - Creation Date & Time
				As CDT line is optional for NAVTEX message, current method will search through
				all (message body) lines for CDT. If found, will be processed, otherwise corresponding
				message (about CDT absence) will be produced.
				If no year specified, it will be obtained by the moment it is invoked.
			"""

			current = datetime.now()
			CDT_issues = list()


			for line in message_body_lines:
				CDT = self.NAVTEX_MESSAGE_CDT.fullmatch(line)

				if	hasattr(CDT, "group"):
					d,HM,m,Y = CDT.group("msg_day", "msg_time", "msg_month", "msg_year")




					# This flow is extra guard for parsed values. Despite "NAVTEX_MESSAGE_CDT" regex
					# must return only groups that probably would satisfy datetime pattern, in case
					# "NAVTEX_MESSAGE_CDT" altered to return something different and strange, the
					# following checkers will marked it down for user as corresponding messages.
					if		Y is None :						Y = current.strftime("%Y")
					elif	len(Y) == 2 and Y.isdigit():	Y = f"20{Y}"
					else:	CDT_issues.append(f"Incorrect year format in CDT line \"{line}\"")


					if	not (d and len(d) == 2 and d.isdigit()) or not (m and len(m) == 3):
						CDT_issues.append(f"Incorrect date format in CDT line \"{line}\"")


					if	not (HM and len(HM) == 4 and HM.isdigit()):
						CDT_issues.append(f"Incorrect time format in CDT line \"{line}\"")




					message_D = f"{d}/{self.NAVTEX_MESSAGE_MONTH_MAPPING.get(m)}/{Y}"
					message_T = HM


					if	message_D != current.strftime("%d/%m/%Y"):
						CDT_issues.append(f"CDT line \"{line}\" doesn't match current date")


					if	not hasattr(self, "check") or not isinstance(self.check, dict):	break


					self.check["message_CDT"] = line, message_D, message_T
					break


			else:	CDT_issues.append("No line looks like message creation timestamp")
			return	tuple(CDT_issues) or None








	def process_body(
						self,
						body_lines							:List[str],
						BoW									:Mapping[str,int]
					)-> None | Tuple[Tuple[int,int,str,str]]:

			"""
				Iterates through every space separated string in NAVTEX message body (all lines of message
				except first, which must be header and second, that must be EoS) and searches for the
				bag of words ("BoW") mapping occurence. The entire process relies on the scheme, where
				every word in the "BoW" might be considered as "known" or "pend". While the key in "BoW"
				is the word itself, the value either 0 for "pend" and 0< for "known". If the word not
				in "BoW" it considered "unknown" with corresponding actions, like adding to the "body_issues"
				and also added BoW as "pend". All "unknown" words goes to "NEW_TEXT_WORDS" set this
				collection might be used to maintain "BoW".
			"""

			self.check_BoW(BoW)
			body_issues = list()


			if	body_lines:
				for N,line in enumerate(body_lines, 2):

					if	line.endswith("=") : body_issues.append(( 30,N,line,"Excess \"=\"" ))
					for chars_chunk in line.split():

						try:

							num_int,		\
							num_int_unit,	\
							num_dec,		\
							num_dec_unit,	\
							num_date,		\
							num_time,		\
							num_range,		\
							num_item,		\
							num_phone,		= self.TEXT_NUMERICAL.fullmatch(chars_chunk).group(

								"num_int",
								"num_int_unit",
								"num_dec",
								"num_dec_unit",
								"num_date",
								"num_time",
								"num_range",
								"num_item",
								"num_phone",
							)


							# Checking out every possible group match in terms of debugging, cause
							# corresponding records will be produced.
							if	num_int is not None:
								body_issues.append(( 10,N,num_int,f"Integer \"{num_int}\"" ))

							if	num_int_unit is not None:
								body_issues.append(( 10,N,num_int_unit,f"Integer unit \"{num_int_unit}\"" ))

							if	num_dec is not None:
								body_issues.append(( 10,N,num_dec,f"Decimal \"{num_dec}\"" ))

							if	num_dec_unit is not None:
								body_issues.append(( 10,N,num_dec_unit,f"Decimal unit \"{num_dec_unit}\"" ))

							if	num_date is not None:
								body_issues.append(( 10,N,num_date,f"Date \"{num_date}\"" ))

							if	num_time is not None:
								body_issues.append(( 10,N,num_time,f"Time \"{num_time}\"" ))

							if	num_range is not None:
								body_issues.append(( 10,N,num_range,f"Range \"{num_range}\"" ))

							if	num_item is not None:
								body_issues.append(( 10,N,num_item,f"Numerical item \"{num_item}\"" ))

							if	num_phone is not None:
								body_issues.append(( 10,N,num_phone,f"Phone number \"{num_phone}\"" ))


						except	AttributeError : pass
						else:	continue


						try:

							cord_point =  self.TEXT_COORDINATAL.fullmatch(chars_chunk).group("cord_point")

							if	cord_point is not None:
								body_issues.append(( 10,N,cord_point,f"Coordinatal point \"{cord_point}\"" ))


						except	AttributeError : pass
						else:	continue


						try:

							alnum_symb_chars, alnum_abbr_chars = self.TEXT_ALPHABETIC.fullmatch(

								chars_chunk
							).group(
								"alnum_symb_chars", "alnum_abbr_chars"
							)


							word = alnum_symb_chars or alnum_abbr_chars
							word = word.rstrip(".")


							if	word in BoW:
								if	BoW[word]:

									body_issues.append(( 10,N,word,f"Known word \"{word}\"" ))
								else:
									body_issues.append(( 20,N,word,f"Pending word \"{word}\"" ))
							else:
								body_issues.append(( 30,N,word,f"Unknown word \"{word}\"" ))
								self.NEW_TEXT_WORDS.add(word)


						except	AttributeError : pass
						else:	continue
						body_issues.append(( 40,N,chars_chunk,f"Not handled \"{chars_chunk}\""))
			else:		body_issues.append(( 20,-1,"",f"Empty messsage body" ))
			return		tuple(body_issues) or None








	def process_EOS(self, EOS_line :str) -> None | str :

		"""
			Validate the very end line is the correct NNNN
		"""

		if	EOS_line != "NNNN" : return f"Incorrect EOS line \"{EOS_line}\""




	def update_BoW(self, BoW :Mapping[str,int]) -> int :

		"""
			Updates bag-of-words mapping by adding all words from "NEW_TEXT_WORDS" field paired with
			corresponding "0" value, which states "pend" status for all of them. Returns the number of
			words that were added to BoW. The next steps of perseverance the mapping is out of scope
			of current Navanalyzer implementation.
		"""

		self.check_BoW(BoW)
		counter = 0


		for word in self.NEW_TEXT_WORDS:
			if	all( symbol in self.ALLOWED_SYMBOLS for symbol in word ):

				BoW[word] = 0
				counter += 1


		self.NEW_TEXT_WORDS = set()
		return	counter




	def check_BoW(self, BoW :Mapping[str,int]) -> None | AssertionError :

		"""
			Helper method that verifies "BoW" tries to implement mapping protocol, which means it's
			just has "keys" as "__getitem__" members implemented. Raises AssertionError	otherwise.
		"""

		assert (

				hasattr(BoW, "keys") and hasattr(BoW, "__getitem__")
			),	"Provided bag of NAVTEX words is invalid"




	def split_lines(self, message :str) -> List[str] :

		"""
			Process raw message lines and return raw lines.
		"""

		return	[ line for line in message.split("\n") if line and not line.isspace() ]




	def get_proper_lines(self, raw_lines :List[str]) -> List[str] :

		"""
			Process raw message lines and return validated message lines
		"""

		return	[ " ".join(line.split()).upper() for line in raw_lines ]








	def __init__(self, station :str, categories :str | List[str] =None):

		assert (

			isinstance(station, str) and
			len(station) == 1 and
			station in ascii_letters and
			station not in "yYzZ"
		),	"Provided station identificator is invalid for NAVTEX"


		self._station = station.upper()


		if	categories is not None:
			raw_categories = set("".join( str(candidate) for candidate in categories ))

			assert all(

				category in ascii_letters
				for category in raw_categories
			),	"Provided messages categories are invalid for NAVTEX"

			self._categories = "".join(raw_categories).upper()
		else:
			self._categories = ascii_uppercase




		# The proper header's message id must consist of validated station litera (B1), messages category
		# litera (B2) and corresponding message number. The following regular expression also considers
		# header to comply the rule, that VITAL and IMPORTANT only message categories, like "D" or "B"
		# must only be numbered as "00".
		self.NAVTEX_MESSAGE_HEADER = pmake(

			rf"""
				^
				ZCZC\ (?P<msg_id>{self._station}[DB]00|
				{self._station}[{self._categories.replace('B','').replace('D','')}]\d\d)
				$
			""",
			VERBOSE
		)


		# The message date and time is just a Pattern to be matched against. Despite the header validation
		# in mathcing time, the datetime validation will take place later, in message processing time.
		self.NAVTEX_MESSAGE_CDT = pmake(

			r"""
				^
				(?P<msg_day>\d\d)(?P<msg_time>\d{4})\ UTC\ 
				(?P<msg_month>JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)
				(\ (?P<msg_year>\d\d))?
				$
			""",
			VERBOSE
		)


		# Literals month mapping to digit representation to maintain the default date format
		self.NAVTEX_MESSAGE_MONTH_MAPPING = {
		
			"JAN": "01",
			"FEB": "02",
			"MAR": "03",
			"APR": "04",
			"MAY": "05",
			"JUN": "06",
			"JUL": "07",
			"AUG": "08",
			"SEP": "09",
			"OCT": "10",
			"NOV": "11",
			"DEC": "12"
		}




		# Message body expressions
		self.TEXT_COORDINATAL	= pmake(

			r"""
				^
				[\('"]*
				(?P<cord_point>\d{2,3}(-\d\d)?(\.\d+)?[SWEN])
				[\)\.,:;'"]*
				$
			""",
			VERBOSE
		)
		self.TEXT_NUMERICAL		= pmake(

			r"""
				^
				[\('"]*												# possible punctuation at the start
				(
				(?P<num_int>\d+)								|	# intger
				(?P<num_int_unit>\d+[A-Z]+)						|	# intger unit, name, datetime, e.t.c.
				(?P<num_dec>\d+[\.,]\d+)						|	# decimal
				(?P<num_dec_unit>\d+[\.,]\d+[A-Z]+)				|	# decimal unit
				(?P<num_date>\d\d[-\\\./]\d\d[-\\\./]\d\d\d?\d?)|	# date
				(?P<num_time>
					[012]?\d:\d\d(?:UTC)?	|
					[012]\d{4}(?:UTC)
				)												|	# time
				(?P<num_range>\d+([\.,]\d+)?-\d+([\.,]\d+)?)	|	# swell, velocity, e.t.c.
				(?P<num_item>([A-Z]+[\.\-:]?)?\d+(/[A-Z\d]+)?)	|	# message number, name, e.t.c.
				(?P<num_phone>\+?[\d\(\)]+)						|	# phone number
				)
				[\)\.,:;'"]*										# possible punctuation at the end
				$
			""",
			VERBOSE
		)
		self.TEXT_ALPHABETIC	= pmake(

			r"""
				^
				(
				[\('\"]*
				(?P<alnum_symb_chars>[A-Z\/\\\-\(\d]+)
				[\)\.,:;'\"=]*
				$
				)|(
				[\('\"]*
				(?P<alnum_abbr_chars>[A-Z\/\\\-\.\(\d]+?\.?)
				(?:[\),:;'\"=]*|[\)\"']*\.*)
				$
				)
			""",
			VERBOSE
		)
		# Current allowed symbols are cnstructed by the fact the NAVTEX message must be short and
		# clean, without extra symbols. Most of following symbols were infered imperical way to suit
		# NAVTEX. This is almost full and enough set for NAVTEX.
		self.ALLOWED_SYMBOLS	= "=!\"'()+,-./0123456789:;ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.TEXT_MSG_STRUCT	= pmake(r"^(?:[ =!\"'\(\)\+,\-\./0-9:;A-Z]+\n)+[ =!\"'\(\)\+,\-\./0-9:;A-Z]+$")
		self.NEW_TEXT_WORDS		= set()








	def __call__(
					self,
					message					:str,
					BoW						:Mapping[str,int],
					separator				:str				="\n"
				)-> Dict[str,bool|str|Tuple]:

		current_lines	= self.split_lines(message)
		proper_lines	= self.get_proper_lines(current_lines)


		assert 1 <len(proper_lines), "NAVTEX message length less than 2 lines"


		self.check =  {

			"raw_message":	message,
			"header_id":	None,
			"message_CDT":	None,
		}


		current_message	= separator.join(current_lines)
		proper_message	= separator.join(proper_lines)


		self.check["proper_lines"]		= proper_lines
		self.check["proper_message"]	= proper_message
		self.check["is_structured"]		= bool(self.TEXT_MSG_STRUCT.fullmatch(message))
		self.check["is_sanitized"]		= len(proper_message) != len(current_message)
		self.check["header_issue"]		= self.process_header(proper_lines[0])
		self.check["CDT_issues"]		= self.process_CDT(proper_lines[1:-1])
		self.check["body_issues"]		= self.process_body(proper_lines[1:-1], BoW)
		self.check["EOS_issue"]			= self.process_EOS(proper_lines[-1])


		return	self.check.copy()







