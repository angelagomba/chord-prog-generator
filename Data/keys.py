from enum import Enum 
from typing import List

class Key(Enum):
  """
  An enum that represents different keys and their major and minor scales.
  """

  C_FLAT = {"major":["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"], "minor":["Cb", "Db", "Ebb", "Fb", "Gb", "Abb", "Bbb"]}
  C = {"major":["C", "D", "E", "F", "G", "A", "B"], "minor": ["C", "D", "Eb", "F", "G", "Ab", "Bb"]}
  C_SHARP = {"major":["C#", "D#", "E#", "F#", "G#", "A#", "B#"], "minor":["C#", "D#", "E", "F#", "G#", "A", "B"]}
  D_FLAT = {"major":["Db", "Eb", "F", "Gb", "Ab", "C"], "minor":["Db", "Eb", "Fb", "Gb", "Ab", "Bbb", "Cb"]}
  D = {"major":["D", "E", "F#", "G", "A", "B", "C#"], "minor":["D", "E", "F", "G", "A", "Bb", "C"]}
  D_SHARP = {"major":["D#", "E#", "F##", "G#", "A#", "B#", "C##"], "minor":["D#", "E#", "F#", "G#", "A#", "B", "C#"]}
  E_FLAT = {"major":["Eb", "F", "G", "Ab", "Bb", "C", "D"], "minor":["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"]}
  E = {"major":["E", "F#", "G#", "A", "B", "C#", "D#"], "minor":["E", "F#", "G", "A", "B", "C", "D"]}
  E_SHARP = {"major":["E#", "F##", "G##", "A#", "B#", "C##", "D##"], "minor":["E#", "F##", "G#", "A#", "B#", "C#", "D#"]}
  F_FLAT = {"major":["Fb", "Gb", "Ab", "Bbb", "Cb", "Db", "Eb"], "minor": ["Fb", "Gb", "Abb", "Bbb", "Cb", "Dbb", "Eb"]}
  F = {"major":["F", "G", "A", "Bb", "C", "D", "E"], "minor":["F", "G", "Ab", "Bb", "C", "Dd", "Eb"]}
  F_SHARP = {"major":["F#", "G#", "A#", "B", "C#", "D#", "E#"], "minor":["F#", "G#", "A", "B", "C#", "D", "E"]}
  G_FLAT = {"major":["Gb", "Ab", "Bb", "Cb", "Eb", "F"], "minor":["Gb", "Ab", "Bbb", "Cb", "Db", "Ebb", "Fb"]}
  G = {"major":["G", "A", "B", "C", "D", "E", "F#"], "minor":["G", "A", "Bb", "C", "D", "Eb", "F"]}
  G_SHARP = {"major":["G#", "A#", "B#", "C#", "D#", "E#", "F##"], "minor":["G#", "A#", "B", "C#", "D#", "E", "F#"]}
  A_FLAT = {"major":["Ab", "Bb", "C", "Db", "Eb", "F", "G"], "minor":["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb"]}
  A = {"major":["A", "B", "C#", "D", "E", "F#", "G#"], "minor":["A", "B", "C", "D", "E", "F", "G"]}
  A_SHARP = {"major":["A#", "B#", "C##", "D#", "E#", "F##", "G##"], "minor":["A#", "B#", "C#", "D#", "E#", "F#", "G#"]}
  B_FLAT = {"major":["Bb", "C", "D", "Eb", "F", "G", "A"], "minor":["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"]}
  B = {"major":["B", "C#", "D#", "E", "F#", "G#", "A#"], "minor":["B", "C#", "D", "E", "F#", "G", "A"]}
  B_SHARP = {"major":["B#", "C##", "D##", "E#", "F##", "G##", "A##"], "minor":["B#", "C##", "D#", "E#", "F##", "G#", "A#"]}

  @staticmethod
  def getKeys():
    """
    Purpose: Returns a list of all the keys
    """
    return [key for key in Key]

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

