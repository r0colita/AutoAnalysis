import pandas as pd
from music21 import *
from midi_to_notation_translator import get_key_sigs
from timeit import timeit

razumovsky = corpus.parse('beethoven/opus59no1/movement1')
# Define file to be searched
czerny = converter.parse('./test midi files/czerny_299_1.midi')



# find the chords present in the midi file

"""
    generate_roman_numerals() function results:

    CZERNY TEST:
        Execution time: 0.50s
        Staff count: 2
        Measure count: 27

    RAZUMOVSKY TEST:
        Execution time: 11.22 seconds
        Staff count: 4
        Measure count: 400
"""
# Time complexity: O(N^2)
def generate_roman_numerals(part):
    keys = get_key_sigs(part)
    chords = part.chordify(removeRedundantPitches=True).flatten(retainContainers=True).getElementsByClass(chord.Chord)
    numeral_list = [] # could be more efficient with a hash map

    # iterate through the stream.Score to get the measures
    for i in chords:
        rn = roman.romanNumeralFromChord(i, keys)
        numeral_list.append(rn.romanNumeral)

    return numeral_list

# function to find the harmonic outline of the piece and point out new tonics
def find_harmonic_outline(romans):
    pass


# use of timeit to measure runtime in seconds
time_taken = timeit('generate_roman_numerals(czerny)', globals=globals(), number=1)
print("Time taken:", time_taken)