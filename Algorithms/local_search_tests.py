import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.local_search import LocalSearch
from Data.qualities import ChordQualities
from Data.keys import Key

class LocalSearchTests(unittest.TestCase):

  def test_chord_prog_simple(self):
    """
    Purpose: Ensures that the chord progression returned has the correct length.
    """
    ls = LocalSearch(Key.C, True, 4, [])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 4)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), 4)
  
  def test_chord_prog_complex_1(self):
    """
    """
    ls = LocalSearch(Key.C, True, 4, [ChordQualities.MIN7])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 4)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 4)

  def test_chord_prog_complex_2(self):
    """
    """
    ls = LocalSearch(Key.D, True, 4, [ChordQualities.MAJ7, ChordQualities.HALF_DIM])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 4)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 4)

  def test_chord_prog_complex_3(self):
    """
    """
    ls = LocalSearch(Key.C, True, 4, [ChordQualities.MIN7, ChordQualities.MAJ7, ChordQualities.DOM7])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 4)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 4)

  def test_chord_prog_complex_4(self):
    """
    """
    ls = LocalSearch(Key.A, True, 5, [ChordQualities.MIN7, ChordQualities.MAJ7])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 5)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 5)

if __name__ == '__main__':
    unittest.main()