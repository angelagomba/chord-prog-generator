import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Algorithms.local_search import local_search
from Data.qualities import ChordQualities
from Data.keys import Key

class LocalSearchTests(unittest.TestCase):

  def test_chord_prog_length(self):
    """
    Purpose: Ensures that the chord progression returned has the correct length.
    """
    chord_prog = local_search(Key.C, True, 4, [])
    # NOTE: Temp way for us to see our result
    print(chord_prog)
    self.assertEqual(len(chord_prog), 4)

if __name__ == '__main__':
    unittest.main()