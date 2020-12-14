import copy
import os
import random
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQuality
from Data.constants import diatonic_seq
from Data.intervals import Interval
from Data.keys import Key
from Algorithms.local_search_methods import LSMethod
from Data.notes import Note
from typing import Dict, List, Tuple
from utils import getTonic, getTonicCount, inKey, chordInKey, parseChordProg

class LocalSearch(object):
  """
  Purpose: We will leverage local search algorithms to build a chord progression of length numChords that contain each chord quality
  specified in qualities. We have chosen to investigate hill climbing as our local search algorithm, and the three methods of 
  hill climbing: simple hill climbing, steepest-ascent hill climbing, and stochastic hill climbing. 
  NOTE: The output of each local search algorithm is a list of chords. A chord is a tuple of the form (Note, ChordQuality).
  """

  def __init__(self, key: Key, isMajor: bool, numChords: int, qualities: List[ChordQuality]):
    """
    Purpose: Initializes a CSP that will be solved by one of the following local search algorithms:
      - Simple Hill Climbing
      - Steepest-Ascent Hill climbing
      - Stochastic Hill Climbing
    NOTE: Each algorithm utilizes the following parameters as its constraints:
    :param key: The musical key the chord progression will be in.
    :param isMajor: Determines whether the given key is a major or minor key.
    :param numChords: The number of desired chords in the chord progression.
    :param qualities: A list of desired chord qualities to be included in the chord progression.
    """
    self.key = key
    self.isMajor = isMajor
    self.numChords = numChords
    self.qualities = qualities

    # Class variables that are used in each local search method
    self.tonic = getTonic(isMajor, key)
    self.chord_prog = [] # stores our current solution
    self.used_qualities = {}
    self.remaining_qualities = []
  
  # ----------------------------------------------------------------------------------------------------------------
  # HILL CLIMBING METHODS
  # ----------------------------------------------------------------------------------------------------------------
  
  def hill_climbing(self, method: LSMethod) -> List[Tuple[Note, ChordQuality]]:
    """
    Purpose: Returns a chord progression using the given hill climbing method.
    """
    # Randomly pick numChords amount of notes in the scale of the given key
    self.chord_prog = self.createRandChordProg()
    # Filter through which qualities we still need
    self.getUsedQualities()
    self.getRemainingQualities()
    # Look for neighboring solutions
    if self.remaining_qualities:
      for i, chord in enumerate(self.chord_prog):
        # We replace a chord only if it's quality is not one of the desired qualities, or if it is 
        # one of the desired qualities but we have duplicates
        if self.canReplaceChord(chord):
          successors = self.getSuccessors(chord[0])
          # The cost at each node is the length of remaining_qualities
          self.runEvaluatorMethod(method, i, chord[0], successors)
        if not self.remaining_qualities:
          break
      # If we did not find a solution, run the algorithm again
      if self.remaining_qualities:
        self.runHCMethodAgain(method)
    return self.chord_prog

  def runEvaluatorMethod(self, method: LSMethod, index: int, note: Note, successors: List[ChordQuality]):
    """
    Purpose: Executes the evaluation function for the given method.
    """
    if method == LSMethod.SIMPLE_HC:
      self.simple_hill_climbing_evaluator(index, note, successors)
    elif method == LSMethod.STEEPEST_ASCENT_HC:
      self.steepest_ascent_hill_climbing_evaluator(index, note, successors)
    elif method == LSMethod.STOCHASTIC_HC:
      self.stochastic_hill_climbing_evaluator(index, note, successors)
  
  def runHCMethodAgain(self, method: LSMethod):
    """
    Purpose: Runs a specific hill climbing method given the method.
    """
    if method == LSMethod.SIMPLE_HC:
      return self.simple_hill_climbing()
    elif method == LSMethod.STEEPEST_ASCENT_HC:
      return self.steepest_ascent_hill_climbing()
    elif method == LSMethod.STOCHASTIC_HC:
      return self.stochastic_hill_climbing()
  
  # ----------------------------------------------------------------------------------------------------------------
  # HILL CLIMBING METHODS & EVALUATOR METHODS
  # ----------------------------------------------------------------------------------------------------------------

  def simple_hill_climbing(self) -> List[Tuple[Note, ChordQuality]]:
    """
    Purpose: Returns a chord progression in the given key that contains the given qualities using simple hill climbing.
    """
    return self.hill_climbing(LSMethod.SIMPLE_HC)

  def simple_hill_climbing_evaluator(self, index: int, note: Note, successors: List[ChordQuality]):
    """
    Purpose: The evaluation function for simple hill climbing, which examines each neighboring node and selects the 
    first neighboring node which optimizes the cost (length of remaining_qualities) of the next node.
    """
    for successor in successors:
      if successor in self.remaining_qualities:
        self.chord_prog[index] = (note, successor)
        self.remaining_qualities.remove(successor)
        self.updateUsedQualities(successor)

  def steepest_ascent_hill_climbing(self) -> List[Tuple[Note, ChordQuality]]:
    """
    Purpose: Returns a chord progression in the given key that contains the given qualities using steepest ascent hill climbing.
    """
    return self.hill_climbing(LSMethod.STEEPEST_ASCENT_HC)
  
  def steepest_ascent_hill_climbing_evaluator(self, index: int, note: Note, successors: List[ChordQuality]):
    """
    Purpose: The evaluation function for steepest ascent hill climbing, which examines all neighboring nodes and selects the 
    node closest to the solution state as of next node, i.e. selects the node that minimizes the length of remaining_qualities.
    """
    intersection = set(successors).intersection(self.remaining_qualities)
    if len(intersection) > 0:
      quality = next(iter(intersection))
      self.chord_prog[index] = (note, quality)
      self.remaining_qualities.remove(quality)
      self.updateUsedQualities(quality)

  def stochastic_hill_climbing(self) -> List[Tuple[Note, ChordQuality]]:
    """
    Purpose: Returns a chord progression in the given key that contains the given qualities using stochastic hill climbing.
    """
    return self.hill_climbing(LSMethod.STOCHASTIC_HC)
  
  def stochastic_hill_climbing_evaluator(self, index: int, note: Note, successors: List[ChordQuality]):
    """
    Purpose: The evaluation function for stochastic hill climbing, which selects a neighboring node at random and decides
    whether to move to that node or to examine another.
    """
    while successors:
      quality = random.choice(successors)
      # Remove it from successors so we don't explore it again
      successors.remove(quality)
      if quality in self.remaining_qualities:
        self.chord_prog[index] = (note, quality)
        self.remaining_qualities.remove(quality)
        self.updateUsedQualities(quality)
        break

  # ----------------------------------------------------------------------------------------------------------------
  # HELPER METHODS
  # ----------------------------------------------------------------------------------------------------------------

  def createRandChordProg(self) -> List[Tuple[Note, ChordQuality]]:
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

  def getUsedQualities(self) -> Dict[ChordQuality, int]:
    """
    Purpose: Returns a dictionary whose keys are chord qualities found in the given chord_prog and values are
    the count of those qualities in the chord progression.
    """
    self.used_qualities = {}
    for chord in self.chord_prog:
      if chord[1] in self.used_qualities:
        self.used_qualities[chord[1]] += 1
      else:
        self.used_qualities[chord[1]] = 1
  
  def getRemainingQualities(self) -> List[ChordQuality]:
    """
    Purpose: Returns a list of chord qualities that remain to be assigned in the chord progression.
    """
    self.remaining_qualities = []
    for quality in self.qualities:
      if quality in self.used_qualities:
        used_count = self.used_qualities[quality]
        desired_count = self.qualities.count(quality)
        remaining_count = desired_count - used_count
        if remaining_count > self.remaining_qualities.count(quality):
          self.remaining_qualities.append(quality)
      else:
        self.remaining_qualities.append(quality)

  def getSuccessors(self, note: Note) -> List[ChordQuality]:
    """
    Purpose: Returns a list of successors. A successor is a quality that fits the root note
    in the given key.
    """
    successors = []
    qualities = ChordQuality.getAllQualities()
    for quality in qualities:
      potentialChord = chordInKey(note, quality, self.key, self.isMajor)
      if potentialChord:
        successors.append(quality)
    return successors

  def canReplaceChord(self, chord: Tuple[Note, ChordQuality]) -> bool:
    """
    Purpose: Determines whether or not we can replace the given chord within the chord progression.
    """
    quality = chord[1]
    qualityCount = self.qualities.count(quality)
    # We can replace if the chord doesn't have a desired quality, or if it is a desired quality and we have more
    # than desired
    return (quality not in self.qualities) or (quality in self.used_qualities and self.used_qualities[quality] > qualityCount)
  
  def updateUsedQualities(self, quality: ChordQuality) -> Dict[ChordQuality, int]:
    """
    Purpose: Updates used_qualities dictionary to include the given quality or increase its count.
    """
    if quality in self.used_qualities:
      self.used_qualities[quality] += 1
    else:
      self.used_qualities[quality] = 1

