import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.backtracking import backtracking
from Data.qualities import ChordQualities
from Data.keys import Key

class LocalSearchTests(unittest.TestCase):

  def test_runnning(self):
    # self.assertEqual(backtracking(Key.C, True, 4, []), None)
    print('res', backtracking(Key.C, True, 4, []))

if __name__ == '__main__':
    unittest.main()