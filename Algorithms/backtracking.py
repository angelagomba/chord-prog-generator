import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.Chords.qualities import ChordQualities
from Data.Chords.interval import Interval
from typing import List

"""
We will leverage backtracking to build a chord progression of length numChords that contain each chord quality specified in qualities. 
TODO: Describe how we will use backtracking to accomplish this.
"""

def backtracking(key: str, numChords: int, qualities: List[ChordQualities]):
  """
  Purpose: Returns a chord progression in the given key that contains the given qualities.
  TODO: We want to use enums.
  Signature: str, int, List[ChordQualities] -> List[List[str]]
  :param key: The key the chord progression is in.
  :param qualities: The chord qualities the chord progression must have.
  """
  # TODO: Implement backtracking to generate a chord progression of length numChords.