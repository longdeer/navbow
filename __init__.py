from typing								import List
from typing								import Dict
from typing								import Tuple
from datetime							import datetime
from collections						import defaultdict
from NavtexBoWAnalyzer.header			import B1
from NavtexBoWAnalyzer.header			import G_NAVTEX_MESSAGE_HEADER
from NavtexBoWAnalyzer.coordinates		import P_COORDINATE
from NavtexBoWAnalyzer.numerical		import P_NUMERICAL
from NavtexBoWAnalyzer.alphanumerical	import P_ALPHANUMERICAL
from NavtexBoWAnalyzer.cdt				import G_MESSAGE_CDT
from NavtexBoWAnalyzer.cdt				import MONTH_MAP
from NavtexBoWAnalyzer.scanner			import sanit_state
from NavtexBoWAnalyzer.scanner			import word_scan








class Navanalyzer:

	"""
		Navtex messages analyzing tool.
		Very simple.
		Uses Bag of Words method to store all alphabetic words to be recognized.
		Treats almost all alphanumeric words as non-memorizable chunks.

		v 1.0.0 2024 jun 13

		author: lngd
		lngdeer@gmail.com


		old:
		Navtex messages analyzer solution

		BoW			-	Bag of Words, the hash table of NAVTEX words, that are used in messages,
						to check spelling against; it is assumed to be just a dict or a
						pygwarts.irma.shelve.LibraryShelf instance
		station		-	current station litera
		categories	-	the most significant for current station message categories, that are to be
						checked, might be provided as a string or as an array of characters/strings

		Process NAVTEX header
		If header is valid, None returned, otherwise corresponding message string

		CDT - Creation Date & Time
		As CDT line is optional for NAVTEX message, current method will search through
		all (message body) lines for CDT. If found, will be processed, otherwise corresponding
		message (about CDT absence) will be produced.
		If no year specified, it will be obtained by the moment it is invoked.

		Iterates through every space separated string in NAVTEX message body (all lines of message
		except first, which must be header and second, that must be EoS) and searches for the
		bag of words ("BoW") mapping occurence. The entire process relies on the scheme, where
		every word in the "BoW" might be considered as "known" or "pend". While the key in "BoW"
		is the word itself, the value either 0 for "pend" and 0< for "known". If the word not
		in "BoW" it considered "unknown" with corresponding actions, like adding to the "body_issues"
		and also added BoW as "pend". All "unknown" words goes to "NEW_TEXT_WORDS" set this
		collection might be used to maintain "BoW".


		scanned good symbols:
		'()+,-./0123456789:=ABCDEFGHIJKLMNOPQRSTUVWXYZ
	"""

	def __init__(self, station :str):

		assert (

			isinstance(station,str) and len(station) == 1 and station.upper() in B1
		),	f"Invalid station literal {station}"

		self.station = station.upper()

	def with_mapping(self, path :str, BoW :Dict[str,int]) -> Dict[str,int|List|Dict] | None :

		"""
			Ananlysis implementation that uses dictionary 

			0	- broken bytes detected by byte_scan;
			1	- message without header, EoS, CDT and any words (only numerical, alphanumerical
				and coordinates);
			3	- sanitized message without header, EoS, CDT and any words (only numerical, alphanumerical
				and coordinates);
			5	- message without EoS, CDT and any words (only numerical, alphanumerical and coordinates);
			7	- sanitized message without EoS, CDT and any words (only numerical, alphanumerical
				and coordinates);
			9	- message without header, CDT and any words (only numerical, alphanumerical and coordinates);
			11	- sanitized message without header, CDT and any words (only numerical, alphanumerical
				and coordinates);
			13	- message without CDT and any words (only numerical, alphanumerical and coordinates);
			15	- sanitized message without CDT and any words (only numerical, alphanumerical and
				coordinates);
			17	- message without header, EoS, CDT, with known word;
			19	- sanitized message without header, EoS, CDT, with known word;
			21	- message without EoS, CDT, with known word;
			23	- sanitized message without EoS, CDT, with known word;
			25	- message without header, CDT, with known word;
			27	- sanitized message without header, CDT, with known word;
			29	- message without CDT, with known word;
			31	- sanitized message without CDT, with known word;
			33	- message without header, EoS, CDT, with unknown or pending word;
			35	- sanitized message without header, EoS, CDT, with unknown or pending word;
			37	- message without EoS, CDT, with unknown or pending word;
			39	- sanitized message without EoS, CDT, with unknown or pending word;
			41	- message without header, CDT, with unknown or pending word;
			43	- sanitized message without header, CDT, with unknown or pending word;
			45	- message without CDT, with unknown or pending word;
			47	- sanitized message without CDT, with unknown or pending word;
			49	- message without header, EoS, CDT, with known and unknown or pending words;
			51	- sanitized message without header, EoS, CDT, with known and unknown or pending words;
			53	- message without EoS, CDT, with known and unknown or pending words;
			55	- sanitized message without EoS, CDT, with known and unknown or pending words;
			57	- message without header, CDT, with known and unknown or pending words;
			59	- sanitized message without header, CDT, with known and unknown or pending words;
			61	- message without CDT, with known and unknown or pending words;
			63	- sanitized message without CDT, with known and unknown or pending words;

			65	- impossible state cause CDT must content any words;
			67	- impossible state cause CDT must content any words;
			69	- impossible state cause CDT must content any words;
			71	- impossible state cause CDT must content any words;
			73	- impossible state cause CDT must content any words;
			75	- impossible state cause CDT must content any words;
			77	- impossible state cause CDT must content any words;
			79	- impossible state cause CDT must content any words;

			81	- message without header, EOS, with known word;
			83	- sanitized message without header, EOS, with known word;
			85	- message without EOS, with known word;
			87	- sanitized message without EOS, with known word;
			89	- message without header, with known word;
			91	- sanitized message without header, with known word;
			93	- message with known word;
			95	- sanitized message with known word;
			97	- message without header, EoS, with unknown or pending word;
			99	- sanitized message without header, EoS, with unknown or pending word;
			101	- message without EoS, with unknown or pending word;
			103	- sanitized message without EoS, with unknown or pending word;
			105	- message without header, with unknown or pending word;
			107	- sanitized message without header, with unknown or pending word;
			109	- message with unknown or pending word;
			111	- sanitized message with unknown or pending word;
			113	- message without header, EoS, with known and unknown or pending words;
			115	- sanitized message without header, EoS, with known and unknown or pending words;
			117	- message without EoS, with known and unknown or pending words;
			119	- sanitized message without EoS, with known and unknown or pending words;
			121	- message without header, with known and unknown or pending words;
			123	- sanitized message without header, with known and unknown or pending words;
			125	- message with known and unknown or pending words;
			127	- sanitized message with known and unknown or pending words;
		"""

		if	isinstance(sanit := sanit_state(path), dict) and isinstance(state := sanit.get("sanit"), int):
			if	state:

				raw_lines	= sanit["raw_lines"]
				air_lines	= sanit["air_lines"]
				analysis	= {

					"coords":	defaultdict(lambda : defaultdict(int)),
					"alnums":	defaultdict(lambda : defaultdict(int)),
					"nums":		defaultdict(lambda : defaultdict(int)),
					"known":	defaultdict(lambda : defaultdict(int)),
					"unknown":	defaultdict(lambda : defaultdict(int)),
					"pending":	defaultdict(lambda : defaultdict(int)),
					"punc":		defaultdict(lambda : defaultdict(int)),
				}


				header, *body, eos = air_lines
				state  ^= (eos == [ "NNNN" ]) <<3
				scan	= word_scan(body)
				pend	= set()


				if	(SSN := self.is_valid_header(" ".join(header))) is not None:

					analysis["header"] = SSN
					state  |= 4


				for i,unmatch in scan[1]: analysis["punc"][i][unmatch] += 1
				for i in range(1,len(scan[0]) +1):


					line = scan[0][i]


					if	(match := G_MESSAGE_CDT.fullmatch(" ".join(line))):
						
						d,m,H,M,Y = match.group("day", "month", "hour", "minute", "year")
						Y = int(f"20{Y}") if Y else int(datetime.today().strftime("%Y"))
						m = MONTH_MAP[m]
						d = int(d)
						H = int(H)
						M = int(M)

						analysis["cdt"] = datetime(Y,m,d,H,M)
						state |= 64


					for word in line:


						if		P_COORDINATE.fullmatch(word):		analysis["coords"][i][word]	+= 1
						elif	P_ALPHANUMERICAL.fullmatch(word):	analysis["alnums"][i][word]	+= 1
						elif	P_NUMERICAL.fullmatch(word):		analysis["nums"][i][word]	+= 1
						else:


							try:	BoW_state = BoW[word]
							except:	BoW_state = None
							match	BoW_state:

								case None:

									analysis["unknown"][i][word] += 1
									pend.add(word)
									BoW[word] = 0
									state |= 32

								case 0 if word not in pend:

									analysis["pending"][i][word] += 1
									state |= 32

								case 0: analysis["unknown"][i][word] += 1
								case _:

									analysis["known"][i][word] += 1
									state |= 16
				return	{

					"analysis":	analysis,
					"state":	state,
					"air":		air_lines,
					"raw":		raw_lines,
				}
			return	{

				"message":	sanit.get("message"),
				"state":	state,
			}




	def is_valid_header(self, header :str) -> Tuple[str,str,str] | None :

		"""
			Helper method that will try to extract a B1 from the "header" string and return True
			if it is the same letter than "station" field, obtained in initiation time. Returns
			False in any other cases, including Exception raises.
		"""

		try:

			match = G_NAVTEX_MESSAGE_HEADER.fullmatch(header)
			station, subject, number = match.group("tcB1", "tcB2", "tcB34")

			if	station == self.station : return station, subject, number
		except:	return







