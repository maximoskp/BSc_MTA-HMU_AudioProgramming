# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:12:23 2020

@author: user
"""

import librosa
import audio_utils as au
import soundfile as sf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# example: random composition
# initialise composition of 10 secs
composition_duration = 10
sr = 44100
composition_samples = composition_duration*sr
c = np.zeros( ( composition_samples , 2 ) )
# let's place a number of notes randomly
n = 5000
for i in range( n ):
    # random note
    f = np.random.randint(50, 5000)
    a = np.random.random()
    tmp_adsr = au.make_adsr( dur_secs = np.random.random() + 0.5 )
    d = np.random.randint(0,10)
    if d <= 6:
        r = au.make_sine_with_adsr(freq=f, amp=a/1000, adsr=tmp_adsr)
    elif d <= 7:
        r = au.make_square_with_adsr(freq=f, amp=a, adsr=tmp_adsr)
    elif d <= 8:
        r = au.make_sawtooth_with_adsr(freq=f, amp=a, adsr=tmp_adsr)
    elif d <= 9:
        r = au.make_triangle_with_adsr(freq=f, amp=a, adsr=tmp_adsr)
    # place note randomly within the composition
    tmp_idx = np.random.randint(composition_samples - 44100-22050)
    # apply random panning
    tmp_pan = np.random.random()
    c[ tmp_idx:(tmp_idx+r.size) , 0 ] += tmp_pan*r
    c[ tmp_idx:(tmp_idx+r.size) , 1 ] += (1-tmp_pan)*r

# normalize
c = c / np.max( np.abs( c ) )
sf.write('audio_files/random_composition.wav', c, 44100, 'PCM_24')