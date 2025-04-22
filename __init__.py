from typing								import List
from typing								import Dict
from typing								import Tuple
from collections						import defaultdict
from NavtexBoWAnalyzer.header			import B1
from NavtexBoWAnalyzer.header			import B2
from NavtexBoWAnalyzer.header			import G_NAVTEX_MESSAGE_HEADER
from NavtexBoWAnalyzer.coordinates		import P_COORDINATE
from NavtexBoWAnalyzer.numerical		import P_NUMERICAL
from NavtexBoWAnalyzer.cdt				import G_MESSAGE_CDT
from NavtexBoWAnalyzer.alphanumerical	import P_ALPHANUMERICAL
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
	"""

	def __init__(self, station :str):

		assert (

			isinstance(station,str) and len(station) == 1 and station.upper() in B1
		),	f"Invalid station literal {station}"

		self.station = station.upper()

	def with_mapping(self, path :str, BoW :Dict[str,int]) -> Dict[str,int|List|Dict] :

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
			33	- message without header, EoS, CDT, with unknown word;
			35	- sanitized message without header, EoS, CDT, with unknown word;
			37	- message without EoS, CDT, with unknown word;
			39	- sanitized message without EoS, CDT, with unknown word;
			41	- message without header, CDT, with unknown word;
			43	- sanitized message without header, CDT, with unknown word;
			45	- message without CDT, with unknown word;
			47	- sanitized message without CDT, with unknown word;
			49	- message without header, EoS, CDT, with known and unkown words;
			51	- sanitized message without header, EoS, CDT, with known and unkown words;
			53	- message without EoS, CDT, with known and unkown words;
			55	- sanitized message without EoS, CDT, with known and unkown words;
			57	- message without header, CDT, with known and unkown words;
			59	- sanitized message without header, CDT, with known and unkown words;
			61	- message without CDT, with known and unkown words;
			63	- sanitized message without CDT, with known and unkown words;

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
			97	- message without header, EoS, with unkown word;
			99	- sanitized message without header, EoS, with unkown word;
			101	- message without EoS, with unkown word;
			103	- sanitized message without EoS, with unkown word;
			105	- message without header, with unkown word;
			107	- sanitized message without header, with unkown word;
			109	- message with unkown word;
			111	- sanitized message with unkown word;
			113	- message without header, EoS, with known and unkown words;
			115	- sanitized message without header, EoS, with known and unkown words;
			117	- message without EoS, with known and unkown words;
			119	- sanitized message without EoS, with known and unkown words;
			121	- message without header, with known and unkown words;
			123	- sanitized message without header, with known and unkown words;
			125	- message with known and unkown words;
			127	- sanitized message with known and unkown words;
		"""

		if	isinstance(sanit := sanit_state(path), dict):
			state = sanit.get("sanit")


			if	isinstance(state, int) and state:


				raw_lines	= sanit["raw_lines"]
				air_lines	= sanit["air_lines"]
				analysis	= {

					"coords":	defaultdict(lambda : defaultdict(int)),
					"alnums":	defaultdict(lambda : defaultdict(int)),
					"nums":		defaultdict(lambda : defaultdict(int)),
					"known":	defaultdict(lambda : defaultdict(int)),
					"unknown":	defaultdict(lambda : defaultdict(int)),
					"punc":		defaultdict(lambda : defaultdict(int)),
				}


				header, *body, eos = air_lines
				state  ^= self.is_valid_header(" ".join(header)) <<2
				state  ^= (eos == [ "NNNN" ]) <<3
				scan	= word_scan(body)


				for line,unmatch in scan[1]: analysis["punc"][unmatch][line] += 1
				for i in range(1,len(scan[0]) +1):


					line = scan[0][i]
					state |= bool(G_MESSAGE_CDT.fullmatch(" ".join(line))) <<6


					for word in line:


						if		P_COORDINATE.fullmatch(word):		analysis["coords"][word][i] += 1
						elif	P_ALPHANUMERICAL.fullmatch(word):	analysis["alnums"][word][i] += 1
						elif	P_NUMERICAL.fullmatch(word):		analysis["nums"][word][i] += 1
						else:


							try:	BoW_state = BoW[word]
							except:	BoW_state = 0
							match	BoW_state:

								case None | 0:

									analysis["unknown"][word][i] += 1
									state |= 1 <<5

								case _:

									analysis["known"][word][i] += 1
									state |= 1 <<4
				return {

					"analysis":	analysis,
					"state":	state,
					"air":		air_lines,
					"raw":		raw_lines,
				}
			return	{

				"message":	sanit.get("message"),
				"state":	state,
			}




	def is_valid_header(self, header :str) -> bool :

		"""
			Helper method that will try to extract a B1 from the "header" string and return True
			if it is the same letter than "station" field, obtained in initiation time. Returns
			False in any other cases, including Exception raises.
		"""

		try:	return G_NAVTEX_MESSAGE_HEADER.fullmatch(header).group("tcB1") == self.station
		except:	return False







