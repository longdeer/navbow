import	unittest
from	NavtexBoWAnalyzer.header import B1
from	NavtexBoWAnalyzer.header import B2
from	NavtexBoWAnalyzer.header import G_NAVTEX_MESSAGE_HEADER








class HeaderCase(unittest.TestCase):

	def test_valid_station_A(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC A{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "A")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_B(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC B{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "B")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_C(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC C{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "C")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_D(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC D{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "D")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_E(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC E{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "E")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_F(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC F{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "F")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_G(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC G{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "G")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_H(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC H{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "H")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_I(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC I{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "I")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_J(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC J{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "J")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_K(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC K{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "K")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_L(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC L{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "L")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_M(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC M{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "M")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_N(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC N{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "N")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_O(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC O{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "O")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_P(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC P{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "P")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_Q(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC Q{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "Q")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_R(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC R{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "R")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_S(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC S{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "S")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_T(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC T{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "T")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_U(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC U{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "U")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_V(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC V{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "V")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_W(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC W{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "W")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)

	def test_valid_station_X(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC X{subj}{B34}"

					with self.subTest(header=current):

						match = G_NAVTEX_MESSAGE_HEADER.fullmatch(current)
						tcB1, tcB2, tcB34 = match.group("tcB1", "tcB2", "tcB34")

						self.assertEqual(tcB1, "X")
						self.assertEqual(tcB2, subj)
						self.assertEqual(tcB34,B34)




	def test_invalid_station_Y(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC Y{subj}{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_invalid_station_Z(self):

		for subj in B2:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC Z{subj}{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))




	def test_unused_subject_M(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}M{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_N(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}N{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_O(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}O{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_P(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}P{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_Q(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}Q{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_R(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}R{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_S(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}S{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_T(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}T{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))

	def test_unused_subject_U(self):

		for station in B1:
			for i in range(10):
				for j in range(10):

					B34 = f"{i}{j}"
					current = f"ZCZC {station}U{B34}"

					with self.subTest(invalid=current):
						self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))




	def test_invalid_numbering(self):

		for station in B1:
			for sub in B2:
				for i in range(10):
					for B34 in f"{i}{station}", f"{station}{i}":

						current = f"ZCZC {station}{sub}{B34}"

						with self.subTest(invalid=current):
							self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(current))




	def test_invalid_form(self):

		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch(""))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("Z"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("ZC"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("ZCZ"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("ZCZC"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("ZCZCC"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("CZCZC"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("ZCZCKB00"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("ZCZC KB 00"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("Z CZC KB00"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("Z C ZC KB00"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("Z C Z C KB00"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("Z C Z C K B00"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("Z C Z C K B 00"))
		self.assertIsNone(G_NAVTEX_MESSAGE_HEADER.fullmatch("Z C Z C K B 0 0"))








if __name__ == "__main__" : unittest.main(verbosity=2)







