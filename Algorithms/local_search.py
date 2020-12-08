import copy
import os
import random
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQualities
from Data.intervals import Interval
from Data.keys import Key
from Data.notes import Note
from Data.constants import diatonic_seq
from typing import Dict, List, Tuple
from utils import getTonic, getTonicCount, inKey, chordInKey

"""
We will leverage local search to build a chord progression of length numChords that contain each chord quality specified in qualities. 
We will start off with a randomly generated chord progression that follows the qualities specified in the diatonic sequence, and iteratively 
move to a neighboring solution until we have a solution that meets the constraints of the CSP. If our initial candidate solution does not 
include all the chord qualities in qualities, then we will iterate through the chord progression and find a neighboring solution 
where we change our current chord to a chord with a chord quality listed in qualities. If we reach the end of the chord progression and 
are unable to meet all the constraints, we start the algorithm again with another randomly generated chord progression. Since local search 
does not guarantee completeness, we will return the solution we have, whether complete or incomplete, before the end of the timeout.
"""

# Chord: (Note, ChordQuality)

class LocalSearch(object):

  def __init__(self, key: Key, isMajor: bool, numChords: int, qualities: List[ChordQualities]):
    self.key = key
    self.isMajor = isMajor
    self.numChords = numChords
    self.qualities = qualities
    self.tonic = getTonic(isMajor, key)
    self.chord_prog = [] # stores our current solution

  def local_search(self) -> List[Tuple[str, ChordQualities]]:
    """
    Purpose: Returns a chord progression in the given key that contains the given qualities.
    Signature: Key, bool, int, List[ChordQualities] -> List[Tuple[str, ChordQualities]]
    :param key: The key the chord progression is in.
    :param qualities: The chord qualities the chord progression must have.
    """
    # Randomly pick numChords amount of notes in the scale of the given key
    self.chord_prog = self.createRandChordProg()
    # Filter through which qualities we still need
    used_qualities = self.getUsedQualities()
    remaining_qualities = [quality for quality in self.qualities if quality not in used_qualities]
    # Look for neighboring solutions
    if remaining_qualities:
      for i, chord in enumerate(self.chord_prog):
        newChord = self.getNewChord(chord[0], remaining_qualities) \
          if self.canReplaceChord(chord, used_qualities) else None
        if newChord:
            newQuality = newChord[1]
            self.chord_prog[i] = newChord
            used_qualities[newQuality] = 1
            remaining_qualities.remove(newQuality)
        # If we have all of the desired qualities, we can break out of the loop
        if not remaining_qualities:
          break
      # If we did not find a solution, run the algorithm again
      if remaining_qualities:
        return self.local_search()
    return self.chord_prog

  def createRandChordProg(self) -> List[Tuple[str, ChordQualities]]:
    """
    Purpose: Returns a random chord progression of length numChords in the given key. isMajor determines whether the 
    chord progression is minor or major.
    """
    scale = Key.getScale(self.key, self.isMajor)
    root_notes = random.choices(scale, k=self.numChords)
    chord_prog = [(Note.getNote(note), diatonic_seq[scale.index(note)]) for note in root_notes]
    # Check if the tonic is in the chord_prog. If not, replace the last chord as the tonic.
    # NOTE: We do this because we want our chord_prog to resolve.
    tonic_count = chord_prog.count(self.tonic)
    if tonic_count == 0:
      chord_prog[-1] = self.tonic
      tonic_count = 1
    return chord_prog

  def getUsedQualities(self) -> Dict[ChordQualities, int]:
    """
    Purpose: Returns a dictionary whose keys are chord qualities found in the given chord_prog and values are
    the count of those qualities in the chord progression.
    """
    used_qualities = {}
    for chord in self.chord_prog:
      if chord[1] in used_qualities:
        used_qualities[chord[1]] += 1
      else:
        used_qualities[chord[1]] = 1
    return used_qualities

  def canReplaceChord(self, chord: Tuple[str, ChordQualities], used_qualities: Dict[ChordQualities, int]) -> bool:
    """
    Purpose: Determines whether or not we can replace the given chord within the chord progression.
    """
    tonic_count = getTonicCount(self.tonic, self.chord_prog)
    quality = chord[1]
    # We can replace a duplicate tonic, if the chord doesn't have a desired quality, or if it is a desired quality and we have more
    # than one of it
    return (chord == self.tonic and tonic_count > 1) or (chord != self.tonic and quality not in self.qualities) or (quality in used_qualities and used_qualities[quality] > 1)

  def getNewChord(self, root: Note, qualities: List[ChordQualities]) -> Tuple[str, ChordQualities] or None:
    """
    Purpose: Returns a chord with the same root and a quality in qualities that is in the given key. If there is none, we return None.
    """
    for quality in qualities:
      potentialChord = chordInKey(root, quality, self.key, self.isMajor)
      if potentialChord:
        return potentialChord
    return None

