import unittest
import os
import sys
import timeit
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.local_search import LocalSearch
from Data.qualities import ChordQuality
from Data.keys import Key
from utils import parseChordProg

SETUP = '''from Algorithms.local_search import LocalSearch
from Data.qualities import ChordQuality
from Data.keys import Key
from Algorithms.utils import parseChordProg'''

#----------------------------------------------------------------------------------------------------------------
# SIMPLE HILL CLIMBING: Experiments & Results
#----------------------------------------------------------------------------------------------------------------
# Average time = 8.579478999308776e-05
SIMPLE_4_RUN_SHC = '''ls = LocalSearch(Key.C, True, 4, [])
ls.simple_hill_climbing()'''

# Average time = 0.00011784174996137153
SIMPLE_6_RUN_SHC = '''ls = LocalSearch(Key.C, True, 6, [])
ls.simple_hill_climbing()'''

# Average time = 0.0050837286000023595
TWO_4_RUN_SHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
ls.simple_hill_climbing()'''

# Average time = 0.005294061629974749
TWO_6_RUN_SHC = '''ls = LocalSearch(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
ls.simple_hill_climbing()'''

# INCOMPLETE
INCOMPLETE_SHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
ls.simple_hill_climbing()'''

# Average Time = 0.1374030632100039
FOUR_5_RUN_SHC = '''ls = LocalSearch(Key.C, True, 5, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
ls.simple_hill_climbing()'''

# Average time = 0.030169640430030994
FOUR_4_RUN_SHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
ls.simple_hill_climbing()'''

# Average time = 0.01221034079004312
FOUR_6_RUN_SHC = '''ls = LocalSearch(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
ls.simple_hill_climbing()'''

#----------------------------------------------------------------------------------------------------------------
# STEEPEST-ASCENT HILL CLIMBING: Experiments & Results
#----------------------------------------------------------------------------------------------------------------
# Average time = 8.579572997405194e-05
SIMPLE_4_RUN_SAHC = '''ls = LocalSearch(Key.C, True, 4, [])
ls.steepest_ascent_hill_climbing()'''

# Average time = 0.00011996578003163449
SIMPLE_6_RUN_SAHC = '''ls = LocalSearch(Key.C, True, 6, [])
ls.steepest_ascent_hill_climbing()'''

# Average time = 0.005097900530017796
TWO_4_RUN_SAHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
ls.steepest_ascent_hill_climbing()'''

# Average time = 0.004552593490006984
TWO_6_RUN_SAHC = '''ls = LocalSearch(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
ls.steepest_ascent_hill_climbing()'''

# INCOMPLETE
INCOMPLETE_SAHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
ls.steepest_ascent_hill_climbing()'''

# Average Time = 0.11634837288002017
FOUR_5_RUN_SAHC = '''ls = LocalSearch(Key.C, True, 5, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
ls.steepest_ascent_hill_climbing()'''

# Average time = 0.030060418249995564
FOUR_4_RUN_SAHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
ls.steepest_ascent_hill_climbing()'''

# Average time = 0.01023197110000183
FOUR_6_RUN_SAHC = '''ls = LocalSearch(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
ls.steepest_ascent_hill_climbing()'''

#----------------------------------------------------------------------------------------------------------------
# STOCHASTIC HILL CLIMBING: Experiments & Results
#----------------------------------------------------------------------------------------------------------------
# Average time = 8.420908998232334e-05
SIMPLE_4_RUN_STHC = '''ls = LocalSearch(Key.C, True, 4, [])
ls.stochastic_hill_climbing()'''

# Average time = 0.00011589933004870546
SIMPLE_6_RUN_STHC = '''ls = LocalSearch(Key.C, True, 6, [])
ls.stochastic_hill_climbing()'''

# Average time = 0.0052351125299901465
TWO_4_RUN_STHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
ls.stochastic_hill_climbing()'''

# Average time = 0.005487475379995885
TWO_6_RUN_STHC = '''ls = LocalSearch(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
ls.stochastic_hill_climbing()'''

# INCOMPLETE
INCOMPLETE_STHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
ls.stochastic_hill_climbing()'''

# Average Time = 0.11376047908997862
FOUR_5_RUN_STHC = '''ls = LocalSearch(Key.C, True, 5, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
ls.stochastic_hill_climbing()'''

# Average time = 0.031121719970033154
FOUR_4_RUN_STHC = '''ls = LocalSearch(Key.C, True, 4, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
ls.stochastic_hill_climbing()'''

# Average time = 0.011717057679998106
FOUR_6_RUN_STHC = '''ls = LocalSearch(Key.C, True, 6, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
ls.stochastic_hill_climbing()'''

class LocalSearchTests(unittest.TestCase):
  #----------------------------------------------------------------------------------------------------------------
  # SIMPLE HILL CLIMBING
  #----------------------------------------------------------------------------------------------------------------
  def test_shc_simple_4(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time simple 4:', timeit.timeit(setup=SETUP,stmt=SIMPLE_4_RUN_SHC, number=100) / 100)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_shc_simple_6(self):
    numChords = 6
    ls = LocalSearch(Key.C, True, numChords, [ChordQuality.MIN7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time simple 6:', timeit.timeit(setup=SETUP,stmt=SIMPLE_6_RUN_SHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_two_qualities_4(self):
    numChords = 4
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 2 qualities 4:', timeit.timeit(setup=SETUP,stmt=TWO_4_RUN_SHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_two_qualities_6(self):
    numChords = 6
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 2 qualities 6:', timeit.timeit(setup=SETUP,stmt=TWO_6_RUN_SHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_four_qualities_4(self):
    numChords = 4
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 4:', timeit.timeit(setup=SETUP,stmt=INCOMPLETE_SHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_four_qualities_incomplete(self):
    numChords = 4
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 4:', timeit.timeit(setup=SETUP,stmt=FOUR_4_RUN_SHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      print('Local search average time 4 qualities 4:', timeit.timeit(setup=SETUP,stmt=FOUR_4_RUN_SHC, number=100) / 100)
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_shc_four_qualities_5(self):
    numChords = 5
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DIM, ChordQuality.DOM7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 5:', timeit.timeit(setup=SETUP,stmt=FOUR_5_RUN_SHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_shc_four_qualities_6(self):
    numChords = 6
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.simple_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 6:', timeit.timeit(setup=SETUP,stmt=FOUR_6_RUN_SHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)
  
  #----------------------------------------------------------------------------------------------------------------
  # STEEPEST-ASCENT HILL CLIMBING
  #----------------------------------------------------------------------------------------------------------------
  def test_sahc_simple_4(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time simple 4:', timeit.timeit(setup=SETUP,stmt=SIMPLE_4_RUN_SAHC, number=100) / 100)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_sahc_simple_6(self):
    numChords = 6
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time simple 6:', timeit.timeit(setup=SETUP,stmt=SIMPLE_6_RUN_SAHC, number=100) / 100)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_two_qualities_4(self):
    numChords = 4
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 2 qualities 4:', timeit.timeit(setup=SETUP,stmt=TWO_4_RUN_SAHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_two_qualities_6(self):
    numChords = 6
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 2 qualities 6:', timeit.timeit(setup=SETUP,stmt=TWO_6_RUN_SAHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_four_qualities_incomplete(self):
    numChords = 4
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 4:', timeit.timeit(setup=SETUP,stmt=INCOMPLETE_SAHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_four_qualities_5(self):
    numChords = 5
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 5:', timeit.timeit(setup=SETUP,stmt=FOUR_5_RUN_SAHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_four_qualities_4(self):
    numChords = 4
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 4:', timeit.timeit(setup=SETUP,stmt=FOUR_4_RUN_SAHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sahc_four_qualities_6(self):
    numChords = 6
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.steepest_ascent_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 6:', timeit.timeit(setup=SETUP,stmt=FOUR_6_RUN_SAHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)
  
  #----------------------------------------------------------------------------------------------------------------
  # STOCHASTIC HILL CLIMBING
  #----------------------------------------------------------------------------------------------------------------
  def test_sthc_simple_4(self):
    numChords = 4
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time simple 4:', timeit.timeit(setup=SETUP,stmt=SIMPLE_4_RUN_STHC, number=100) / 100)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_sthc_simple_6(self):
    numChords = 6
    ls = LocalSearch(Key.C, True, numChords, [])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time simple 6:', timeit.timeit(setup=SETUP,stmt=SIMPLE_6_RUN_STHC, number=100) / 100)
    except RecursionError:
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_two_qualities_4(self):
    numChords = 4
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time two qualities 4:', timeit.timeit(setup=SETUP,stmt=TWO_4_RUN_STHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_two_qualities_6(self):
    numChords = 6
    ls = LocalSearch(Key.D, True, numChords, [ChordQuality.MAJ7, ChordQuality.HALF_DIM])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time two qualities 6:', timeit.timeit(setup=SETUP,stmt=TWO_6_RUN_STHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_four_qualities_incomplete(self):
    numChords = 4
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 4:', timeit.timeit(setup=SETUP,stmt=INCOMPLETE_STHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_four_qualities_5(self):
    numChords = 5
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MIN7, ChordQuality.DIM, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 5:', timeit.timeit(setup=SETUP,stmt=FOUR_5_RUN_STHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

  def test_sthc_four_qualities_4(self):
    numChords = 4
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 4:', timeit.timeit(setup=SETUP,stmt=FOUR_4_RUN_STHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)
  
  def test_sthc_four_qualities_6(self):
    numChords = 6
    ls = LocalSearch(Key.G, True, numChords, [ChordQuality.MAJ7, ChordQuality.MIN7, ChordQuality.HALF_DIM, ChordQuality.DOM7])
    try:
      ls.stochastic_hill_climbing()
      self.assertEqual(len(ls.chord_prog), numChords)
      print('Local search average time 4 qualities 6:', timeit.timeit(setup=SETUP,stmt=FOUR_6_RUN_STHC, number=100) / 100)
    except RecursionError:
      print('Unable to create chord prog with the following qualities: ', [quality.name for quality in ls.qualities])
      self.assertEqual(len(ls.chord_prog), numChords)

if __name__ == '__main__':
    unittest.main()