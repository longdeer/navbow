import re








# Transmitter
# identification
# character				Transmission start times (UTC)
# (B1)
#
# A					0000	0400	0800	1200	1600	2000
# B					0010	0410	0810	1210	1610	2010
# C					0020	0420	0820	1220	1620	2020
# D					0030	0430	0830	1230	1630	2030
# E					0040	0440	0840	1240	1640	2040
# F					0050	0450	0850	1250	1650	2050
# G					0100	0500	0900	1300	1700	2100
# H					0110	0510	0910	1310	1710	2110
# I					0120	0520	0920	1320	1720	2120
# J					0130	0530	0930	1330	1730	2130
# K					0140	0540	0940	1340	1740	2140
# L					0150	0550	0950	1350	1750	2150
# M					0200	0600	1000	1400	1800	2200
# N					0210	0610	1010	1410	1810	2210
# O					0220	0620	1020	1420	1820	2220
# P					0230	0630	1030	1430	1830	2230
# Q					0240	0640	1040	1440	1840	2240
# R					0250	0650	1050	1450	1850	2250
# S					0300	0700	1100	1500	1900	2300
# T					0310	0710	1110	1510	1910	2310
# U					0320	0720	1120	1520	1920	2320
# V					0330	0730	1130	1530	1930	2330
# W					0340	0740	1140	1540	1940	2340
# X					0350	0750	1150	1550	1950	2350
#
# B2 Subject indicator character
#
# A = Navigational warnings
# B = Meteorological warnings
# C = Ice reports
# D = Search and rescue information, acts of piracy warnings, tsunamis and other natural phenomena
# E = Meteorological forecasts
# F = Pilot and VTS service messages
# G = AIS service messages (non-navigational aid)
# H = LORAN messages
# I = Currently not used
# J = GNSS messages regarding PRN status
# K = Other electronic navigational aid system messages
# L = Other navigational warnings – additional to B2 character A
# V = Special services allocation by the IMO NAVTEX Coordinating Panel
# W = Special services allocation by the IMO NAVTEX Coordinating Panel
# X = Special services allocation by the IMO NAVTEX Coordinating Panel
# Y = Special services allocation by the IMO NAVTEX Coordinating Panel
# Z = No message on hand
#
# Each message within each subject group is allocated a two digit sequential serial
# number beginning at 01 and ending at 99. The B3B4 message numbering characters together,
# are often referred to as the "NAVTEX number".
# The NAVTEX number is solely allocated as a component of the NAVTEX message
# identity and should not be confused with (and bears no correlation to) the series identity and
# consecutive number of the NAVAREA or Coastal warning contained in the message.
# Messages broadcast using NAVTEX number B3B4 = 00 cannot be rejected and will
# automatically override any selection of B1 transmitter identification characters as well as any B2
# subject indicator characters selected on the NAVTEX receiver.
# Use of NAVTEX number B3B4 = 00 must therefore be strictly controlled, since
# messages carrying it will always be printed or displayed every time they are received. Routine
# messages and service messages must never be allocated B3B4 = 00. The correct use of B2
# characters A, B, D and L will ensure that messages containing safety information will always
# be printed or displayed on first receipt.








G_NAVTEX_MESSAGE_HEADER = re.compile(r"^ZCZC (?P<tcB1>[A-X])(?P<tcB2>[A-LV-Z])(?P<tcB34>\d\d)$")







