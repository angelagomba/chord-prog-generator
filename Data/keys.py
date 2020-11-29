from enum import Enum 
from typing import List

class Key(Enum):
  """
  An enum that represents different keys and their major and minor scales.
  TODO: Minor scales
  """

  C_FLAT = {"major":["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"], "minor":[]}
  C = {"major":["C", "D", "E", "F", "G", "A", "B"], "minor": []}
  C_SHARP = {"major":["C#", "D#", "E#", "F#", "G#", "A#", "B#"], "minor":[]}
  D_FLAT = {"major":["Db", "Eb", "F", "Gb", "Ab", "C"], "minor":[]}
  D = {"major":["D", "E", "F#", "G", "A", "B", "C#"], "minor":[]}
  D_SHARP = {"major":["D#", "E#", "F##", "G#", "A#", "B#", "C##"], "minor":[]}
  E_FLAT = {"major":["Eb", "F", "G", "Ab", "Bb", "C", "D"], "minor":[]}
  E = {"major":["E", "F#", "G#", "A", "B", "C#", "D#"], "minor":[]}
  E_SHARP = {"major":["E#", "F##", "G##", "A#", "B#", "C##", "D##"], "minor":[]}
  F_FLAT = {"major":["Fb", "Gb", "Ab", "Bbb", "Cb", "Db", "Eb"], "minor": []}
  F = {"major":["F", "G", "A", "Bb", "C", "D", "E"], "minor":[]}
  F_SHARP = {"major":["F#", "G#", "A#", "B", "C#", "D#", "E#"], "minor":[]}
  G_FLAT = {"major":["Gb", "Ab", "Bb", "Cb", "Eb", "F"], "minor":[]}
  G = {"major":["G", "A", "B", "C", "D", "E", "F#"], "minor":[]}
  G_SHARP = {"major":["G#", "A#", "B#", "C#", "D#", "E#", "F##"], "minor":[]}
  A_FLAT = {"major":["Ab", "Bb", "C", "Db", "Eb", "F", "G"], "minor":[]}
  A = {"major":["A", "B", "C#", "D", "E", "F#", "G#"], "minor":[]}
  A_SHARP = {"major":["A#", "B#", "C##", "D#", "E#", "F##", "G##"], "minor":[]}
  B_FLAT = {"major":["Bb", "C", "D", "Eb", "F", "G", "A"], "minor":[]}
  B = {"major":["B", "C#", "D#", "E", "F#", "G#", "A#"], "minor":[]}
  B_SHARP = {"major":["B#", "C##", "D##", "E#", "F##", "G##", "A##"], "minor":[]}

  @staticmethod
  def getKeys():
    """
    Purpose: Returns a list of all the keys
    """
    return [Key.C_FLAT, Key.C, Key.C_SHARP, Key.D_FLAT, Key.D, Key.D_SHARP, Key.E_FLAT, Key.E, Key.E_SHARP, Key.F_FLAT, Key.F, Key.F_SHARP, Key.G_FLAT, Key.G, Key.G_SHARP, Key.A_FLAT, Key.A, Key.A_SHARP, Key.B_FLAT, Key.B, Key.B_SHARP ]

  @staticmethod
  def getKey(root: str):
    """
    Purpose: Returns the Key that has the given root 
    """
    for key in Key.getKeys():
      key_val = key.value
      if key_val['major'][0] == root:
        return key

  @staticmethod
  def getScale(key, isMajor):
    """
    Purpose: Returns the scale of the given key
    """
    key_val = key.value
    return key_val["major"] if isMajor else key_val["minor"]

