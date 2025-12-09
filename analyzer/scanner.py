from os				import access	as osaccess
from os				import path		as ospath
from os				import R_OK
from pathlib		import Path
from collections	import defaultdict
from functools		import partial
from typing			import Set
from typing			import List
from typing			import Dict
from typing			import Tuple








def word_scan(lines :List[List[str]]) -> Tuple[Dict[int,List[str]],List[Tuple[int,str]]] :

	"""
		Accepts list of lists of words, that represents message lines, and scans every single string
		to distinguish words and punctuation. Every opening brackets and quotes will be stripped
		by default no matter their matching, whenever closing unmatched will stay in final word.
		Coma and colon are treated like a word separation. One dot at the end of a word will be stripped,
		if word has more than one symbol. Returns tuple of two:
			- dictionary which is mapping of tuples line number with list of words;
			- list of tuples of two: line number and unmatched punctuation.
	"""

	scope = { ")":"(", "'":"'", "\"":"\"" }
	words = defaultdict(list)
	stack = list()


	for i,line in enumerate(lines,1):
		for word in line:
			current = list()


			for j,char in enumerate(word):
				match char:


					# Every punctuation that matched in stack will form a word
					# and pop the stack. Every unmatched will go in stack and
					# in word if "current" is not empty.
					case ")" | "'" | "\"":

						if	stack and stack[-1][1] == scope[char]:
							if	1 <len(current) and current[-1] == "." : current.pop()
							if	current:

								words[i].append(str().join(current))
								current = list()

							stack.pop()
						else:
							stack.append(( i,char ))
							if current : current.append(char)


					# Additional symbols that are treated like separators. If goes after stack closing,
					# will be just skipped. Otherwise coma and colon immediately separates a word.
					# If in sequence, every even char will go to "current" as a part of new word.
					case "," | ":" | "-" | "." if 0 <j and word[j-1] in scope: continue
					case "," | ":" if current:

						words[i].append(str().join(current))
						current = list()

					case "(":	stack.append(( i,char )) # Always count opening
					case _:		current.append(char)


			if 1 <len(current) and current[-1] == "." : current.pop()
			if current : words[i].append(str().join(current))


	return	words,stack








def decoder(B :bytes, tp :List[str], bp :List[bool], nlp :List[bool], crp :List[bool]) -> Tuple[str,bool]:

	"""
		Decoder for a single byte "B" as ASCII symbol. Successfully decoded bit will be added
		to string which "tp" points to. Any "\\n" or "\\r" or consecutive pair of "\\r" and "\\n"
		or "\\n" and "\\r" will be treated as single new line character "\\n". In case of fail with
		non-ASCII symbol, "*" will be added to "tp" pointer and False will be stored for "bp" pointer.
	"""

	try:

		match (symbol := B.decode("ascii")):

			case "\r" if nlp[0]:	nlp[0] = False
			case "\r" if crp[0]:	tp[0] += "\n"

			case "\n" if crp[0]:	crp[0] = False
			case "\n" if nlp[0]:	tp[0] += "\n"

			case "\r":				tp[0],crp[0] = tp[0] + "\n",True
			case "\n":				tp[0],nlp[0] = tp[0] + "\n",True

			case _ if crp[0]:		tp[0],crp[0] = tp[0] + symbol,False
			case _ if nlp[0]:		tp[0],nlp[0] = tp[0] + symbol,False
			case _:					tp[0] += symbol

	except:	tp[0],bp[0] = tp[0] + "*",True








def byte_scan(target :str | Path | bytes) -> Tuple[bool,str] :

	"""
		Reads "target" file path in byte mode or as already bytes object or a text string and
		recreates whole text. If any not ASCII symbol will be encountered, it will be substituted
		with "*" and "broken" flag will be set to True. Returns the tuple of "broken" flag and
		recreated text string. Empty "target" will produce ( False,"" ). Doesn't handle any
		possible Exceptions, but ensures "target" is either the text, accessible file path
		or a bytes object.
	"""

	NL		= [ False ]
	CR		= [ False ]
	text	= [ str() ]
	broken	= [ False ]

	match target:

		case str() | Path() if ospath.isfile(target) and osaccess(target, R_OK):

			with open(target, "rb") as file:
				while(B := file.read(1)): decoder(B, text, broken, NL, CR)

		case str():
			for B in map(partial(bytes, encoding="utf-8"), target): decoder(B, text, broken, NL, CR)

		case bytes():
			for B in map(lambda i : target[i:i+1],range(len(target))): decoder(B, text, broken, NL, CR)

		case _: return True,text[0]

	return broken[0],text[0]








def sanit_state(path :str | Path) -> Dict[str,int|Set|List] | None :

	"""
		Scans message with "byte_scan" and disassembles it to:
			- raw_lines, unmodified strings obtained after split to lines;
			- air_lines, fully sanitized proper strings of lines split;
			- chunks, set of strings (every word);
			- symbols, all non-whitespace symbols in the message.
		Also maintains a "sanit" state integer that is:
			- zero at start;
			- has first bit set if any proper line "proper" encountered;
			- has second bit set if any proper line "proper" and corresponding "raw" line
			inequality encountered.
		Returns the dictionary of mentioned key-value pairs in case of False value of "byte_scan"
		returned false broken flag, or a dictionary with zero "sanit" and "message" string from
		"byte_scan" otherwise.
	"""

	F,message	= byte_scan(path)
	sanit		= 0

	if	not F:

		raw_lines	= [ line for line in message.split("\n") ]
		air_lines	= list()
		symbols		= set()
		chunks		= set()


		for raw in raw_lines:
			if	raw and not raw.isspace() and not (air := list()):
				if	(split := raw.split()):
					for word in split:


						current = word.upper()
						air.append(current)
						chunks.add(current)


						for char in current : symbols.add(char)


					air_lines.append(air)
					sanit |= (" ".join(air) != raw) <<1
					sanit |= 1
		return	{

			"raw_lines":	raw_lines,
			"air_lines":	air_lines,
			"symbols":		symbols,
			"chunks":		chunks,
			"sanit":		sanit,
		}
	return	{

		"message":	message,
		"sanit":	sanit,
	}







