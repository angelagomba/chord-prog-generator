import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQualities
from Data.keys import Key
from typing import List, Tuple

def getScale(key: Key, isMajor: bool) -> List[str]:
  return key["major"] if isMajor else key["minor"]

def getTonic(isMajor, key=None, scale=None) -> List[str, ChordQualities]:
  if not key and not scale:
    # TODO: What is the best way to raise errors? Temporarily printing for now.
    print('Must call with key or scale.')
    pass
  scale = scale if scale else getScale(key, isMajor)
  return (scale[0], ChordQualities.MAJ if isMajor else ChordQualities.MIN)

def getTonicCount(tonic: Tuple[str, ChordQualities], chord_prog: List[Tuple[str, ChordQualities]]) -> int:
  """
  Purpose: Returns the number of instances of the tonic chord in a chord progression.
  """
  return chord_prog.count(tonic)