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
from NavtexBoWAnalyzer.scanner			import sanit_scan








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

	def __init__(self, station :str, BoW :Dict[str,int]):

		assert isinstance(BoW, dict), f"Uncompatible bag of words type {type(BoW)}"
		assert (

			isinstance(station,str) and len(station) == 1 and station.upper() in B1
		),	f"Invalid station literal {station}"

		self.station = station.upper()
		self.BoW = BoW

	def __call__(self, path :str) -> Dict[str,int|Set[str]|List[str]] | None :

		if	(sanit := sanit_scan(path)) is not None:

			coords	= set()
			nums	= set()
			alnums	= set()
			known	= set()
			unknown	= set()
			lines	= sanit["air_lines"]
			words	= sanit["chunks"]
			state	= sanit["sanit"]
			header, *_, eos	= lines
			state  ^= self.is_valid_header(" ".join(header)) <<2
			state  ^= (eos == [ "NNNN" ]) <<3


			for word in words:

				if		P_COORDINATE.fullmatch(word):		coords.add(word)
				elif	P_ALPHANUMERICAL.fullmatch(word):	alnums.add(word)
				elif	P_NUMERICAL.fullmatch(word):		nums.add(word)

				else:

					match self.BoW_state(word):

						case 1:

							known.add(word)
							state |= 1 <<4

						case 0:

							unknown.add(word)
							state |= 1 <<5


			return {

				"state":	state,
				"coords":	coords,
				"nums":		nums,
				"alnums":	alnums,
				"known":	known,
				"unknown":	unknown,
				"lines":	lines,
			}




	def is_valid_header(self, header :str) -> bool :

		"""
			Helper method that will try to extract a B1 from the "header" string and return True
			if it is the same letter than "station" field, obtained in initiation time. Returns
			False in any other cases, including Exception raises.
		"""

		try:	return G_NAVTEX_MESSAGE_HEADER.fullmatch(header).group("tcB1") == self.station
		except:	return False




	def BoW_state(self, word :str) -> Literal[0|1] | None :

		"""
			Helper method that implements inspection of "BoW". If "word" mapped with anything in
			"BoW" it will be converted to 0 or 1, depending is it mapped with zero or not. That means
			the "word state" in BoW always evaluates as 0, either "word" not in "BoW" or it's mapping
			is 0, or as 1 in case of any other than 0 mapping.
		"""

		if	isinstance(state := self.BoW.get(word,0), int):
			if state == 0 : return 0
		return 1







