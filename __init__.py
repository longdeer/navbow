from typing								import Set
from typing								import List
from typing								import Dict
from typing								import Literal
from NavtexBoWAnalyzer.header			import B1
from NavtexBoWAnalyzer.header			import B2
from NavtexBoWAnalyzer.header			import G_NAVTEX_MESSAGE_HEADER
from NavtexBoWAnalyzer.coordinates		import P_COORDINATE
from NavtexBoWAnalyzer.numerical		import P_NUMERICAL
from NavtexBoWAnalyzer.alphanumerical	import P_ALPHANUMERICAL
from NavtexBoWAnalyzer.scanner			import sanit_state








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

	def with_mapping(self, path :str, BoW :Dict[str,int]) -> Dict[str,int|Set[str]|List[str]] | None :

		"""
			Ananlysis implementation that uses dictionary 
		"""

		# assert isinstance(BoW, dict), f"Uncompatible bag of words type {type(BoW)}"

		if	isinstance(sanit := sanit_state(path), dict):
			state = sanit.get("sanit")

			if	isinstance(state, int) and state:

				coords	= set()
				nums	= set()
				alnums	= set()
				known	= set()
				unknown	= set()
				lines	= sanit["air_lines"]
				words	= sanit["chunks"]
				header, *_, eos	= lines
				state  ^= self.is_valid_header(" ".join(header)) <<2
				state  ^= (eos == [ "NNNN" ]) <<3


				for word in words:

					if		P_COORDINATE.fullmatch(word):		coords.add(word)
					elif	P_ALPHANUMERICAL.fullmatch(word):	alnums.add(word)
					elif	P_NUMERICAL.fullmatch(word):		nums.add(word)
					else:

						try:	BoW_state = BoW[word]
						except:	BoW_state = 0
						match	BoW_state:

							case None | 0:

								unknown.add(word)
								state |= 1 <<5

							case _:

								known.add(word)
								state |= 1 <<4
				return {

					"state":	state,
					"coords":	coords,
					"nums":		nums,
					"alnums":	alnums,
					"known":	known,
					"unknown":	unknown,
					"lines":	lines,
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







