import re








# "NAVTEX NANUAL" does not explicitly restrict the use of geographic coordinates systems, but it is
# implicitly suggested (according to messages archive at https://www.navtex.net/navtex-archive.html)
# Degree-Minutes-Seconds system, so Navtex messages must include coordinates in following format:
#	DD-MM[.DECIMAL][-SS[.DECIMAL]](NS)
#	DDD-MM[.DECIMAL][-SS[.DECIMAL]](EW)
# The following tools are only suggestion for Navtex messages processing, which general purpose is
# filtering out determined information and attract attention to controversial moments.
P_COORDINATE = re.compile(

	r"""
		(
			(
				(
					([0-8]\d)|90					# 0-90 degrees north latitude
				)									# mandatory
				(
					\-[0-5]\d						# 0-59 minutes and/or seconds
				)									# optional
				{0,2}
				(
					\.\d+							# decimal part of floating point number
				)?									# optional
				N
			)
			|
			(
				(
					([0-8]\d)|90					# 0-90 degrees south latitude
				)									# mandatory
				(
					\-[0-5]\d						# 0-59 minutes and/or seconds
				)									# optional
				{0,2}
				(
					\.\d+							# decimal part of floating point number
				)?									# optional
				S
			)
			|
			(
				(
					(0\d\d)|(1[0-7]\d)|180			# 0-180 degrees west longitude
				)									# mandatory
				(
					\-[0-5]\d						# 0-59 minutes and/or seconds
				)									# optional
				{0,2}
				(
					\.\d+							# decimal part of floating point number
				)?									# optional
				W
			)
			|
			(
				(
					(0\d\d)|(1[0-7]\d)|180			# 0-180 degrees east longitude
				)									# mandatory
				(
					\-[0-5]\d						# 0-59 minutes and/or seconds
				)									# optional
				{0,2}
				(
					\.\d+							# decimal part of floating point number
				)?									# optional
				E
			)
		)
	""",
	re.VERBOSE
)







