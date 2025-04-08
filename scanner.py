from typing import List
from typing import Dict








def byte_scan(path :str) -> str | None :

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








def state_scan(path :str) -> Dict[str,int|str|List[str]] :

	"""
		Scans message in utf-8 mode (after byte_scan) and disassembles it to:
			- raw_lines, unmodified strings obtained after NL split;
			- hot_lines, fully sanitized proper strings;
			- chunks, set of strings (every word);
			- symbols, all non-whitespace symbols.
		Also maintains a "state" integer that is:
			- zero at start;
			- has first bit set for any proper "hot_line";
			- has second bit set for any proper "hot_line" and corresponding "raw" line inequality.
		Returns the dictionary of mentioned key-value pairs, or None if any Exceptions caught.
	"""

	state		= 0
	chunks		= set()
	symbols		= set()
	raw_lines	= list()
	hot_lines	= list()

	try:

		with open(path) as file:
			for line in file:

				raw = line.rstrip("\n")
				raw_lines.append(raw)
				hot = list()

				if	(split := raw.split()):
					for word in split:

						current = word.upper()
						hot.append(current)
						chunks.add(current)

						for char in current : symbols.add(char)

					hot_line = " ".join(hot)
					hot_lines.append(hot_line)
					state |= (hot_line != raw) <<1
					state |= 1

	except:	return
	else:	return {

		"raw_lines":	raw_lines,
		"hot_lines":	hot_lines,
		"symbols":		symbols,
		"chunks":		chunks,
		"state":		state,
	}







