from NavtexBoWAnalyzer.header import B1
from NavtexBoWAnalyzer.header import B2








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

		self.station = station.upper()
		assert self.station in B1, "Invalid station literal"







