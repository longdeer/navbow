from typing								import List
from typing								import Dict
from typing								import Tuple
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

	def with_mapping(self, path :str, BoW :Dict[str,int]) -> Dict[str,int|List[str]|Dict[str,List[str]]] :

		"""
			Ananlysis implementation that uses dictionary 
		"""

		if	isinstance(sanit := sanit_state(path), dict):
			state = sanit.get("sanit")

			if	isinstance(state, int) and state:
				analysis = {

					"known":	list(),
					"unknown":	list(),
					"coord":	list(),
					"nums":		list(),
					"alnums":	list(),
					"punc":		list(),
				}


				lines	= sanit["air_lines"]
				header, *body, eos	= lines
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
					"lines":	lines,
					"analysis":	analysis,
				}
			return	{

				"message":	sanit.get("message"),
				"state":	state,
			}




	def extract(self, lines :List[List[str]]) -> Tuple[List[Tuple[str,int]],List[Tuple[str,int]]] :

		"""
			[ extracted words ],[( unmatched punctuation, line index )]
		"""

		words = list()
		punct = list()
		stack = list()

		for i,line in enumerate(lines,1):
			for word in line:
				current = str()

				for char in word:
					match char:

						case ")":

							if stack and stack[-1][0] == "(" : stack.pop()
							else: stack.append(( char,i ))

						case "'":

							if stack and stack[-1][0] == "'" : stack.pop()
							else: stack.append(( char,i ))

						case "\"":

							if stack and stack[-1][0] == "\"": stack.pop()
							else: stack.append(( char,i ))


						case "(":	stack.append(( char,i ))
						case "'":	stack.append(( char,i ))
						case "\"":	stack.append(( char,i ))
						case _:		current += char

				words.append(( current,i ))
		return	words,punct + stack




	def is_valid_header(self, header :str) -> bool :

		"""
			Helper method that will try to extract a B1 from the "header" string and return True
			if it is the same letter than "station" field, obtained in initiation time. Returns
			False in any other cases, including Exception raises.
		"""

		try:	return G_NAVTEX_MESSAGE_HEADER.fullmatch(header).group("tcB1") == self.station
		except:	return False







