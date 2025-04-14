from NavtexBoWAnalyzer.header			import B1
from NavtexBoWAnalyzer.header			import B2
from NavtexBoWAnalyzer.header			import G_NAVTEX_MESSAGE_HEADER
from NavtexBoWAnalyzer.coordinates		import G_COORDINATE
from NavtexBoWAnalyzer.numerical		import G_NUMERICAL
from NavtexBoWAnalyzer.alphanumerical	import G_ALPHANUMERICAL
from NavtexBoWAnalyzer.scanner			import byte_scan
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

	def __init__(self, station :str):

		self.station = station.upper()
		assert self.station in B1, "Invalid station literal"








if	__name__ == "__main__":

	import	os
	import	re
	from	shutil						import copyfile
	from	collections					import defaultdict
	from	pygwarts.hagrid.walks		import fstree

	ROOT	= ""
	FOLDER1	= ""
	FOLDER2	= ""
	FOLDER3	= ""
	FOLDER4	= ""
	FOLDER5	= ""
	SYMBOLS	= set()
	ARCHIVE = dict()
	WORDS	= defaultdict(int)
	BROKEN	= list()
	ERROR	= list()
	WRONGS	= list()
	ALPHAS	= defaultdict(int)
	NUMBS	= defaultdict(int)
	ALNUMBS	= defaultdict(int)
	OTHER	= defaultdict(int)
	COORD	= defaultdict(int)
	AWORD	= re.compile(r"\(?[A-Z]+[\-/]?[A-Z]+\)?[\-\.,:]?")

	for sprout in [ fstree(FOLDER1), fstree(FOLDER2), fstree(FOLDER3), fstree(FOLDER4), fstree(FOLDER5) ]:
		for branch, folders, files in sprout:
			for file in files:

				if (broken := byte_scan(file)) is not None : BROKEN.append(broken)
				else:

					name	= file.name
					current	= sanit_scan(file)
					message	= "\n".join(current["air_lines"])
					header	= current["air_lines"][0]
					eos		= current["air_lines"][-1]
					body	= current["chunks"] - set(header.split()) - { "NNNN" }

					if "*" in current["symbols"]: ERROR.append(message)
					elif(

						not G_NAVTEX_MESSAGE_HEADER.fullmatch(header)
						or
						not eos == "NNNN"
					):	WRONGS.append(message)
					elif(ARCHIVE.get(name) != message):

						ARCHIVE[name] = message
						SYMBOLS |= current["symbols"]
						good_path = os.path.join(ROOT, "good", os.path.relpath(file,ROOT))
						os.makedirs(os.path.dirname(good_path), exist_ok=True)
						with open(good_path, "w") as good_file : good_file.write(message)

						for chunk in body:
							WORDS[chunk] += 1

							if		G_COORDINATE.fullmatch(chunk): COORD[chunk] += 1
							elif	G_NUMERICAL.fullmatch(chunk): NUMBS[chunk] += 1
							elif	G_ALPHANUMERICAL.fullmatch(chunk): ALNUMBS[chunk] += 1
							elif	AWORD.fullmatch(chunk): ALPHAS[chunk] += 1
							else:	OTHER[chunk] += 1

				print(f"processed {file}")


	with open("", "w") as dump:

		print(f"{sorted(SYMBOLS)}", file=dump)
		print(file=dump)
		print(f"brokens:", file=dump)
		for broken in BROKEN : print("\n".join(broken), file=dump)
		print(file=dump)
		for word,f in sorted(WORDS.items(), key=lambda E : E[1], reverse=True):
			print(f"{word}: {f}", file=dump)

	with open("", "w") as dump:

		print(f"errors:", file=dump)
		for error in ERROR : print(error + "\n", file=dump)
		print(file=dump)

	with open("", "w") as dump:

		print(f"wrongs:\n", file=dump)
		for wrong in WRONGS : print(wrong + "\n", file=dump)
		print(file=dump)

	with open("", "w") as dump:

		for word,f in sorted(ALPHAS.items(), key=lambda E : E[1], reverse=True):
			print(f"{word}: {f}", file=dump)

	with open("", "w") as dump:

		for word,f in sorted(NUMBS.items(), key=lambda E : E[1], reverse=True):
			print(f"{word}: {f}", file=dump)

	with open("", "w") as dump:

		for word,f in sorted(ALNUMBS.items(), key=lambda E : E[1], reverse=True):
			print(f"{word}: {f}", file=dump)

	with open("", "w") as dump:

		for word,f in sorted(OTHER.items(), key=lambda E : E[1], reverse=True):
			print(f"{word}: {f}", file=dump)

	with open("", "w") as dump:

		for word,f in sorted(COORD.items(), key=lambda E : E[1], reverse=True):
			print(f"{word}: {f}", file=dump)







