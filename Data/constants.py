import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Data.qualities import ChordQuality

"""
Purpose: A file to store different constants that don't require an Enum class.
"""

diatonic_seq = [ChordQuality.MAJ, ChordQuality.MIN, ChordQuality.MIN, ChordQuality.MAJ, ChordQuality.MAJ, ChordQuality.MIN, ChordQuality.DIM]


