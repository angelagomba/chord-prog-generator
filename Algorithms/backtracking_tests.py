import unittest
import os
import sys
os.path.join(".")
from backtracking import backtracking

class LocalSearchTests(unittest.TestCase):

  def test_runnning(self):
    self.assertEqual(backtracking("C", 4, []), None)

if __name__ == '__main__':
    unittest.main()