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
    # TODO: What is the best way to raise errors? Temporarily printing for now.
    print('Must call with key or scale.')
    pass
  scale = scale if scale else Key.getScale(key, isMajor)
  # TODO: Check if there is a difference in tonics between major and minor
  return (scale[0], ChordQualities.MAJ if isMajor else ChordQualities.MIN)

def getTonicCount(tonic: Tuple[str, ChordQualities], chord_prog: List[Tuple[str, ChordQualities]]) -> int:
  """
  Purpose: Returns the number of instances of the tonic chord in a chord progression.
  """
  return chord_prog.count(tonic)

def inKey(note: Note, key: Key, isMajor: bool) -> bool:
  """
  Purpose: Returns a boolean determining whether the given Note is in the key of the given key.
  """
  note_reps = Note.getEquals(note)
  return not set(note_reps).isdisjoint(Key.getScale(key, isMajor))


