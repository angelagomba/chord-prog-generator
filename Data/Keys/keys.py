from enum import Enum 

class Key():
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

