import re








# Bellow is the group pattern regular expression, that allows to extract Date Time Group information,
# in the way it is defined in "NAVTEX MANUAL". As Date Time Group defined as optional message content,
# the following is the default format which is used by stations (according to messages archive at
# https://www.navtex.net/navtex-archive.html) and represents the following information:
#   2 digits day designation
#   | 2 digits hour designation
#   | | 2 digits minutes designation
#   | | |   Coordinated Universal Time use designation
#   | | |   |   3 letters month designation (ISO abbreviation)
#   | | |   |   |   2 digits year designation (optional)
#   | | |   |   |   |
#	DDHHMM UTC MMM YY
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







