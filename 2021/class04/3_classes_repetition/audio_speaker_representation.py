# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 07:57:14 2021

@author: user
"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import audio_file_representation as afr

class AudioSpeakerRepresentation(afr.AudioFileRepresentation):
    
    def __init__(self, file_path, sr=44100, keep_audio=False):
        super().__init__(self, file_path, sr=44100, keep_audio=False)
        # keep name for further processing
        self.name = file_path.split( '\\' )[-1]
        self.extract_speaker_information()
    # end init
    
    def extract_speaker_information(self):
        useful_name = self.name.split('.')[0]
        splt = useful_name.split('-')
        self.actor_ID = splt[-1]
        self.female = int(self.actor_ID)%2 == 0
    # end extract_speaker_information
# end AudioSpeakerRepresentation

'''
Filename identifiers

    Modality (01 = full-AV, 02 = video-only, 03 = audio-only).

    Vocal channel (01 = speech, 02 = song).

    Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).

    Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.

    Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").

    Repetition (01 = 1st repetition, 02 = 2nd repetition).

    Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).

Filename example: 03-01-06-01-02-01-12.wav

    Audio-only (03)
    Speech (01)
    Fearful (06)
    Normal intensity (01)
    Statement "dogs" (02)
    1st Repetition (01)
    12th Actor (12)
    Female, as the actor ID number is even.
'''