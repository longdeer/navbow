import re








# Regular expression that allows filtering possible words, that are formed only by integers with
# possible separation by:
#	"-" - for range designation;
#	"." - for floating point number designation;
#	"," - for floating point number designation;
#	"/" - for some sort of ordering notation;
#	":" - for special numbering notation.
# The following tools are only suggestion for Navtex messages processing, which general purpose is
# filtering out determined information and attract attention to controversial moments.
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







