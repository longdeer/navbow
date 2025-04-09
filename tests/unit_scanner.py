import	os
import	unittest
import	NavtexBoWAnalyzer
from	NavtexBoWAnalyzer.scanner import byte_scan








class SannerCase(unittest.TestCase):

	wd = os.path.join(NavtexBoWAnalyzer.__path__[0], "tests")

	def test_byte_scan_invalid(self):	self.assertIsNotNone(byte_scan(os.path.join(self.wd, "WZ29")))
	def test_byte_scan_valid(self):		self.assertIsNone(byte_scan(os.path.join(self.wd, "KA60")))








if	__name__ == "__main__" : unittest.main(verbosity=2)







