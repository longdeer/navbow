import	unittest
from	NavtexBoWAnalyzer.alphanumerical import P_ALPHANUMERICAL








class AlphanumericalCase(unittest.TestCase):

	def test_MNM_units(self):

		for i in range(1,1001):
			for end in "",".",",",":":

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}M){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}M){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69M){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69M){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69M){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69M){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}M){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}M){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69M){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69M){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69M{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69M){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69M){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}NM){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}NM){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69NM){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69NM){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69NM){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69NM){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}NM){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}NM){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69NM){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69NM){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69NM{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69NM){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69NM){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}M/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}M/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69M/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69M/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69M/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69M/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}M/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}M/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69M/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69M/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69M/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69M/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69M/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}NM/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}NM/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69NM/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69NM/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69NM/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69NM/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{i+1}NM/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{i+1}NM/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.69-{i+1}.69NM/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.69-{i+1}.69NM/S){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69NM/S{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},69-{i+1},69NM/S){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},69-{i+1},69NM/S){end}"))


	def test_order_numbers(self):

		for i in range(1,1001):
			for end in "",".",",",":":

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}-{i+1}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}-{i+1}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}-{i+1}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}-{i+1}){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}.69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}/69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}/69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69-{i+1}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}.69-{i+1}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69-{i+1}.69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}.69-{i+1}.69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69-{i+1},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},69-{i+1},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69-{i+1},69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},69-{i+1},69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},/69-{i+1}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},/69-{i+1}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},/69-{i+1}/69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},/69-{i+1}/69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69-{i+1}.69-{i+3}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}.69-{i+1}.69-{i+3}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i}.69-{i+1}.69-{i+3}.69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i}.69-{i+1}.69-{i+3}.69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69-{i+1},69-{i+3},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},69-{i+1},69-{i+3},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},69-{i+1},69-{i+3},69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},69-{i+1},69-{i+3},69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},/69-{i+1}/69-{i+3}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},/69-{i+1}/69-{i+3}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"N{i},/69-{i+1}/69-{i+3}/69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(N{i},/69-{i+1}/69-{i+3}/69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}-{i+1}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}-{i+1}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}-{i+1}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}-{i+1}){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}.69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}.69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}/69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}/69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}.69-{i+1}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}.69-{i+1}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}.69-{i+1}.69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}.69-{i+1}.69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},69-{i+1},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},69-{i+1},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},69-{i+1},69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},69-{i+1},69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},/69-{i+1}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},/69-{i+1}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},/69-{i+1}/69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},/69-{i+1}/69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}.69-{i+1}.69-{i+3}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}.69-{i+1}.69-{i+3}.69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i}.69-{i+1}.69-{i+3}.69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i}.69-{i+1}.69-{i+3}.69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},69-{i+1},69-{i+3},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},69-{i+1},69-{i+3},69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},69-{i+1},69-{i+3},69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},69-{i+1},69-{i+3},69){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},/69-{i+1}/69-{i+3}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},/69-{i+1}/69-{i+3}/69{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"#{i},/69-{i+1}/69-{i+3}/69){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(#{i},/69-{i+1}/69-{i+3}/69){end}"))


	def test_channel_numbers(self):

		for i in range(1,1001):
			for end in "",".",",",":":

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"VHF{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(VHF{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"VHF{i}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(VHF{i}){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"HF{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(HF{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"HF{i}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(HF{i}){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"MF{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(MF{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"MF{i}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(MF{i}){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"CH{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(CH{i}{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"CH{i}){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"(CH{i}){end}"))


	def test_frequency(self):

		for i in range(2000,3000):
			for end in "",".",",",":":

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}-{(i+1)*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000}HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}-{(i+1)*1000}HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5-{(i+1)*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000}HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5-{(i+1)*1000}HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}-{(i+1)*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000}.5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}-{(i+1)*1000}.5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5-{(i+1)*1000}HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000}HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5-{(i+1)*1000}HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}-{(i+1)*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}-{(i+1)*1000},5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}-{(i+1)*1000},5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5-{(i+1)*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000}.5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5-{(i+1)*1000}.5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5-{(i+1)*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000},5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5-{(i+1)*1000},5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5-{(i+1)*1000}.5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000},5-{(i+1)*1000}.5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000},5-{(i+1)*1000}.5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5-{(i+1)*1000},5HZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i*1000}.5-{(i+1)*1000},5HZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i*1000}.5-{(i+1)*1000},5HZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{(i+1)}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)}KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{(i+1)}KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5-{(i+1)}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)}KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5-{(i+1)}KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{(i+1)}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)}.5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{(i+1)}.5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5-{(i+1)}KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)}KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5-{(i+1)}KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{(i+1)},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}-{(i+1)},5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}-{(i+1)},5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5-{(i+1)}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)}.5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5-{(i+1)}.5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5-{(i+1)},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)},5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5-{(i+1)},5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5-{(i+1)}.5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i},5-{(i+1)}.5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i},5-{(i+1)}.5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5-{(i+1)},5KHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i}.5-{(i+1)},5KHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i}.5-{(i+1)},5KHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}-{(i+1)//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000}MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}-{(i+1)//1000}MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5-{(i+1)//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000}MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5-{(i+1)//1000}MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}-{(i+1)//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000}.5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}-{(i+1)//1000}.5MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5-{(i+1)//1000}MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000}MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5-{(i+1)//1000}MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}-{(i+1)//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}-{(i+1)//1000},5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}-{(i+1)//1000},5MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5-{(i+1)//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000}.5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5-{(i+1)//1000}.5MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5-{(i+1)//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000},5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5-{(i+1)//1000},5MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5-{(i+1)//1000}.5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000},5-{(i+1)//1000}.5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000},5-{(i+1)//1000}.5MHZ){end}"))

				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5-{(i+1)//1000},5MHZ{end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"{i//1000}.5-{(i+1)//1000},5MHZ){end}"))
				self.assertTrue(P_ALPHANUMERICAL.fullmatch(f"({i//1000}.5-{(i+1)//1000},5MHZ){end}"))








if	__name__ == "__main__" : unittest.main(verbosity=2)







