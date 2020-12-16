import unittest
import os
import sys
import timeit
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.backtracking import backtracking, backtrackingFC, backtrackingConflictSet, backtrackingGAC, backtrackingGACPre
from Data.qualities import ChordQuality
from Data.keys import Key
from Algorithms.utils import parseChordProg

SETUP = '''from Algorithms.backtracking import backtracking, backtrackingFC, backtrackingConflictSet, backtrackingGAC, backtrackingGACPre
from Data.qualities import ChordQuality
from Data.keys import Key
from Algorithms.utils import parseChordProg'''

class BacktrackingTests(unittest.TestCase):
  #----------------------------------------------------------------------------------------------------------------
  # NAIVE BACKTRACKING
  #----------------------------------------------------------------------------------------------------------------
  def test_bt_simple_4(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [])), 1920)
    # Average time (10 trials) = 4.66535627350022
    # Average time (15 trials) = 4.552761030533778
    # Average time (20 trials) = 5.370403074999922
    print('Backtracking average time simple 4:', (timeit.timeit(setup=SETUP,stmt='backtracking(Key.C, True, 4, [])', number=10) / 10))

  def test_bt_simple_6(self):
    self.assertEqual(len(backtracking(Key.C, True, 6, [])), 46080)
    # Average time (3 trials) = 136.436584875332
    print('Backtracking average time simple 6:', timeit.timeit(setup=SETUP,stmt='backtracking(Key.C, True, 6, [])', number=3) / 3)

  def test_bt_two_qualities_4(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 321)
    # Average time (10 trials) = 5.0792490199994065
    # Average time (15 trials) = 5.820826986866693
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=15) / 15))

  def test_bt_two_qualities_6(self):
    self.assertEqual(len(backtracking(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 15858)
    # Average time (10 trials) = 139.35179846149987
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtracking(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_bt_four_qualities_complex(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 12)
    # Average time (10 trials) = 
    print('Backtracking average time four qualities complex:', (timeit.timeit(setup=SETUP,stmt='backtracking(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_bt_four_qualities_4(self):
    self.assertEqual(len(backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtracking(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_bt_four_qualities_6(self):
    self.assertEqual(len(backtracking(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtracking(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  #----------------------------------------------------------------------------------------------------------------
  # FORWARD CHECKING
  #----------------------------------------------------------------------------------------------------------------

  def test_fc_simple_4(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 4, [])), 1920)
    # Average time (10 trials) = 
    print('Backtracking average time simple 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingFC(Key.C, True, 4, [])', number=10) / 10))

  def test_fc_simple_6(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 6, [])), 46080)
    # Average time (10 trials) = 
    print('Backtracking average time simple 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingFC(Key.C, True, 6, [])', number=10) / 10))

  def test_fc_two_qualities_4(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 321)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_fc_two_qualities_6(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingFC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_fc_four_qualities_complex(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 12)
    # Average time (10 trials) = 
    print('Backtracking average time four qualities complex:', (timeit.timeit(setup=SETUP,stmt='backtrackingFC(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_fc_four_qualities_4(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingFC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_fc_four_qualities_6(self):
    self.assertEqual(len(backtrackingFC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingFC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  #----------------------------------------------------------------------------------------------------------------
  # CONFLICT
  #----------------------------------------------------------------------------------------------------------------
  def test_nogood_simple_4(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 4, [])), 1920)
    # Average time (10 trials) = 
    print('Backtracking average time simple 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingConflictSet(Key.C, True, 4, [])', number=10) / 10))

  def test_nogood_simple_6(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 6, [])), 46080)
    # Average time (10 trials) = 
    print('Backtracking average time simple 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingConflictSet(Key.C, True, 6, [])', number=10) / 10))

  def test_nogood_two_qualities_4(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 321)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_nogood_two_qualities_6(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingConflictSet(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_nogood_four_qualities_complex(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 12)
    # Average time (10 trials) = 
    print('Backtracking average time four qualities complex:', (timeit.timeit(setup=SETUP,stmt='backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_nogood_four_qualities_4(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingConflictSet(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_nogood_four_qualities_6(self):
    self.assertEqual(len(backtrackingConflictSet(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingConflictSet(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  #----------------------------------------------------------------------------------------------------------------
  # GAC
  #----------------------------------------------------------------------------------------------------------------
  def test_gac_simple_4(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [])), 1920)
    print('Backtracking average time simple 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingGAC(Key.C, True, 4, [])', number=10) / 10))

  def test_gac_simple_6(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 6, [])), 46080)
    print('Backtracking average time simple 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingGAC(Key.C, True, 6, [])', number=10) / 10))

  def test_gac_two_qualities_4(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 321)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingGAC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_gac_two_qualities_6(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingGAC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_gac_four_qualities_complex(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 12)
    # Average time (10 trials) = 
    print('Backtracking average time four qualities complex:', (timeit.timeit(setup=SETUP,stmt='backtrackingGAC(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_gac_four_qualities_4(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingGAC(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_gac_four_qualities_6(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingGAC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  #----------------------------------------------------------------------------------------------------------------
  # GAC PRECOMPUTE
  #----------------------------------------------------------------------------------------------------------------
  def test_gac_pre_simple_4(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 4, [])), 1920)
    print('Backtracking average time simple 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingGACPre(Key.C, True, 4, [])', number=10) / 10))

  def test_gac_pre_simple_6(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 6, [])), 46080)
    print('Backtracking average time simple 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingGACPre(Key.C, True, 6, [])', number=10) / 10))

  def test_gac_pre_two_qualities_4(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 321)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingGACPre(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_gac_pre_two_qualities_6(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingGACPre(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])', number=10) / 10))

  def test_gac_pre_four_qualities_complex(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 12)
    # Average time (10 trials) = 
    print('Backtracking average time four qualities complex:', (timeit.timeit(setup=SETUP,stmt='backtrackingGACPre(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_gac_pre_four_qualities_4(self):
    self.assertEqual(len(backtrackingGACPre(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 4:', (timeit.timeit(setup=SETUP,stmt='backtrackingGACPre(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

  def test_gac_pre_four_qualities_6(self):
    self.assertEqual(len(backtrackingGAC(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])), 1227)
    # Average time (10 trials) = 
    print('Backtracking average time two qualities 6:', (timeit.timeit(setup=SETUP,stmt='backtrackingGACPre(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])', number=10) / 10))

if __name__ == '__main__':
    unittest.main()