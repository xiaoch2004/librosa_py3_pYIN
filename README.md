# librosa_py3_pYIN
python3 pYIN based on librosa and numpy 

- A python version of pYIN of Matthias Mauch  
- Pitch and note tracking in monophonic audio

## About the pYIN algorithm 
- pYIN is a pitch tracking algorithm proposed by Matthias Mauch in [this paper](https://www.eecs.qmul.ac.uk/~simond/pub/2014/MauchDixon-PYIN-ICASSP2014.pdf)
- You may refer to the pYIN project page at [https://code.soundsoftware.ac.uk/projects/pyin](https://code.soundsoftware.ac.uk/projects/pyin) for more details

## About this repo
This repository is mostly based on [pypyin](https://github.com/ronggong/pypYIN). The origin repo is written in python 2 and requires essentia(not available in windows). I made two changes to the original repo:
- Substitute essentia with librosa, which is eaiser to install.
- Change all python 2 syntax to python 3

## Dependencies
- Numpy  
- Librosa

## Usage
```
python demo.py
```
or
```
from pyin import pyin
pitch, _ = pyin(audio, inputSampleRate=None)
```

