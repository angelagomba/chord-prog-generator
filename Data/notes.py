from enum import Enum
from typing import List

class Note(Enum):

  # C
  C_DFLAT = {"note": "Cbb", "flats": ["Bbb", "A", "G##"], "equals": ["Cbb", "Bb", "A#"]}
  C_FLAT = {"note": "Cb", "flats": ["Cbb", "Bb", "A#"], "equals": ["Cb", "B", "A##"]}
  C = {"note": "C", "flats": ["Cb", "B", "A##"], "equals": ["Dbb", "C", "B#"]}
  C_SHARP = {"note": "C#", "flats": ["Dbb", "C", "B#"], "equals": ["Db", "C#","B##"]}
  C_DSHARP = {"note": "C##", "flats": ["Db", "C#","B##"], "equals": ["Ebb", "D", "C##"]}

  # D
  D_DFLAT = {"note": "Dbb", "flats": ["Cb", "B", "A##"], "equals": ["Dbb", "C", "B#"]}
  D_FLAT = {"note": "Db", "flats": ["Dbb", "C", "B#"], "equals": ["Db", "C#", "B##"]}
  D = {"note": "D", "flats": ["Db", "C#", "B##"], "equals": ["Ebb", "D", "C##"]}
  D_SHARP = {"note": "D#", "flats": ["Ebb", "D", "C##"], "equals": ["Fbb", "Eb", "D#"]}
  D_DSHARP = {"note": "D##", "flats": ["Fbb", "Eb", "D#"], "equals": ["Fb", "E", "D##"]}

  # E
  E_DFLAT = {"note": "Ebb", "flats": ["Db", "C#", "B##"], "equals": ["Ebb", "D","C##"]}
  E_FLAT = {"note": "Eb", "flats": ["Ebb", "D","C##"], "equals": ["Fbb", "Eb", "D#"]}
  E = {"note": "E", "flats": ["Fbb", "Eb", "D#"], "equals": ["Fb", "E", "D##"]}
  E_SHARP = {"note": "E#", "flats": ["Fb", "E", "D##"], "equals": ["Gbb","F", "E#"]}
  E_DSHARP = {"note": "E##", "flats": ["Gbb","F", "E#"], "equals": ["Gb", "F#", "E##"]}

  # F
  F_DFLAT = {"note": "Fbb", "flats": ["Ebb", "D", "C##"], "equals": ["Fbb" ,"Eb", "D#"]}
  F_FLAT = {"note": "Fb", "flats": ["Fbb" ,"Eb", "D#"], "equals": ["Fb", "E", "D##"]}
  F = {"note": "F", "flats": ["Fb", "E", "D##"], "equals": ["Gbb", "F", "E#"]}
  F_SHARP = {"note": "F#", "flats": ["Gbb", "F", "E#"], "equals": ["Gb", "F#", "E##"]}
  F_DSHARP = {"note": "F##", "flats": ["Gb", "F#", "E##"], "equals": ["Abb", "G", "F##"]}

  # G
  G_DFLAT = {"note": "Gbb", "flats": ["Fb", "E", "D#"], "equals": ["Gbb", "F", "E#"]}
  G_FLAT = {"note": "Gb", "flats": ["Gbb", "F", "E#"], "equals": ["Gb", "F#", "E##"]}
  G = {"note": "G", "flats": ["Gb", "F#", "E##"], "equals": ["Abb", "G", "F##"]}
  G_SHARP = {"note": "G#", "flats": ["Abb", "G", "F##"], "equals": ["G#", "Ab"]}
  G_DSHARP = {"note": "G##", "flats": ["G#", "Ab"], "equals": ["Bbb", "A", "G##"]}

  # A
  A_DFLAT = {"note": "Abb", "flats": ["Gb", "F#", "E##"], "equals": ["Abb", "G", "F##"]}
  A_FLAT = {"note": "Ab", "flats": ["Abb", "G", "F##"], "equals": ["Ab", "G#"]}
  A = {"note": "A", "flats": ["Ab", "G#"], "equals": ["Bbb", "A", "G##"]}
  A_SHARP = {"note": "A#", "flats": ["Bbb", "A", "G##"], "equals": ["Cbb", "Bb", "A#"]}
  A_DSHARP = {"note": "A##", "flats": ["Cbb", "Bb", "A#"], "equals": ["B", "A##"]}

  # B
  B_DFLAT = {"note": "Bbb", "flats": ["Ab", "G#"], "equals": ["Bbb", "A", "G##"]}
  B_FLAT = {"note": "Bb", "flats": ["Bbb", "A", "G##"], "equals": ["Cbb", "Bb", "A#"]}
  B = {"note": "B", "flats": ["Cbb", "Bb", "A#"], "equals": ["B", "A##"]}
  B_SHARP = {"note": "B#", "flats": ["B", "A##"], "equals": ["Dbb", "C", "B#"]}
  B_DSHARP = {"note": "B##", "flats": ["Dbb", "C", "B#"], "equals": ["Db", "C#", "B##"]}

  @staticmethod
  def getNotes():
    """
    Purpose: Returns a list of every note representation
    """
    return [Note.C_DFLAT, Note.C_FLAT, Note.C, Note.C_SHARP, Note.C_DSHARP, 
            Note.D_DFLAT, Note.D_FLAT, Note.D, Note.D_SHARP, Note.D_DSHARP, 
            Note.E_DFLAT, Note.E_FLAT, Note.E, Note.E_SHARP, Note.E_DSHARP, 
            Note.F_DFLAT, Note.F_FLAT, Note.F, Note.F_SHARP, Note.F_DSHARP,
            Note.G_DFLAT, Note.G_FLAT, Note.G, Note.G_SHARP, Note.G_DSHARP,
            Note.A_DFLAT, Note.A_FLAT, Note.A, Note.A_SHARP, Note.A_DSHARP,
            Note.B_DFLAT, Note.B_FLAT, Note.B, Note.B_SHARP, Note.B_DSHARP]

  @staticmethod
  def getNote(note): 
    """
    Purpose: Returns the Note enum representation that matches the given note. If it doesn't find one, it returns None.
    """
    notes = Note.getNotes()
    for curr_note in notes:
      cur_note_val = curr_note.value
      if cur_note_val["note"] == note:
        return cur_note_val
    return None

  @staticmethod
  def getNoteName(note):
    """
    Purpose: Returns the Note string representation that matches the given note. If it doesn't find one, it returns None.
    """
    return note["note"]
  
  @staticmethod
  def getFlats(note):
    """
    Purpose: Returns a list of all the note representations for a given note's flat.
    """
    return note["flats"]

  @staticmethod
  def getEquals(note):
    return note["equals"] 


