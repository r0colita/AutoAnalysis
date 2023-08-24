from mido import MidiFile, MetaMessage, Message
import pypianoroll
import matplotlib.pyplot as plt

# import midi file
mid = MidiFile('./test midi files/czerny_299_1.midi')
msg = Message('note_on')

#print meta message
# for message in mid:
#     if message.is_meta:
#         print(message)

#Extract key signature from meta message
key = ' '
for i in mid:
    if i.is_meta and hasattr(i, "key"):
        key = i.key
print(f'The file you\'ve uploaded is in the key of {key}.')

# Chord class to identify individual chords
class Chord:
    def __init__(self, root_note, chord_type, start_time):
        self.root_note = root_note
        self.chord_type = ['major', 'minor']
        self.start_time = start_time

    def set_duration(self, end_time):
        self.duration = end_time - self.start_time
    
    def get_chord_type(self, intervals):
        pass
    
    def __str__(self) -> str:
        return f"Chord: {self.root_note} {self.chord_type}, Duration: {self.duration}"
    
# Find chords by time simultaneity and store them in a list
chords= []
current_chord = None
accumulated_time = 0

for msg in mid.tracks[1]:
    accumulated_time += msg.time
    if not msg.is_meta and hasattr(msg, 'note'):
        if msg.type == 'note_on':
            if current_chord:
                # Finalize the previous chord
                current_chord.set_duration(accumulated_time)
                chords.append(current_chord)
            current_chord = Chord([msg.note], msg.time, accumulated_time)
        elif msg.type == 'note_off' and current_chord:
            current_chord.notes.append(msg.note)
 
# Finalize the last chord if it exists
if current_chord:
    current_chord.set_duration(accumulated_time)
    chords.append(current_chord)

# Print the detected chords
for chord in chords:
    print(chord)
        
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



# print piano roll of file
# multitrack = pypianoroll.read('./test midi files/czerny_299_1.midi')
# multitrack.plot()
# plt.show()