# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:08:28 2020

@author: user
"""

import librosa
import audio_utils as au
import soundfile as sf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

filename = 'audio_files/celloSampleStereo.wav'

y, sr = librosa.load(filename)

# to following function already applies a hanning window to the grain
# create a new function or expand this function by adding an argument
# describing the window type, if you want a different envolope
p = au.get_stereo_random_part( y , s=0 , e=22050 , d_min=1000 , d_max=2000 , pan=0.9 )
# here you could apply speed/pitch change on the isolated grain or
# you could create a new function, expanding get_stereo_random_part
# to include an argument that describes speed/pitch alteration

sf.write('audio_files/result.wav', p, 44100, 'PCM_24')

sd.play(p, sr)

plt.subplot(211)
plt.plot( np.arange( p.shape[0] ) , p[:,0] )
axes = plt.gca()
axes.set_ylim([-1,1])
plt.subplot(212)
plt.plot( np.arange( p.shape[0] ) , p[:,1] )
axes = plt.gca()
axes.set_ylim([-1,1])

