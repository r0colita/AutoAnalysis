import pandas as pd
from music21 import *
from mido import Message
from midi_to_notation_translator import get_key_sigs

razumovsky = corpus.parse('beethoven/opus59no1/movement1')
# Define file to be searched
czerny = converter.parse('./test midi files/czerny_299_1.midi')



# find the chords present in the midi file
def generate_roman_numerals(part):
    keys = get_key_sigs(part)
    chords = part.chordify(removeRedundantPitches=True)
    numeral_list = []

    for measure in chords.getElementsByClass(stream.Measure):
        measure_chords = []
        
        for c in measure.flatten().getElementsByClass(chord.Chord):
            rn = roman.romanNumeralFromChord(c, keys)
            measure_chords.append(rn.figure)
    
        numeral_list.append(measure_chords)
    return numeral_list


#help(key.Key)
print(generate_roman_numerals(razumovsky))