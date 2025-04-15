import re








G_MESSAGE_CDT = re.compile(

	r"""
		(?P<day>[0-2]\d|3[01])
		(?P<hour>[01]\d|2[0-3])
		(?P<minute>[0-5]\d)
		\ UTC\ 
		(?P<month>JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)
		(\ (?P<year>\d\d))?
	""",
	re.VERBOSE
)







