import	unittest
from	NavtexBoWAnalyzer.alphanumerical import P_ALPHANUMERICAL








class AlphanumericalCase(unittest.TestCase):

	def test_MNM_units(self):

		for i in range(1,1001):

			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}M"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69M"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69M"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}M"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69M"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69M"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}NM"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69NM"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69NM"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}NM"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69NM"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69NM"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}M/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69M/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69M/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}M/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69M/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69M/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}NM/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69NM/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69NM/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}NM/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69NM/S"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69NM/S"))


	def test_order_numbers(self):

		for i in range(1,1001):

			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}-{i+1}"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}/69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69-{i+1}.69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69-{i+1},69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},/69-{i+1}/69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69-{i+1}.69-{i+3}.69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69-{i+1},69-{i+3},69"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},/69-{i+1}/69-{i+3}/69"))


	def test_channel_numbers(self):

		for i in range(1,1001):

			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"VHF{i}"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"HF{i}"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"MF{i}"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"CH{i}"))


	def test_frequency(self):

		for i in range(2000,3000):

			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000}HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000}HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000}.5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000}HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000},5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000}.5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000},5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000}.5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000},5HZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)}KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)}KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)}.5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)}KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)},5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)}.5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)},5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)}.5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)},5KHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000}MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000}MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000}.5MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000}MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000},5MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000}.5MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000},5MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000}.5MHZ"))
			self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000},5MHZ"))








if __name__ == "__main__" : unittest.main(verbosity=2)







