import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.backtracking import backtracking, backtrackingFC, backtrackingConflictSet, backtrackingGAC, backtrackingGACPre
from Data.qualities import ChordQuality
from Data.keys import Key
from Algorithms.utils import parseChordProg

class BacktrackingTests(unittest.TestCase):

  #----------------------------------------------------------------------------------------------------------------
  # NAIVE BACKTRACKING
  #----------------------------------------------------------------------------------------------------------------
  def test_simple_chord_progs(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [])), 1920)

  def test_one_quality_chord_progs(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [ChordQuality.MAJ7])), 1227)

  def test_three_quality_chord_progs(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])), 111)

  def test_four_quality_chord_progs(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])), 12)


  
  #----------------------------------------------------------------------------------------------------------------
  # FORWARD CHECKING
  #----------------------------------------------------------------------------------------------------------------

  def test_simple_chord_progs_fc(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 4, [])), 1920)

  def test_three_quality_chord_progs_fc(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])), 111)

  def test_four_quality_chord_progs_fc(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])), 12)

  #----------------------------------------------------------------------------------------------------------------
  # CONFLICT
  #----------------------------------------------------------------------------------------------------------------
  def test_simple_chord_progs_nogood(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 4, [])), 1920)
  
  def test_three_quality_chord_progs_nogood(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])), 111)

  def test_four_quality_chord_progs_nogood(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])), 12)

  #----------------------------------------------------------------------------------------------------------------
  # GAC
  #----------------------------------------------------------------------------------------------------------------
  def test_simple_chord_progs_gac(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [])), 1920)

  def test_three_quality_chord_progs_gac(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])), 111)
  
  def test_four_quality_chord_progs_gac(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])), 12)
  

  #----------------------------------------------------------------------------------------------------------------
  # GAC PRECOMPUTE
  #----------------------------------------------------------------------------------------------------------------
  def test_simple_chord_progs_gac_pre(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 4, [])), 1920)

  def test_three_quality_chord_progs_gac_pre(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])), 111)
  
  def test_four_quality_chord_progs_gac_pre(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])), 12)


if __name__ == '__main__':
    unittest.main()