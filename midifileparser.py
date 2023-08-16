from mido import MidiFile, MetaMessage, Message
import pypianoroll
import matplotlib.pyplot as plt

# import midi file
mid = MidiFile('./test midi files/prelude04.midi')
msg = Message('note_on')

def read_midi_file(file_path):
    try:
        midi_file = mid
        return midi_file
    except IOError as e:
        print(f"Error reading MIDI file: {e}")
        return None

#Identify key of piece:)
key = ' '
for i in mid:
    if i.is_meta and hasattr(i, "key"):
        key = i.key

print(f'The file you\'ve uploaded is in the key of {key}.')

#Chord class to identify individual chords
class Chord:
    def __init__(self, root_note, chord_type, duration):
        self.root_note = root_note
        self.chord_type = ['major', 'minor', 'diminished', 'dominant 7th', 'half-diminished']
        self.duration = duration
    
#     def __str__(self) -> str:
#         return f"Chord: {self.root_note} {self.chord_type}, Duration: {self.duration}"
        
# # Converts midi note values to their corresponding note names
# def midi_to_note_name(midi_note):
#     # Define the list of note names
#     note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
#     # Calculate the octave and note index
#     octave = midi_note // 12 - 1
#     note_index = midi_note % 12
    
#     # Construct the note name
#     note_name = f"{note_names[note_index]}{octave}"
    
#     return note_name

# # prints all the note values of the messages that don't equal 0
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         if not msg.is_meta and hasattr(msg, 'note'):
#             midi_note = msg.note
#             note_name = midi_to_note_name(midi_note)
#             print(f"MIDI Note: {midi_note}, Note Name: {note_name}")

# class Chord:
#     def __init__(self, root_note, chord_type, duration):
#         self.root_note = root_note
#         self.chord_type = chord_type
#         self.duration = duration
    
#     def __str__(self) -> str:
#         return f"Chord: {self.root_note} {self.chord_type}, Duration: {self.duration}"

# print piano roll of file
# multitrack = pypianoroll.read('./test midi files/sonate_01_(c)hisamori.midi')
# multitrack.plot()
# plt.show()