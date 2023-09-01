from mido import Message, MidiFile, Parser #to handle midi files
import pypianoroll #to visualize midi files
import matplotlib.pyplot as plt

greeting = "Welcome to AutoAnalysis pre-alpha! Please upload a midi file to analyze."
print(greeting)

#import midi file
mid = MidiFile('./test midi files/czerny_299_1.midi')
sound = Message('note_on')
rest = Message('note_off')
parser = Parser()

#print all midi messages in file BEFORE graphing it out
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for sound in track:
        print(sound)
        print(rest)


#print piano roll of file (visualize)
# print("Here is the piano roll of the midi file you uploaded:")
# multitrack = pypianoroll.read('./test midi files/prelude04.midi')
# multitrack.plot()
# plt.show()

