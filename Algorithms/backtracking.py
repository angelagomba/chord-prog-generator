import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQualities
from Data.intervals import Interval
from Data.notes import Note
from Data.keys import Key
from typing import List, Tuple
from utils import getTonic, getTonicCount, chordInKey

"""
We will leverage backtracking to build a chord progression of length numChords that contain each chord quality specified in qualities. 
TODO: Describe how we will use backtracking to accomplish this.
"""

def backtracking(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQualities]) -> List[List[Tuple[str, ChordQualities]]]:
  """
  Purpose: Returns a chord progression in the given key that contains the given qualities.
  TODO: We want to use enums.
  Signature: str, int, List[ChordQualities] -> List[List[str]]
  :param key: The key the chord progression is in.
  :param qualities: The chord qualities the chord progression must have.
  """
  # TODO: Implement backtracking to generate a chord progression of length numChords.
  """
  Initialize empty array (res) of chord progressions
  Memoize the used qualities so that we know how to calculate our backtracking condition
  Backtracking condition: The next chord quality cannot be created 
  Iterate through qualities, attempt to add a chord to the progression with that quality
  If next chord quality cannot be created go back to the previous and assign new value
  Return when res has numChords chords and all qualities used (remaining qualities is empty )

  Choice: What chord (root note) to assign to the current quality
  Goal: Given the choice we just made for the given quality, is the chord progression still solvable
  - Within stack frame/individual iteration of recursion, we want to express our decision by iterating through
    the notes in the key and attempting to assign chord with the current quality we are attempting to fill
  """
  # All of the chord progressions which meet the inputted constraints
  res = []
  possibleTonics = Key.getScale(key, True)
  backtrackingDriver(key, isMajor, possibleTonics, numChords, qualities, res, [], 0)
  return res

def backtrackingDriver(key: Key, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQualities], res: List[List[Tuple[Note, ChordQualities]]], progression: List[Tuple[Note, ChordQualities]], start: int):
  if len(progression) == numChords:
    if hasQualities(progression, qualities):
      res.append(progression)
    return
  for i in range(start, len(scale)):
    note = Note.getNote(scale[i])
    for quality in ChordQualities.getAllQualities():
      chord = chordInKey(note, quality, key, isMajor)
      if chord:
        backtrackingDriver(key, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1)
  

def hasQualities(progression: List[Tuple[Note, ChordQualities]], qualities: List[ChordQualities]):
  usedQualities = [chord[1] for chord in progression]
  for quality in qualities:
    if usedQualities.count(quality) < qualities.count(quality):
      return False
  return True


# def backtrackingDriver(possibleTonics, numChords, qualities, res, progression, start):
#   # TODO: Account for 7th tonic chords
#   # Append results which meet the constraints to the resultant array
#   if len(progression) == numChords and start == len(qualities) and getTonic(true, scale=possibleTonics) in progression:
#     res.append(progression)
  
#   for i in range(start, len(qualities)):
#     # Current variable to assign
#     currQuality = qualities[i]
#     # Search through domain for notes that can be assign to current quality
#     for note in possibleTonics:
#       if noteCanFormQuality(note, possibleTonics, currQuality):
#         chord = (note, currQuality)
#         progression.append(chord)
#         backtrackingDriver(possibleTonics, numChords - 1, qualities, res, progression, start + 1)
    

"""
Input: C, 3, [maj7, maj7]
First Iteration: Searching for a maj7
C -> can form maj7 -> 
F -> can form maj7  ->
G -> can form maj7 ->

"""



# def noteCanFormQuality(note, possibleTonics, quality):
  


      
