import	unittest
from	NavtexBoWAnalyzer.coordinates import P_COORDINATE








class CoordinatesCase(unittest.TestCase):

	def test_valid_SN(self):

		for d in range(91):
			for m in range(60):
				for s in range(60):

					D = str(d).zfill(2)
					M = str(m).zfill(2)
					S = str(s).zfill(2)

					self.assertTrue(P_COORDINATE.fullmatch(f"{D}N"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}.99N"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}N"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}.99N"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}N"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99N"))

					self.assertTrue(P_COORDINATE.fullmatch(f"{D}S"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}.99S"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}S"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}.99S"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}S"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99S"))


	def test_valid_EW(self):

		for d in range(181):
			for m in range(60):
				for s in range(60):

					D = str(d).zfill(3)
					M = str(m).zfill(2)
					S = str(s).zfill(2)

					self.assertTrue(P_COORDINATE.fullmatch(f"{D}E"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}.99E"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}E"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}.99E"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}E"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99E"))

					self.assertTrue(P_COORDINATE.fullmatch(f"{D}W"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}.99W"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}W"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}.99W"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}W"))
					self.assertTrue(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99W"))


	def test_invalid_SN(self):

		for d in range(91,110):
			for m in range(60,110):
				for s in range(60,110):

					D = str(d).zfill(2)
					M = str(m).zfill(2)
					S = str(s).zfill(2)

					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}N"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}.99N"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}N"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}.99N"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}N"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99N"))

					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}S"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}.99S"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}S"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}.99S"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}S"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99S"))


	def test_invalid_EW(self):

		for d in range(181,200):
			for m in range(60,110):
				for s in range(60,110):

					D = str(d).zfill(3)
					M = str(m).zfill(2)
					S = str(s).zfill(2)

					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}E"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}.99E"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}E"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}.99E"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}E"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99E"))

					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}W"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}.99W"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}W"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}.99W"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}W"))
					self.assertIsNone(P_COORDINATE.fullmatch(f"{D}-{M}-{S}.99W"))








if	__name__ == "__main__" : unittest.main(verbosity=2)







