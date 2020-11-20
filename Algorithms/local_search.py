import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.Chords.qualities import ChordQualities
from Data.Chords.interval import Interval
from typing import List

"""
We will leverage local search to build a chord progression of length numChords that contain each chord quality specified in qualities. 
We will start off with a randomly generated chord progression that follows the qualities specified in the diatonic sequence, and iteratively 
move to a neighboring solution until we have a solution that meets the constraints of the CSP. If our initial candidate solution does not 
include all the chord qualities in qualities, then we will iterate through the chord progression and find a neighboring solution 
where we change our current chord to a chord with a chord quality listed in qualities. If we reach the end of the chord progression and 
are unable to meet all the constraints, we start the algorithm again with another randomly generated chord progression. Since local search 
does not guarantee completeness, we will return the solution we have, whether complete or incomplete, before the end of the timeout.
"""

def local_search(key: str, numChords: int, qualities: List[ChordQualities]):
  """
  Purpose: Returns a chord progression in the given key that contains the given qualities.
  TODO: We want to use enums.
  Signature: str, int, List[ChordQualities] -> List[List[str]]
  :param key: The key the chord progression is in.
  :param qualities: The chord qualities the chord progression must have.
  """
  # Randomly generating chords:
  # ---------------------------
  # Randomly pick numChords amount of notes in the scale of the given key
  # Form those 4 notes into chords with qualities from the diatonic sequence

  # Building the chord progression:
  # -------------------------------
  # Randomly generate a list of 4 chords in the given key
  # Iterate thorugh the 4 chords to find which qualities we use
    # Have a list to keep track of which chord qualities in qualities we have used
  # If the length of used is 4, RETURN
  # If the length of used is less than 4,
    # Iterate through our current chord progression
      # If the chord we are looking at doesn't have a quality specified in qualities:
        # Keep the root note of the chord, but change its quality
        # Check if this new chord is in the key
        # If it is, make the change
        # Otherwise, move on to the next chord in the progression
    # If the length of used is 4, RETURN
    # Else, run the algorithm again
  # If the timeout runs out before the algorithm returns, RETURN
  return key

