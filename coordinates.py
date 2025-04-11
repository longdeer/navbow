import re








G_COORDINATE = re.compile(

	r"""
		(
			(\d\d\-\d\d(-\d\d)?(\.\d+)?N)
			|
			(\d\d\-\d\d(-\d\d)?(\.\d+)?S)
			|
			(\d\d\d\-\d\d(-\d\d)?(\.\d+)?W)
			|
			(\d\d\d\-\d\d(-\d\d)?(\.\d+)?E)
		)
		[,.:]?
	""",
	re.VERBOSE
)







