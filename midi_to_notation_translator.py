from mido import MidiFile

mid = MidiFile('./test midi files/Nocturne-in-E-Flat-Opus-9-Nr-2.midi')

def get_key_sig(mid):
    key = None
    for msg in mid:
        if msg.is_meta and hasattr(msg, 'key'):
            key = msg.key
    return key

# Converts midi note values to their corresponding note names
def midi_to_note_name(midi_note):
    key_sig = get_key_sig(mid)
    # Define the list of note names
    note_names = ['C', ['C#', "D-"], 'D', ['D#', 'E-'], 'E', 'F', ['F#', 'G-'], 'G', ['G#', 'A-'], 'A', ['A#', "B-"], 'B']
    
    # Calculate the octave and note index
    octave = midi_note // 12 - 1
    note_index = midi_note % 12
    
    global note_name
    # Construct the note name
    if isinstance(note_names[note_index], list):
        if key_sig and ('b' in key_sig):
            note_name = f"{note_names[note_index][1]}{octave}"
        elif key_sig and ('#' in key_sig):
            note_name = f"{note_names[note_index][0]}{octave}"
    else:
        note_name = f"{note_names[note_index]}{octave}"
    return note_name