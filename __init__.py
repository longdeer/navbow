from typing								import List
from typing								import Dict
from typing								import Tuple
from datetime							import datetime
from collections						import defaultdict
from pathlib							import Path
from NavtexBoWAnalyzer.header			import B1
from NavtexBoWAnalyzer.header			import G_NAVTEX_MESSAGE_HEADER
from NavtexBoWAnalyzer.coordinates		import P_COORDINATE
from NavtexBoWAnalyzer.numerical		import P_NUMERICAL
from NavtexBoWAnalyzer.alphanumerical	import P_ALPHANUMERICAL
from NavtexBoWAnalyzer.DTG				import G_MESSAGE_DTG
from NavtexBoWAnalyzer.DTG				import MONTH_MAP
from NavtexBoWAnalyzer.scanner			import sanit_state
from NavtexBoWAnalyzer.scanner			import word_scan








class Navanalyzer:

	"""
		Navtex messages analyzer.
		Implements the tecnique, that reads text file, splits by whitespaces it's content to chunks,
		and compares chunks against Bag of Word - special container with state determined words.
		Not all chunks will form a "word", so analyzer will first try to filter out following chunks:
			- coordinates;
			- numbers;
			- alphabetic numbers.
		This filtering will rely on regular expression matching, so any totally unmatched chunk will be
		considered a "word" candidate. Such candidates will be then compared with Bag of Word content.
		This is suggestion for Navtex messages processing, which general purpose is filtering out
		determined information and attract attention to probably controversial moments.
		Messages processing will comply "NAVTEX MANUAL" by IMO, which determines following structure:

		Element                          | Example
		--------------------------------------------------------------
		Phasing signal                   |
		--------------------------------------------------------------
		Start of message group           | ZCZC
		--------------------------------------------------------------
		One space                        |
		--------------------------------------------------------------
		NAVTEX message identity          | FA01
		--------------------------------------------------------------
		Carriage return + line feed      |
		--------------------------------------------------------------
		Message content                  | (Date Time Group – Optional
		                                 | e.g. 040735 UTC OCT 21)
		                                 | NAV I 114/21
		                                 | ENGLISH CHANNEL. START
		                                 | POINT SOUTHWARD.
		                                 | CHART BA 442 (INT 1701).
		                                 | UNEXPLODED ORDNANCE
		                                 | LOCATED
		                                 | 49-51.97N 003-39.54W AND
		                                 | 49-55.24N 003-40.79W.
		--------------------------------------------------------------
		End of message instruction       | NNNN
		--------------------------------------------------------------
		Carriage return + two line feeds |
		--------------------------------------------------------------
		Phasing signal                   |

		Also will maintains message "state" which will reflect details.
	"""

	def __init__(self, station :str):

		assert (

			isinstance(station,str) and len(station) == 1 and station.upper() in B1
		),	f"Invalid station literal {station}"

		self.station = station.upper()

	def with_mapping(self, path :str | Path, BoW :Dict[str,int]) -> Dict[str,int|List|Dict] | None :

		"""
			Analysis implementation that uses dictionary like mapping as "Bag of Words". Maintains a
			dictionary of message details. Relies on preliminary "sanit_state" exploration, which must
			provide "state" and either "message" in case of non-utf8 symbols, or useful statistics
			otherwise. Will extend "state" integer by more detailed inspection as following:
				0	- broken bytes detected by "byte_scan", or file has no valid symbols;
				1	- message without header, EoS, DTG and any words (only numerical, alphanumerical
					and coordinates);
				3	- sanitized message without header, EoS, DTG and any words (only numerical,
					alphanumerical and coordinates);
				5	- message without EoS, DTG and any words (only numerical, alphanumerical and
					coordinates);
				7	- sanitized message without EoS, DTG and any words (only numerical, alphanumerical
					and coordinates);
				9	- message without header, DTG and any words (only numerical, alphanumerical and
					coordinates);
				11	- sanitized message without header, DTG and any words (only numerical, alphanumerical
					and coordinates);
				13	- message without DTG and any words (only numerical, alphanumerical and coordinates);
				15	- sanitized message without DTG and any words (only numerical, alphanumerical and
					coordinates);
				17	- message without header, EoS, DTG, with known word;
				19	- sanitized message without header, EoS, DTG, with known word;
				21	- message without EoS, DTG, with known word;
				23	- sanitized message without EoS, DTG, with known word;
				25	- message without header, DTG, with known word;
				27	- sanitized message without header, DTG, with known word;
				29	- message without DTG, with known word;
				31	- sanitized message without DTG, with known word;
				33	- message without header, EoS, DTG, with unknown or pending word;
				35	- sanitized message without header, EoS, DTG, with unknown or pending word;
				37	- message without EoS, DTG, with unknown or pending word;
				39	- sanitized message without EoS, DTG, with unknown or pending word;
				41	- message without header, DTG, with unknown or pending word;
				43	- sanitized message without header, DTG, with unknown or pending word;
				45	- message without DTG, with unknown or pending word;
				47	- sanitized message without DTG, with unknown or pending word;
				49	- message without header, EoS, DTG, with known and unknown or pending words;
				51	- sanitized message without header, EoS, DTG, with known and unknown or pending words;
				53	- message without EoS, DTG, with known and unknown or pending words;
				55	- sanitized message without EoS, DTG, with known and unknown or pending words;
				57	- message without header, DTG, with known and unknown or pending words;
				59	- sanitized message without header, DTG, with known and unknown or pending words;
				61	- message without DTG, with known and unknown or pending words;
				63	- sanitized message without DTG, with known and unknown or pending words;

				65	- impossible state cause DTG must content any words;
				67	- impossible state cause DTG must content any words;
				69	- impossible state cause DTG must content any words;
				71	- impossible state cause DTG must content any words;
				73	- impossible state cause DTG must content any words;
				75	- impossible state cause DTG must content any words;
				77	- impossible state cause DTG must content any words;
				79	- impossible state cause DTG must content any words;

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
			"sanit_state" might obtain False "broken" state from "byte_scan", but the message
			will not content any valid symbols. In this case, "sanit_state" will return full dictionary,
			but "with_mapping" return value due zero "state" will try to return dictionary with
			"message" key, which is not present in "sanit_state" return value, so it will be None.
			All unknown words will be mapped in "BoW" with 0, so "BoW" will be eventually altered.
			Return value is a dictionary, which might be of two types:
				state, message - for the "corrupted" files;
				state, analysis, raw, air - all other cases.
		"""

		if	isinstance(sanit := sanit_state(path), dict) and isinstance(state := sanit.get("sanit"), int):
			if	state:

				air_lines	:List[List[str]]	= sanit["air_lines"]
				raw_lines	:List[str]			= sanit["raw_lines"]
				analysis	= {

					"coords":	defaultdict(lambda : defaultdict(int)),
					"alnums":	defaultdict(lambda : defaultdict(int)),
					"nums":		defaultdict(lambda : defaultdict(int)),
					"known":	defaultdict(lambda : defaultdict(int)),
					"unknown":	defaultdict(lambda : defaultdict(int)),
					"pending":	defaultdict(lambda : defaultdict(int)),
					"punct":	defaultdict(lambda : defaultdict(int)),
				}


				header, *body, eos = air_lines
				state  ^= (eos == [ "NNNN" ]) <<3
				scan	= word_scan(body)
				pend	= set()


				# SSN states for Station Subject Number - this is the information which any valid Navtex
				# message header must start with. Technically Navtex receiver will discard the whole
				# message if header is invalid. In following operation if only header is valid, SSN will
				# be extracted and putted in result dictionary with corresponding "state" shift.
				if	(SSN := self.is_valid_header(" ".join(header))) is not None:

					analysis["header"] = SSN
					state  |= 4


				for i,unmatch in scan[1]: analysis["punct"][i][unmatch] += 1
				for i in range(1,len(scan[0]) +1):


					line = scan[0][i]


					# Despite the fact DTG is optional for Navtex messages, it has common pattern, so once
					# such line is find it will be converted to "datetime" object and putted in result
					# dictionary. It is important, that if message somehow has a few DTG lines, result
					# dictionary will have only the last one. Also invalid DTG will be skipped.
					if	(match := G_MESSAGE_DTG.fullmatch(" ".join(line))):
						
						d,m,H,M,Y = match.group("day", "month", "hour", "minute", "year")

						Y = int(f"20{Y}") if Y else int(datetime.today().strftime("%Y"))
						m = MONTH_MAP[m]
						d = int(d)
						H = int(H)
						M = int(M)

						try:	analysis["DTG"] = datetime(Y,m,d,H,M)
						except:	pass
						else:	state |= 64


					for word in line:


						if		P_COORDINATE.fullmatch(word):		analysis["coords"][i][word]	+= 1
						elif	P_ALPHANUMERICAL.fullmatch(word):	analysis["alnums"][i][word]	+= 1
						elif	P_NUMERICAL.fullmatch(word):		analysis["nums"][i][word]	+= 1
						else:


							# At this point any value that mapped with "word" in "BoW" will be considered
							# as a flag whether this "word" is known/unknown/pending. If value is None,
							# which might be obtained directly from "BoW" if it is able to handle
							# nonexistent keys, or set after KeyError Exception caught, the "word"
							# considered as unknown. After an unknown "word" discovered, it is mapped
							# with 0 in "BoW" and also added to "pend" set, so all other occurrences
							# of "word" will be also treated as unknown. If "word" value is 0 and
							# it is not in "pend", it is considered pending. Any other values will
							# seam "word" is known.
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







