from pathlib	import Path
from typing		import Set
from typing		import List
from typing		import Dict








def byte_scan(path :str | Path) -> str | None :

	"""
		Reads "path" file in byte mode for validation.
		If any not utf-8 symbol will be encountered, recreates message, substituting such symbols
		with "*", and returns this string. Returns None otherwise, which must mean all symbols
		are utf-8 compatible.
	"""

	message = str()
	invalid = False

	with open(path, "rb") as file:
		while(B := file.read(1)):

			try:	message += B.decode()
			except:	message,invalid = message + "*",True

	if	invalid : return message








def sanit_scan(path :str | Path) -> Dict[str,int|Set[str]|List[str]] | None :

	"""
		Scans message in utf-8 mode (after byte_scan) and disassembles it to:
			- raw_lines, unmodified strings obtained after split to lines;
			- air_lines, fully sanitized proper strings of splitted lines;
			- chunks, set of strings (every word);
			- symbols, all non-whitespace symbols in the message.
		Also maintains a "sanit" state integer that is:
			- zero at start;
			- has first bit set if any proper line "proper" encountered;
			- has second bit set if any proper line "proper" and corresponding "raw" line
			inequality encountered.
		Returns the dictionary of mentioned key-value pairs, or None if any Exceptions caught.
	"""

	sanit		= 0
	chunks		= set()
	symbols		= set()
	raw_lines	= list()
	air_lines	= list()

	try:

		with open(path) as file:
			for line in file:

				raw = line.rstrip("\n")
				raw_lines.append(raw)
				air = list()

				if	(split := raw.split()):
					for word in split:

						current = word.upper()
						air.append(current)
						chunks.add(current)

						for char in current : symbols.add(char)

					proper = " ".join(air)
					air_lines.append(proper)
					sanit |= (proper != raw) <<1
					sanit |= 1

	except:	return
	else:	return {

		"raw_lines":	raw_lines,
		"air_lines":	air_lines,
		"symbols":		symbols,
		"chunks":		chunks,
		"sanit":		sanit,
	}







