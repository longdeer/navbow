import os
import sys

tests_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_root)
analyzer_root = os.path.join(project_root,"analyzer")
if project_root not in sys.path : sys.path.insert(0,project_root)
if analyzer_root not in sys.path : sys.path.insert(0,analyzer_root)

import	unittest
from	numerical import P_NUMERICAL








class NumericalCase(unittest.TestCase):

	def test_integers(self):

		for i in range(int(1E6)):
			self.assertTrue(P_NUMERICAL.fullmatch(f"{i}"))


	def test_dash(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}-{j}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}-{j}-{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}-{j}-{i}-{j}"))


	def test_coma(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(P_NUMERICAL.fullmatch(f"{i},{j}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i},{j},{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i},{j},{i},{j}"))


	def test_dot(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}.{j}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}.{j}.{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}.{j}.{i}.{j}"))


	def test_colon(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}:{j}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}:{j}:{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}:{j}:{i}:{j}"))


	def test_slash(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}/{j}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}/{j}/{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}/{j}/{i}/{j}"))


	def test_mix(self):

		for i in range(100):
			for j in range(100):

				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}-{j},{i}.{j}:{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}:{j}.{i},{j}-{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i},{j}-{i}:{j}.{i}"))
				self.assertTrue(P_NUMERICAL.fullmatch(f"{i}.{j}:{i}-{j},{i}"))








if __name__ == "__main__" : unittest.main(verbosity=2)







