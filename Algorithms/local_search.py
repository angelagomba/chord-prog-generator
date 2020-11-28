import copy
import os
import random
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQualities
from Data.intervals import Interval
from Data.keys import Key
from typing import Dict, List, Tuple
from utils import getScale, getTonic, getTonicCount
from Data.constants import diatonic_seq

"""
We will leverage local search to build a chord progression of length numChords that contain each chord quality specified in qualities. 
We will start off with a randomly generated chord progression that follows the qualities specified in the diatonic sequence, and iteratively 
move to a neighboring solution until we have a solution that meets the constraints of the CSP. If our initial candidate solution does not 
include all the chord qualities in qualities, then we will iterate through the chord progression and find a neighboring solution 
where we change our current chord to a chord with a chord quality listed in qualities. If we reach the end of the chord progression and 
are unable to meet all the constraints, we start the algorithm again with another randomly generated chord progression. Since local search 
does not guarantee completeness, we will return the solution we have, whether complete or incomplete, before the end of the timeout.
"""
# TODO: Set up notes as enums
# Chord: (root note (str), ChordQuality)

# Notes for parser: 
# - It will need to check for duplicate qualities

def local_search(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQualities]) -> List[Tuple(str, ChordQualities)]:
  """
  Purpose: Returns a chord progression in the given key that contains the given qualities.
  Signature: Key, bool, int, List[ChordQualities] -> List[Tuple(str, ChordQualities)]
  :param key: The key the chord progression is in.
  :param qualities: The chord qualities the chord progression must have.
  """
  # Randomly pick numChords amount of notes in the scale of the given key
  chord_prog = createRandChordProg(key, isMajor, numChords)
  # Filter through which qualities we still need
  used_qualities = getUsedQualities(chord_prog)
  remaining_qualities = [quality for quality in qualities if quality not in used_qualities]
  # Look for neighboring solutions
  tonic = getTonic(isMajor, key)
  if remaining_qualities:
    for i, chord in enumerate(chord_prog):
      tonic_count = getTonicCount(tonic, chord_prog)
      newChord = getNewChord(chord[0], key, remaining_qualities, isMajor) \
        if canReplaceChord(chord, tonic, tonic_count, qualities, used_qualities) else None
      if newChord:
          newQuality = newChord[1]
          chord_prog[i] = newChord
          used_qualities[newQuality] = 1
          remaining_qualities.remove(newQuality)
      # If we have all of the desired qualities, we can break out of the loop
      if not remaining_qualities:
        break
    # If we did not find a solution, run the algorithm again
    if remaining_qualities:
      return local_search(key, isMajor, numChords, qualities)
  # TODO: Figure out where the timeout is supposed to go, and how it will return an incomplete solution
  # NOTE: I feel like there might be an advantage if this is a class... we'd be able to store a temp solution
  # and any other info as class variables.
  return chord_prog

def createRandChordProg(key, isMajor, numChords) -> List[Tuple[str, ChordQualities]]:
  """
  Purpose: Returns a random chord progression of length numChords in the given key. isMajor determines whether the 
  chord progression is minor or major.
  """
  scale = getScale(key, isMajor)
  root_notes = random.choices(scale, k=numChords)
  tonic = getTonic(isMajor, scale=scale)
  chord_prog = [(note, diatonic_seq[scale.index(note)]) for note in root_notes]
  # Check if the tonic is in the chord_prog. If not, replace the last chord as the tonic.
  # NOTE: We do this because we want our chord_prog to resolve.
  tonic_count = chord_prog.count(tonic)
  if tonic_count == 0:
    chord_prog[-1] = tonic
    tonic_count = 1
  return chord_prog

def getUsedQualities(chord_prog: List[Tuple[str, ChordQualities]]) -> Dict[ChordQualities, int]:
  """
  Purpose: Returns a dictionary whose keys are chord qualities found in the given chord_prog and values are
  the count of those qualities in the chord progression.
  """
  used_qualities = {}
  for chord in chord_prog:
    if chord[1] in used_qualities:
      used_qualities[chord[1]] += 1
    else:
      used_qualities[chord[1]] = 1
  return used_qualities

def canReplaceChord(chord: Tuple(str, ChordQualities), tonic: Tuple(str, ChordQualities), tonic_count: int, qualities: List[ChordQualities], \
  used_qualities: Dict[ChordQualities, int]) -> bool:
  """
  Purpose: Determines whether or not we can replace the given chord within the chord progression.
  """
  quality = chord[1]
  # We can replace a duplicate tonic, if the chord doesn't have a desired quality, or if it is a desired quality and we have more
  # than one of it
  return (chord == tonic and tonic_count > 1) or (chord != tonic and quality not in qualities) or (quality in used_qualities and used_qualities[quality] > 1)

def getNewChord(root: str, key: Key, qualities: List[ChordQualities], isMajor: bool) -> Tuple(str, ChordQualities) or None:
  """
  Purpose: Returns a chord with the same root and a quality in qualities that is in the given key. If there is none, we return None.
  """
  for quality in qualities:
    root_scale = getScale(Key.getKey(root), isMajor)
    notes = []
    for interval in quality:
      if 'b' in interval:
        note = interval[-1]
        
      else: 
        notes.append(root_scale[interval - 1])
      # Check that the notes are in the key
      # If so, return the new chord
      return (root, quality)
  return None

