







def has_invalid_bytes(path :str) -> str | None :

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







