import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.local_search import LocalSearch
from Data.qualities import ChordQuality
from Data.keys import Key
from utils import parseChordProg

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
    ls = LocalSearch(Key.C, True, 4, [ChordQuality.MIN7])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 4)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 4)

  def test_chord_prog_complex_2(self):
    """
    """
    ls = LocalSearch(Key.D, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 4)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 4)

  def test_chord_prog_complex_3(self):
    """
    """
    ls = LocalSearch(Key.C, True, 5, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DOM7])
    try:
      ls.local_search()
      print(parseChordProg(ls.chord_prog))
      self.assertEqual(len(ls.chord_prog), 5)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 5)

  def test_chord_prog_complex_4(self):
    """
    """
    ls = LocalSearch(Key.A, True, 5, [ChordQuality.MIN7, ChordQuality.MAJ7])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 5)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 5)

  def test_chord_prog_complex_5(self):
    """
    """
    ls = LocalSearch(Key.G, True, 8, [ChordQuality.MIN7, ChordQuality.MAJ7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.local_search()
      self.assertEqual(len(ls.chord_prog), 8)
    except RecursionError:
      print('Unable to create chord prog')
      self.assertEqual(len(ls.chord_prog), 8)

if __name__ == '__main__':
    unittest.main()