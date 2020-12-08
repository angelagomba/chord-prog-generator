import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from enum import Enum
from intervals import Interval

class ChordQualities(Enum):
  """
  An enum that represents different chord qualities, and the intervals that compose them.
  """
  MAJ = [Interval.TONIC, Interval.MAJ_THIRD, Interval.PERF_FIFTH] # maj: 1 3 5
  MIN = [Interval.TONIC, Interval.MIN_THIRD, Interval.PERF_FIFTH] # min: 1 b3 5
  DIM = [Interval.TONIC, Interval.MIN_THIRD, Interval.TRITONE] # dim: 1 b3 b5
  HALF_DIM = [Interval.TONIC, Interval.MIN_THIRD, Interval.TRITONE, Interval.MIN_SEVENTH] # half-dim: 1 b3 b5 b7
  MAJ7 = [Interval.TONIC, Interval.MAJ_THIRD, Interval.PERF_FIFTH, Interval.MAJ_SEVENTH] # maj7: 1 3 5 7
  MIN7 = [Interval.TONIC, Interval.MIN_THIRD, Interval.PERF_FIFTH, Interval.MIN_SEVENTH] # min7: 1 b3 5 b7
  DOM7 = [Interval.TONIC, Interval.MAJ_THIRD, Interval.PERF_FIFTH, Interval.MIN_SEVENTH] # dom7: 1 3 5 b7

  # We will adapt our data structures to handle extended chords in a later milestone
  # MAJ9 = [Interval.TONIC, Interval.MAJ_THIRD, Interval.PERF_FIFTH, Interval.MAJ_SEVENTH, Interval.MAJ_NINTH] # maj9: 1 3 5 7 9
  # MIN9 = [] # min9: 1 b3 5 b7 9

  @staticmethod
  def getIntervals(quality):
    return quality.value

  @staticmethod
  def getAllQualities():
    return [quality for quality in ChordQualities]


  