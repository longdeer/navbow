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
		"""

		if	isinstance(sanit := sanit_state(path), dict):
			state = sanit.get("sanit")


			if	isinstance(state, int) and state:


				raw_lines	= sanit["air_lines"]
				analysis	= {

					"coords":	defaultdict(lambda : defaultdict(int)),
					"alnums":	defaultdict(lambda : defaultdict(int)),
					"nums":		defaultdict(lambda : defaultdict(int)),
					"known":	defaultdict(lambda : defaultdict(int)),
					"unknown":	defaultdict(lambda : defaultdict(int)),
					"punc":		defaultdict(lambda : defaultdict(int)),
				}


				header, *body, eos = raw_lines
				state  ^= self.is_valid_header(" ".join(header)) <<2
				state  ^= (eos == [ "NNNN" ]) <<3
				scan	= word_scan(body)


				for line,unmatch in scan[1]: analysis["punc"][unmatch][line] += 1
				for line,word in scan[0]:


					if		P_COORDINATE.fullmatch(word):		analysis["coords"][word][line] += 1
					elif	P_ALPHANUMERICAL.fullmatch(word):	analysis["alnums"][word][line] += 1
					elif	P_NUMERICAL.fullmatch(word):		analysis["nums"][word][line] += 1
					else:

						try:	BoW_state = BoW[word]
						except:	BoW_state = 0
						match	BoW_state:

							case None | 0:

								analysis["unknown"][word][line] += 1
								state |= 1 <<5

							case _:

								analysis["known"][word][line] += 1
								state |= 1 <<4
				return {

					"state":	state,
					"lines":	raw_lines,
					"analysis":	analysis,
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







