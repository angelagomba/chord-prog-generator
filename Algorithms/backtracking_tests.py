import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.backtracking import backtracking, backtrackingFC, backtrackingConflictSet, backtrackingGAC
from Data.qualities import ChordQuality
from Data.keys import Key
from Algorithms.utils import parseChordProg

class BacktrackingTests(unittest.TestCase):

  def test_simple_chord_progs(self):
    print(len(backtracking(Key.C, True, 4, [])))

  def test_one_quality_chord_progs(self):
    print(backtracking(Key.C, True, 4, [ChordQuality.MAJ7]))

  def test_three_quality_chord_progs(self):
    print([parseChordProg(progression) for progression in backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])])

  def test_four_quality_chord_progs(self):
    print([parseChordProg(progression) for progression in backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])])

  def test_simple_chord_progs_fc(self):
    print(len(backtrackingFC(Key.C, True, 4, [])))
  
  def test_three_quality_chord_progs_fc(self):
    print(backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])[:4])

  def test_four_quality_chord_progs_fc(self):
    print([parseChordProg(progression) for progression in backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])])

  def test_simple_chord_progs_nogood(self):
    print(len(backtrackingConflictSet(Key.C, True, 4, [])))
  
  def test_three_quality_chord_progs_nogood(self):
    print(backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])[:4])

  def test_four_quality_chord_progs_nogood(self):
    print([parseChordProg(progression) for progression in backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM])])

  def test_three_quality_chord_progs_gac(self):
    print(len([parseChordProg(progression) for progression in backtrackingGAC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.DIM])]))


if __name__ == '__main__':
    unittest.main()