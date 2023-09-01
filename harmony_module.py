from music21 import chord, note
from mido import MidiFile, Message
from midi_to_notation_translator import *

mid = MidiFile('./test midi files/czerny_299_1.midi')
key_sig = get_key_sig(mid)


# find the chords present in the midi file
def find_chords(file):
    chords = []
    current_chord_notes =[]
    current_chord_start_time = None
    for msg in file.tracks[1]:
        if not msg.is_meta and hasattr(msg, 'note'):
            midi_note = msg.note
            midi_to_note_name(midi_note)
            note_name = midi_to_note_name(midi_note)
            if msg.time > 0:
                if current_chord_notes:
                    chord_obj = chord.Chord(current_chord_notes)
                    chords.append(chord_obj)
                current_chord_start_time = msg.time
                current_chord_notes = [note_name]
            elif msg.time == 0:
                current_chord_notes.append(note_name)

    #print(current_chord_notes)
    print(chords)

find_chords(mid)