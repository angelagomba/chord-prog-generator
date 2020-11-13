"""
We will leverage this algorithm to build a chord progression of length numChords that contain each chord quality specified in qualities. 
We will start off with a randomly generated chord progression and iteratively move to a neighboring solution until we have a solution 
that meets the constraints of the CSP. If our initial candidate solution does not include all the chord qualities in qualities, 
then we will iterate through the chord progression and find a neighboring solution where we change our current chord to a chord 
with a chord quality listed in qualities. If we reach the end of the chord progression and are unable to meet all the constraints, 
we start the algorithm again with another randomly generated chord progression. Since local search does not guarantee completeness, 
we will return the solution we have, whether complete or incomplete, before the end of the timeout.
"""

def local_search(qualities, chords, key):
  """Returns a chord progression made up of the given chords.

    # TODO: Some of the types in the signature below can probably be represented as Enums.
    string[], string[][], string -> string[][]

    arguments:
    qualities -- The chord qualities the chord progression must have.
    chords -- The chords within the given key.
    key -- The key the chord progression is in.
  """
  # TODO: Implement local_search for finding a chord progression with the given constraints.

