from enum import Enum

class Interval(Enum):
  """
  An enum that represents different scale intervals.
  """

  TONIC = "1"
  MIN_SECOND = "b2"
  MAJ_SECOND = "2"
  MIN_THIRD = "b3"
  MAJ_THIRD = "3"
  PERF_FOURTH = "4"
  TRITONE = "b5"
  PERF_FIFTH = "5"
  MIN_SIXTH = "b6"
  MAJ_SIXTH = "6"
  MIN_SEVENTH = "b7"
  MAJ_SEVENTH = "7"

