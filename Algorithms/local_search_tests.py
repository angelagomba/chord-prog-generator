import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.local_search import LocalSearch
from Data.qualities import ChordQuality
from Data.keys import Key
from utils import parseChordProg

class LocalSearchTests(unittest.TestCase):

  #----------------------------------------------------------------------------------------------------------------
  # SIMPLE HILL CLIMBING
  #----------------------------------------------------------------------------------------------------------------
  def test_shc_no_qualities(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_shc_one_quality(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [ChordQuality.MIN7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_two_qualities(self):
    numChords = 4
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_three_qualities(self):
    numChords = 5
    ls = LocalSearch(Key.C, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DOM7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_five_qualities(self):
    numChords = 8
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.MAJ7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)
  
  #----------------------------------------------------------------------------------------------------------------
  # STEEPEST-ASCENT HILL CLIMBING
  #----------------------------------------------------------------------------------------------------------------
  def test_sahc_no_qualities(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_sahc_one_quality(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [ChordQuality.MIN7])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_two_qualities(self):
    numChords = 4
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_three_qualities(self):
    numChords = 5
    ls = LocalSearch(Key.C, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DOM7])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_five_qualities(self):
    numChords = 8
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.MAJ7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      prog = ls.steepest_ascent_hill_climbing()
      print(parseChordProg(prog))
      self.assertEqual(len(prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)
  
  #----------------------------------------------------------------------------------------------------------------
  # STOCHASTIC HILL CLIMBING
  #----------------------------------------------------------------------------------------------------------------
  def test_sthc_no_qualities(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_sthc_one_quality(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [ChordQuality.MIN7])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_two_qualities(self):
    numChords = 4
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_three_qualities(self):
    numChords = 5
    ls = LocalSearch(Key.C, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DOM7])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_five_qualities(self):
    numChords = 8
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.MAJ7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      prog = ls.stochastic_hill_climbing()
      print(parseChordProg(prog))
      self.assertEqual(len(prog), numChords)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

if __name__ == '__main__':
    unittest.main()