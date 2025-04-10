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








if	__name__ == "__main__":

	from collections				import defaultdict
	from pygwarts.hagrid.walks		import fstree
	from NavtexBoWAnalyzer.scanner	import byte_scan
	from NavtexBoWAnalyzer.scanner	import sanit_scan

	FOLDER	= ""
	SYMBOLS	= set()
	WORDS	= defaultdict(int)
	BROKEN	= list()

	for branch,folders,files in fstree(FOLDER):
		for file in files:

			if (broken := byte_scan(file)) is not None : BROKEN.append(broken)
			else:

				current  = sanit_scan(file)
				SYMBOLS |= current["symbols"]

				for chunk in current["chunks"]: WORDS[chunk] += 1

			print(f"processed {file}")


	with open("", "w") as dump:

		print(f"{sorted(SYMBOLS)}", file=dump)
		print(file=dump)
		for broken in BROKEN : print(broken, file=dump)
		print(file=dump)
		for word,f in sorted(WORDS.items(), key=lambda E : E[1], reverse=True):
			print(f"{word}: {f}", file=dump)







