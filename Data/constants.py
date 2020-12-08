import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQualities

"""
Purpose: A file to store different constants that don't require an Enum class.
"""

diatonic_seq = [ChordQualities.MAJ, ChordQualities.MIN, ChordQualities.MIN, ChordQualities.MAJ, ChordQualities.MAJ, ChordQualities.MIN, ChordQualities.DIM]


