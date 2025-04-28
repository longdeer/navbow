import re








MONTH_MAP = {

	"JAN":	1,
	"FEB":	2,
	"MAR":	3,
	"APR":	4,
	"MAY":	5,
	"JUN":	6,
	"JUL":	7,
	"AUG":	8,
	"SEP":	9,
	"OCT":	10,
	"NOV":	11,
	"DEC":	12
}
G_MESSAGE_DTG = re.compile(

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







