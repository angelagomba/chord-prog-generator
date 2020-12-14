import os
import sys
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQuality
from Data.intervals import Interval
from Data.notes import Note
from Data.keys import Key
from typing import List, Tuple, Set, Dict
from utils import getTonic, getTonicCount, chordInKey

"""
We will leverage backtracking to build a chord progression of length numChords that contain each chord quality specified in qualities. 
TODO: Describe how we will use backtracking to accomplish this.
"""

def backtracking(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  """
  Purpose: Returns a chord progression in the given key that contains the given qualities.
  TODO: We want to use enums.
  Signature: str, int, List[ChordQuality] -> List[List[str]]
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
  tonicRoot = getTonic(isMajor, key=key)[0]
  backtrackingDriver(key, tonicRoot, isMajor, possibleTonics, numChords, qualities, res, [], 0)
  return res

def backtrackingDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int):
  if len(progression) == numChords:
    if hasQualities(progression, qualities) and hasTonic(progression, tonic):
      res.append(progression)
    return
  for i in range(start, len(scale)):
    note = Note.getNote(scale[i])
    for quality in ChordQuality.getAllQualities():
      chord = chordInKey(note, quality, key, isMajor)
      if chord:
        backtrackingDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1)


def backtrackingFC(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  possibleTonics = Key.getScale(key, True)
  tonicRoot = getTonic(isMajor, key=key)[0]
  remainingQualities = copy.copy(qualities)
  backtrackingFCDriver(key, tonicRoot, isMajor, possibleTonics, numChords, qualities, res, [], 0, remainingQualities)
  return res

def backtrackingFCDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int, remainingQualities: List[ChordQuality]):
  if len(remainingQualities) > numChords - len(progression):
    return 
  if len(progression) == numChords:
    if hasQualities(progression, qualities) and hasTonic(progression, tonic):
      res.append(progression)
    return
  for i in range(start, len(scale)):
    note = Note.getNote(scale[i])
    for quality in ChordQuality.getAllQualities():
      chord = chordInKey(note, quality, key, isMajor)
      if chord:
        if quality in remainingQualities:
          remainingQualities.remove(quality)
        backtrackingFCDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1, remainingQualities)


def backtrackingConflictSet(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  possibleTonics = Key.getScale(key, True)
  tonicRoot = getTonic(isMajor, key=key)[0]
  noGood = []
  backtrackingConflictSetDriver(key, tonicRoot, isMajor, possibleTonics, numChords, qualities, res, [], 0, noGood)
  return res


def backtrackingConflictSetDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int, noGood: List[Tuple[Note, ChordQuality]]):
  if len(progression) == numChords:
    if hasQualities(progression, qualities) and hasTonic(progression, tonic):
      res.append(progression)
    return
  for i in range(start, len(scale)):
    note = Note.getNote(scale[i])
    for quality in ChordQuality.getAllQualities():
      potentialChord = (note, quality)
      if potentialChord in noGood:
        continue
      chord = chordInKey(note, quality, key, isMajor)
      if chord:
        backtrackingConflictSetDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1, noGood)
      else:
        noGood.append(potentialChord)

def backtrackingGAC(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  possibleTonics = Key.getScale(key, True)
  tonicRoot = getTonic(isMajor, key=key)[0]
  allChords = {}
  allQualities = ChordQuality.getAllQualities()
  for note in possibleTonics:
    allChords[note] = list(allQualities)
  backtrackingGACDriver(key, tonicRoot, isMajor, possibleTonics, numChords, qualities, res, [], 0, allChords)
  return res

def backtrackingGACDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int, possibleChords: Dict[Note, List[ChordQuality]]):
  if len(progression) == numChords:
    if hasQualities(progression, qualities) and hasTonic(progression, tonic):
      res.append(progression)
    return
  
  for note in list(possibleChords.keys())[start:len(possibleChords)]:
    root = Note.getNote(note)
    possibleChordQualities = possibleChords[note]
    for i in range(len(possibleChordQualities)):
      quality = possibleChordQualities[i]
      if not quality:
        continue
      possibleChord = chordInKey(root, quality, key, isMajor)
      if possibleChord:
        backtrackingGACDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [possibleChord], start + 1, possibleChords)
      else:
        possibleChords[note][i] = None


def backtrackingGACPre(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  possibleTonics = Key.getScale(key, True)
  tonicRoot = getTonic(isMajor, key=key)[0]
  noGood = set()
  backtrackingFCDriver(key, tonicRoot, isMajor, possibleTonics, numChords, qualities, res, [], 0, noGood)
  return res

def backtrackingGACPreDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int, noGood: Set[Tuple[Note, ChordQuality]]):
  if len(progression) == numChords:
    if hasQualities(progression, qualities) and hasTonic(progression, tonic):
      res.append(progression)
    return
  for i in range(start, len(scale)):
    note = Note.getNote(scale[i])
    for quality in ChordQuality.getAllQualities():
      potentialChord = (note, quality)
      if potentialChord in noGood:
        return
      chord = chordInKey(note, quality, key, isMajor)
      if chord:
        backtrackingGACDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1, noGood)
      else:
        noGood.add(potentialChord)



  


def hasQualities(progression: List[Tuple[Note, ChordQuality]], qualities: List[ChordQuality]):
  usedQualities = [chord[1] for chord in progression]
  for quality in qualities:
    if usedQualities.count(quality) < qualities.count(quality):
      return False
  return True


def hasTonic(progression: List[Tuple[Note, ChordQuality]], tonic: Note):
  for chord in progression:
    if chord[0] == tonic:
      return True
  return False


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
  


      
