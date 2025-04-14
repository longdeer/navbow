import re








G_NUMERICAL = re.compile(

	r"""
		\(?				# possible parenthesizing at the beginning
		\d+				# main integer part
		(				#
			[\-\.,:/]	# possible syntax addition
			\d+			# possible integer part two
		)*				#
		\)?				# possible parenthesizing at the end
		[\-\.,:]?		# possible syntax ending
	""",
	re.VERBOSE
)







