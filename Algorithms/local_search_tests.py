import unittest
import os
import sys
os.path.join(".")
from local_search import local_search

class LocalSearchTests(unittest.TestCase):

  def test_runnning(self):
    self.assertEqual(local_search("C", 4, []), "C")

if __name__ == '__main__':
    unittest.main()