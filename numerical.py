import re








P_NUMERICAL = re.compile(

	r"""
		\d+				# main integer part
		(				#
			[\-\.,:/]	# possible syntax addition
			\d+			# possible integer part two
		)*				#
	""",
	re.VERBOSE
)







