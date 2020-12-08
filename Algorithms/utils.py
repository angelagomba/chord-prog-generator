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

def chordInKey(root: Note, quality: ChordQualities, key: Key, isMajor: bool) -> Tuple[Note, ChordQualities] or None:
  root_note = Note.getNoteName(root)
  root_scale = Key.getScale(Key.getKey(root_note), isMajor)
  isInKey = True
  intervals = ChordQualities.getIntervals(quality)
  for interval in intervals:
    note = ''
    interval = str(interval)
    if 'b' in interval:
      temp = Note.getNote(root_scale[int(interval[-1]) - 1])
      note = Note.getNote(Note.getFlats(temp)[0])
    else: 
      note = Note.getNote(root_scale[int(interval) - 1])
    if not inKey(note, key, isMajor):
      isInKey = False
      break
  if isInKey: 
    return (root, quality)
  return None

def parseChordProg(prog: List[Tuple[Note, ChordQualities]]):
  parsed_chord_prog = []
  for chord in prog:
    parsed_chord = ''
    parsed_chord += Note.getNoteName(chord[0])
    parsed_chord += chord[1].name
    parsed_chord_prog.append(parsed_chord)
  return parsed_chord_prog





