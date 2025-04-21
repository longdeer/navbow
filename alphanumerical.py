import re








P_ALPHANUMERICAL = re.compile(

	r"""
		(
			(											# meters/miles/nautical
				[\d\-\.,]*\d+N?M(/S)?					# miles unit, possibly
			)											# decimal or range
			|
			(
				N\d+([\d\-\.,/]*\d+)*					# ordering number, possibly with formatting
			)
			|
			(
				(V?HF|MF|CH)\d+							# radio channel
			)
			|
			(
				\d+([\.,]\d+)?(-\d+([\.,]\d+)?)?[KM]?HZ	# radio frequency, possibly decimal or range
			)
		)
	""",
	re.VERBOSE
)







