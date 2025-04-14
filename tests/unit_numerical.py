import	unittest
from	NavtexBoWAnalyzer.numerical import G_NUMERICAL








class NumericalCase(unittest.TestCase):

	def test_integers(self):

		for i in range(int(1E6)):

			self.assertTrue(G_NUMERICAL.fullmatch(f"{i}"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i}-"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i},"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i}."))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i}:"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i}"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i}-"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i},"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i}."))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i}:"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i})"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i})-"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i}),"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i})."))
			self.assertTrue(G_NUMERICAL.fullmatch(f"{i}):"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i})"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i})-"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i}),"))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i})."))
			self.assertTrue(G_NUMERICAL.fullmatch(f"({i}):"))

	def test_dash(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}-{j}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}-{j}-{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}-{j}-{i}-{j}"))

	def test_coma(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(G_NUMERICAL.fullmatch(f"{i},{j}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i},{j},{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i},{j},{i},{j}"))

	def test_dot(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}.{j}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}.{j}.{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}.{j}.{i}.{j}"))

	def test_colon(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}:{j}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}:{j}:{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}:{j}:{i}:{j}"))

	def test_slash(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}/{j}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}/{j}/{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}/{j}/{i}/{j}"))

	def test_mix(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}-{j},{i}.{j}:{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}:{j}.{i},{j}-{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i},{j}-{i}:{j}.{i}"))
				self.assertTrue(G_NUMERICAL.fullmatch(f"{i}.{j}:{i}-{j},{i}"))








if	__name__ == "__main__" : unittest.main(verbosity=2)







