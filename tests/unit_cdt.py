import	unittest
from	datetime				import datetime
from	NavtexBoWAnalyzer.cdt	import G_MESSAGE_CDT








class CDTCase(unittest.TestCase):

	def test_JAN_CDT(self):

		for d in range(1,32):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,1,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC JAN")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"JAN")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC JAN 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"JAN")
					self.assertEqual(year,"25")


	def test_FEB_CDT(self):

		for d in range(1,29):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,2,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC FEB")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"FEB")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC FEB 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"FEB")
					self.assertEqual(year,"25")


	def test_MAR_CDT(self):

		for d in range(1,32):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,3,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC MAR")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"MAR")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC MAR 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"MAR")
					self.assertEqual(year,"25")


	def test_APR_CDT(self):

		for d in range(1,31):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,4,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC APR")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"APR")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC APR 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"APR")
					self.assertEqual(year,"25")


	def test_MAY_CDT(self):

		for d in range(1,32):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,5,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC MAY")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"MAY")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC MAY 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"MAY")
					self.assertEqual(year,"25")


	def test_JUN_CDT(self):

		for d in range(1,31):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,6,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC JUN")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"JUN")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC JUN 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"JUN")
					self.assertEqual(year,"25")


	def test_JUL_CDT(self):

		for d in range(1,32):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,7,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC JUL")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"JUL")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC JUL 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"JUL")
					self.assertEqual(year,"25")


	def test_AUG_CDT(self):

		for d in range(1,32):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,8,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC AUG")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"AUG")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC AUG 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"AUG")
					self.assertEqual(year,"25")


	def test_SEP_CDT(self):

		for d in range(1,31):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,9,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC SEP")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"SEP")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC SEP 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"SEP")
					self.assertEqual(year,"25")


	def test_OCT_CDT(self):

		for d in range(1,32):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,10,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC OCT")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"OCT")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC OCT 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"OCT")
					self.assertEqual(year,"25")


	def test_NOV_CDT(self):

		for d in range(1,31):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,11,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC NOV")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"NOV")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC NOV 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"NOV")
					self.assertEqual(year,"25")


	def test_DEC_CDT(self):

		for d in range(1,32):
			for h in range(24):
				for m in range(60):

					D = str(d).zfill(2)
					H = str(h).zfill(2)
					M = str(m).zfill(2)

					self.assertTrue(datetime(2025,12,d,h,m))

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC DEC")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"DEC")
					self.assertIsNone(year)

					match = G_MESSAGE_CDT.fullmatch(f"{D}{H}{M} UTC DEC 25")
					day, hour, minute, month, year = match.group("day", "hour", "minute", "month", "year")
					self.assertEqual(day,D)
					self.assertEqual(hour,H)
					self.assertEqual(minute,M)
					self.assertEqual(month,"DEC")
					self.assertEqual(year,"25")








if	__name__ == "__main__" : unittest.main(verbosity=2)







