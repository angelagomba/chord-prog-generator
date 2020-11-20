import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.local_search import local_search
from Data.Keys.keys import Key

class LocalSearchTests(unittest.TestCase):

  def test_runnning(self):
    self.assertEqual(len(local_search(Key.C, True, 4, [])), 4)

if __name__ == '__main__':
    unittest.main()