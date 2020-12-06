import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQualities
from Data.keys import Key
from Data.notes import Note
from typing import List, Tuple

def getTonic(isMajor, key=None, scale=None) -> Tuple[str, ChordQualities]:
  """
  Purpose: Returns the tonic of the given key or scale 
  """
  if not key and not scale:
    print('Must call with key or scale.')
    pass
  scale = scale if scale else Key.getScale(key, isMajor)
  return (Note.getNote(scale[0]), ChordQualities.MAJ if isMajor else ChordQualities.MIN)

def getTonicCount(tonic: Tuple[str, ChordQualities], chord_prog: List[Tuple[str, ChordQualities]]) -> int:
  """
  Purpose: Returns the number of instances of the tonic note in a chord progression.
  """
  tonic_note = tonic[0]
  notes = [chord[0] for chord in chord_prog]
  return notes.count(tonic_note)

def inKey(note: Note, key: Key, isMajor: bool) -> bool:
  """
  Purpose: Returns a boolean determining whether the given Note is in the key of the given key.
  """
  note_reps = Note.getEquals(note)
  return not set(note_reps).isdisjoint(Key.getScale(key, isMajor))


