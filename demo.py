import os, sys
dir = '/home/x/xiaochan/mandarin_pitch_tracker/pypYIN'
srcpath = dir+'/src'
sys.path.append(srcpath)

import pYINmain
import numpy as np
from YinUtil import RMS
import librosa
import matplotlib.pyplot as plt

filename1 = 'src/a2-cg2.wav'
frameSize = 2048
hopSize = 256

audio, fs = librosa.load(filename1, sr=None)


pYinInst = pYINmain.PyinMain()
pYinInst.initialise(channels = 1, inputSampleRate = fs, stepSize = hopSize, blockSize = frameSize,
                   lowAmp = 0.25, onsetSensitivity = 0.7, pruneThresh = 0.1)

pYinInst.m_yin.m_yinBufferSize = int(frameSize/2)
all_frames = librosa.util.frame(audio, frame_length=frameSize, hop_length=hopSize)

for frame in all_frames.T:
    fs = pYinInst.process(frame)
    
monoPitch = pYinInst.getSmoothedPitchTrack()

# output smoothed pitch track
print("Pitch track")
for ii in fs.m_oSmoothedPitchTrack:
    print(ii.values)
print ('\n')

fs = pYinInst.getRemainingFeatures(monoPitch)

# output of mono notes,
# column 0: frame number,
# column 1: pitch in midi number, this is the decoded pitch
# column 2: attack 1, stable 2, silence 3
print('mono note decoded pitch')
for ii in fs.m_oMonoNoteOut:
    print(ii.frameNumber, ii.pitch, ii.noteState)
print('\n')

print('note pitch tracks')
for ii in fs.m_oNotePitchTracks:
    print(ii)
print('\n')

# median pitch in Hz of the notes
print('median note pitch')
for ii in fs.m_oNotes:
    print(ii.values)
print('\n')