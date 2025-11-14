from typing						import List
from typing						import Dict
from typing						import Tuple
from datetime					import datetime
from collections				import defaultdict
from pathlib					import Path
from analyzer.header			import B1
from analyzer.header			import G_NAVTEX_MESSAGE_HEADER
from analyzer.coordinates		import P_COORDINATE
from analyzer.numerical			import P_NUMERICAL
from analyzer.alphanumerical	import P_ALPHANUMERICAL
from analyzer.DTG				import G_MESSAGE_DTG
from analyzer.DTG				import MONTH_MAP
from analyzer.scanner			import sanit_state
from analyzer.scanner			import word_scan
from server.db					import db_analysis_check








class NavtexAnalyzer:

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

		Also will maintain message "state" which will reflect details.
	"""

	def __init__(self, station :str):

		assert (

			isinstance(station,str) and len(station) == 1 and station.upper() in B1
		),	f"Invalid station literal {station}"

		self.station = station.upper()

	def __call__(self, target :str | Path | bytes) -> Dict[str,int|List|Dict] | None :

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
				33	- message without header, EoS, DTG, with unknown word;
				35	- sanitized message without header, EoS, DTG, with unknown word;
				37	- message without EoS, DTG, with unknown word;
				39	- sanitized message without EoS, DTG, with unknown word;
				41	- message without header, DTG, with unknown word;
				43	- sanitized message without header, DTG, with unknown word;
				45	- message without DTG, with unknown word;
				47	- sanitized message without DTG, with unknown word;
				49	- message without header, EoS, DTG, with known and unknown words;
				51	- sanitized message without header, EoS, DTG, with known and unknown words;
				53	- message without EoS, DTG, with known and unknown words;
				55	- sanitized message without EoS, DTG, with known and unknown words;
				57	- message without header, DTG, with known and unknown words;
				59	- sanitized message without header, DTG, with known and unknown words;
				61	- message without DTG, with known and unknown words;
				63	- sanitized message without DTG, with known and unknown words;
				81	- message without header, EOS, with known word;
				83	- sanitized message without header, EOS, with known word;
				85	- message without EOS, with known word;
				87	- sanitized message without EOS, with known word;
				89	- message without header, with known word;
				91	- sanitized message without header, with known word;
				93	- message with known word;
				95	- sanitized message with known word;
				97	- message without header, EoS, with unknown word;
				99	- sanitized message without header, EoS, with unknown word;
				101	- message without EoS, with unknown word;
				103	- sanitized message without EoS, with unknown word;
				105	- message without header, with unknown word;
				107	- sanitized message without header, with unknown word;
				109	- message with unknown word;
				111	- sanitized message with unknown word;
				113	- message without header, EoS, with known and unknown words;
				115	- sanitized message without header, EoS, with known and unknown words;
				117	- message without EoS, with known and unknown words;
				119	- sanitized message without EoS, with known and unknown words;
				121	- message without header, with known and unknown words;
				123	- sanitized message without header, with known and unknown words;
				125	- message with known and unknown words;
				127	- sanitized message with known and unknown words;

			"sanit_state" might obtain False "broken" state from "byte_scan", but the message
			will not content any valid symbols. In this case, "sanit_state" will return full dictionary,
			but invocation due to zero "state" will try to return dictionary with "message" key, which
			is not present in "sanit_state" return value, so it will be None. All unknown words will be
			mapped in "BoW" with 0, so "BoW" will be eventually altered. "BoW" will be checked to be a
			Mapping type, but very easy. If "BoW" is not a mapping, "analysis" will have empty "unknown"
			and "known" dictionaries, and "state" will reflect it in 65-71 range. Return value is a
			dictionary, which might be of two types:
				state, message - for the "corrupted" files;
				state, analysis, raw, air - all other cases.
		"""

		if	isinstance(sanit := sanit_state(target), dict) and isinstance(state := sanit.get("sanit"), int):
			if	state:

				air_lines	:List[List[str]]	= sanit["air_lines"]
				raw_lines	:List[str]			= sanit["raw_lines"]
				analysis	= {

					"coords":	defaultdict(lambda : defaultdict(int)),
					"alnums":	defaultdict(lambda : defaultdict(int)),
					"nums":		defaultdict(lambda : defaultdict(int)),
					"known":	defaultdict(lambda : defaultdict(int)),
					"unknown":	defaultdict(lambda : defaultdict(int)),
					"punct":	defaultdict(lambda : defaultdict(int)),
				}


				header, *body, eos = air_lines
				state  ^= (eos == [ "NNNN" ]) <<3
				scan	= word_scan(body)
				pend	= defaultdict(list)


				# SSN states for Station Subject Number - this is the information which any valid Navtex
				# message header must start with. Technically Navtex receiver will discard the whole
				# message if header is invalid. In following operation if only header is valid, SSN will
				# be extracted and putted in result dictionary with corresponding "state" shift.
				if	(SSN := self.validate_header(" ".join(header))) is not None:

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


						if		P_COORDINATE.fullmatch(word): analysis["coords"][i][word]		+= 1
						elif	P_ALPHANUMERICAL.fullmatch(word): analysis["alnums"][i][word]	+= 1
						elif	P_NUMERICAL.fullmatch(word): analysis["nums"][i][word]			+= 1
						else:	pend[word].append(i)


				pending_words = set(pend.keys())
				known = db_analysis_check(pending_words)
				unknown = pending_words - known


				for word in known:
					for i in pend[word]:

						analysis["known"][i][word] += 1
						state |= 16

				for word in unknown:
					for i in pend[word]:

						analysis["unknown"][i][word] += 1
						state |= 32


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




	def validate_header(self, header :str) -> Tuple[str,str,str] | None :

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







