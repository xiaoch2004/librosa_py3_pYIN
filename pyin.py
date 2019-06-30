import os, sys
dir = os.path.dirname(os.path.realpath(__file__))
srcpath = dir + '/src'
sys.path.append(srcpath)

import pYINmain
import numpy as np
from YinUtil import RMS
import librosa
import matplotlib.pyplot as plt
import time

def pyin(filename, inputSampleRate=44100, channels=1, frame_length=2048, hop_length=256, lowAmp=0.25, onsetSensitivity=0.7, pruneThresh=0.1):
    audio, fs = librosa.load(filename, sr=inputSampleRate)
    pYinInst = pYINmain.PyinMain()
    pYinInst.initialise(channels = channels, inputSampleRate = inputSampleRate, stepSize = hop_length, blockSize = frame_length,
                   lowAmp = lowAmp, onsetSensitivity = onsetSensitivity, pruneThresh = pruneThresh)
    
    pYinInst.m_yin.m_yinBufferSize = int(frame_length/2)
    all_frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=hop_length)
    rmslist = []
    
    for frame in all_frames.T:
        fs, rms = pYinInst.process(frame)
        rmslist.append(rms)
    
    monoPitch = pYinInst.getSmoothedPitchTrack()
    pitchlist = [ii.values for ii in fs.m_oSmoothedPitchTrack]
    
    return np.array(pitchlist), np.array(rmslist)

if __name__ == "__main__":
    pitch, _ = pyin('src/oboe-a4.wav')
    print(pitch.ravel())
