import re








# Following ASCII symbols in lexigraphical order were determined as allowed for Navtex messages content
NAVTEX_SYMBOLS = "'()+,-./0123456789:=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S_NAVTEX_SYMBOLS = set(NAVTEX_SYMBOLS)
G_NAVTEX_WORD = re.compile(r"[\('('\()(\(')]?(?P<word>[^\(\)]+)[\)'(\)')('\))]?")







