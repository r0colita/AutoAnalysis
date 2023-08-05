from mido import Message, MidiFile, Parser #to handle midi files
import pypianoroll #to visualize midi files
import matplotlib.pyplot as plt

greeting = "Welcome to AutoAnalysis pre-alpha! Please upload a midi file to analyze."
#print(greeting)

#import midi fileg
mid = MidiFile('./test midi files/sonate_01_(c)hisamori.midi')
msg = Message('note_on')
parser = Parser()

#print all midi messages in file
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

#print piano roll of file (visualize)
multitrack = pypianoroll.read('./test midi files/sonate_01_(c)hisamori.midi')
multitrack.plot()
#plt.show()

