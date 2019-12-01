import unittest

# Das Modul schiffe_versenken muss importierbar werden, daher suchen wir seinen Pfad manuell 
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from schiffe_versenken.schiff import Schiff

class TesteSchiff(unittest.TestCase):
    def setUp(self):
        self.schiff = Schiff(1)

    def test_laenge(self):
        self.assertEqual(1, self.schiff.laenge)


unittest.main(argv=[''], verbosity=2, exit=False)
