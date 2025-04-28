import re








# Regular expression, that is a set of popular suggestions for concatenations of alphabetic and numerical
# symbols, which can form:
#	M/S or NM/S		- velocity designation;
#	N or NR			- numbering designation;
#	VHF or MF or CH	- channels numbers designation;
#	KHZ or MHZ		- GMDSS frequencies designation.
# The following tools are only suggestion for Navtex messages processing, which general purpose is
# filtering out determined information and attract attention to controversial moments.
P_ALPHANUMERICAL = re.compile(

	r"""
		(
			(											# meters/miles/nautical
				[\d\-\.,]*\d+N?M(/S)?					# miles unit, possibly
			)											# decimal or range
			|
			(
				NR?\d+([\d\-\.,/]*\d+)*					# ordering number, possibly with formatting
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







