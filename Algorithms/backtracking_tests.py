import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.backtracking import backtracking
from Data.qualities import ChordQualities
from Data.keys import Key

class BacktrackingTests(unittest.TestCase):

  # def test_simple_chord_progs(self):
  #   print(len(backtracking(Key.C, True, 4, [])))

  def test_one_quality_chord_progs(self):
    print(backtracking(Key.C, True, 4, [ChordQualities.MAJ7, ChordQualities.MIN7, ChordQualities.DIM])[:4])

if __name__ == '__main__':
    unittest.main()