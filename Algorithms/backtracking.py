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
"""

def backtracking(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  """
  Main driving function for the naive backtracking implementation
  :param key: the desired musical key for the chord progressions to be generated in
  :param isMajor: a boolean representing whether the key passed in is major (true) or minor (false)
  :param numChords: the number of chords requested by the user
  :param qualities: the list of chord qualities requested by the user
  :return: a list of all chord progressions which meet the inputted constraints
  """
  # All of the chord progressions which meet the inputted constraints
  res = []
  # The possible root notes for chords (the scale of the passed in key)
  scale = Key.getScale(key, isMajor)
  # The tonic note
  tonicRoot = getTonic(isMajor, key=key)[0]
  # Recursive call to build up solutions
  backtrackingDriver(key, tonicRoot, isMajor, scale, numChords, qualities, res, [], 0)
  return res

def backtrackingDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int):
  """
  Recursive function for generating chord progressions for the naive backtracking
  implementation
  :param key: the desired musical key for the chord progressions to be generated in
  :param tonic: the tonic note for the passed in key
  :param isMajor:a boolean representing whether the key pass in is major (true) or minor (false)
  :param scale: the possible root notes for chords (the scale of the passed in key)
  :param numChords: the number of chords requested by the user
  :param qualities: a list of qualites requested by the user
  :param res: the resultant array containing all of the solutions which satisfy the constraints
  :param progression: the current chord progression being built
  :param start: the index of where to start in the scale when looking for a root note
  """
  # If the progression is the desired length
  if len(progression) == numChords:
    # If the progression has all of the inputted qualities and a chord with the tonic as a root, add it to our solutions
    if hasQualities(progression, qualities) and hasTonic(progression, tonic):
      res.append(progression)
    return
  # Iterate through the scale to select a root note
  for i in range(start, len(scale)):
    note = Note.getNote(scale[i])
    # Iterate through all of the chord qualities to select a chord quality
    for quality in ChordQuality.getAllQualities():
      # Check if the chord is within key
      chord = chordInKey(note, quality, key, isMajor)
      if chord:
        # Recursive call to continue exploration along a branch, adds the chord to the progression and increments the start pointer to allow for different combinations to be generated
        backtrackingDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1)


# This is the code for backtracking improved with forward checking
def backtrackingFC(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  scale = Key.getScale(key, isMajor)
  tonicRoot = getTonic(isMajor, key=key)[0]
  # Keep a list of remaining qualities
  remainingQualities = copy.copy(qualities)
  backtrackingFCDriver(key, tonicRoot, isMajor, scale, numChords, qualities, res, [], 0, remainingQualities)
  return res

def backtrackingFCDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int, remainingQualities: List[ChordQuality]):
  # Discard this solution if there are more remaining qualities than there are remaining slots in the chord progression
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
        # If the chord quality is in the remaining qualities, remove it from remaining qualities
        if quality in remainingQualities:
          remainingQualities.remove(quality)
        backtrackingFCDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1, remainingQualities)

# This is the code for backtracking improved with a conflict set for conflict-directed backjumping
def backtrackingConflictSet(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  scale = Key.getScale(key, isMajor)
  tonicRoot = getTonic(isMajor, key=key)[0]
  # Keep a no-good/conflict set for values which result in impossible to solve progressions (out of key chords)
  noGood = []
  backtrackingConflictSetDriver(key, tonicRoot, isMajor, scale, numChords, qualities, res, [], 0, noGood)
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
      # If the chord is not in key, backjump to last assignment without this inconsistent value
      if potentialChord in noGood:
        continue
      chord = chordInKey(note, quality, key, isMajor)
      if chord:
        backtrackingConflictSetDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [chord], start + 1, noGood)
      else:
        # Add out of key chords to our conflict set
        noGood.append(potentialChord)

# This is the code for backtracking with GAC informed filtering
def backtrackingGAC(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  scale = Key.getScale(key, isMajor)
  tonicRoot = getTonic(isMajor, key=key)[0]
  # Initialize our domain as a map whose keys are the root notes, and whose values are a list of chord qualities to form a potential chord
  allChords = {}
  allQualities = ChordQuality.getAllQualities()
  for note in scale:
    allChords[note] = list(allQualities)
  backtrackingGACDriver(key, tonicRoot, isMajor, scale, numChords, qualities, res, [], 0, allChords)
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
      # skip qualities that have been filtered out
      if not quality:
        continue
      possibleChord = chordInKey(root, quality, key, isMajor)
      if possibleChord:
        backtrackingGACDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [possibleChord], start + 1, possibleChords)
      else:
        # filter out of key chord qualities out of the domain
        possibleChords[note][i] = None

# This is the code for backtracking with GAC informed filtering, but the filtering is done as a preprocesser rather than during exploration/at each assignment
def backtrackingGACPre(key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]) -> List[List[Tuple[str, ChordQuality]]]:
  res = []
  scale = Key.getScale(key, isMajor)
  tonicRoot = getTonic(isMajor, key=key)[0]
  allChordsInKey = {}
  allQualities = ChordQuality.getAllQualities()
  # Initialize our domain as a map whose keys are the root notes, and whose values are a list of chord qualities to form a potential chord
  # Only add chords qualities that are in key
  for note in scale:
    root = Note.getNote(note)
    for quality in allQualities:
      chord = chordInKey(root, quality, key, isMajor)
      if chord:
        if note in allChordsInKey:
          allChordsInKey[note].append(quality)
        else:
          allChordsInKey[note] = [quality]
  backtrackingGACPreDriver(key, tonicRoot, isMajor, scale, numChords, qualities, res, [], 0, allChordsInKey)
  return res

def backtrackingGACPreDriver(key: Key, tonic: Note, isMajor: bool, scale: List[str], numChords: int, qualities: List[ChordQuality], res: List[List[Tuple[Note, ChordQuality]]], progression: List[Tuple[Note, ChordQuality]], start: int, possibleChords: Dict[Note, List[ChordQuality]]):
  if len(progression) == numChords:
    if hasQualities(progression, qualities) and hasTonic(progression, tonic):
      res.append(progression)
    return
  
  for note in list(possibleChords.keys())[start:len(possibleChords)]:
    possibleChordQualities = possibleChords[note]
    for quality in possibleChordQualities:
      backtrackingGACPreDriver(key, tonic, isMajor, scale, numChords, qualities, res, progression + [(Note.getNote(note), quality)], start + 1, possibleChords)

  

def hasQualities(progression: List[Tuple[Note, ChordQuality]], qualities: List[ChordQuality]) -> bool:
  """
  Helper function that returns whether the given chord progression has the given list of qualities
  :param progression: the chord progression to check for qualities
  :param qualities: the qualities to look for in the progression
  :return: a boolean indicating the progression has all of the given qualities
  """
  usedQualities = [chord[1] for chord in progression]
  for quality in qualities:
    if usedQualities.count(quality) < qualities.count(quality):
      return False
  return True


def hasTonic(progression: List[Tuple[Note, ChordQuality]], tonic: Note) -> bool:
  """
  Helper function that returns whether the given chord progresion has the given tonic
  :param progression: the chord progression to check for the tonic
  :param tonic: the tonic to look for in the progression
  :return: a boolean indicating whether or not the tonic exists in the chord progression
  """
  for chord in progression:
    if chord[0] == tonic:
      return True
  return False



  


      
