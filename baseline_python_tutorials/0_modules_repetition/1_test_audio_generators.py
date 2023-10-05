# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:27:47 2020

@author: user
"""

import audio_utils as au
import sounddevice as sd

play_audio = True
sr = 44100

freq = 440
amp = 0.7

dur = 0.8

# %% noise

s = au.make_noise( amp=amp , dur_secs=dur , sr=sr )
# s = au.make_noise( amp=0.1 )

if play_audio:
    sd.play( s , sr )

# %% sine

s = au.make_sine( freq=freq , amp=amp , phase=0.0 , dur_secs=dur , sr=sr )

if play_audio:
    sd.play( s , sr )

# %% sine with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.5 , dur_secs=dur , sr=sr )
s = au.make_sine_with_adsr( freq=freq , amp=amp , phase=0.0 , adsr=a, sr=sr )

if play_audio:
    sd.play( s , sr )

# %% aliased square with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.3 , dur_secs=dur , sr=sr )
s = au.make_square_aliased_with_adsr( freq=freq , amp=amp , phase=0.0 , adsr=a, sr=sr )

if play_audio:
    sd.play( s , sr )

# %% square with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.3 , dur_secs=dur , sr=sr )
s = au.make_square_with_adsr( freq=freq , amp=amp , phase=0.0 , adsr=a, sr=sr )
'''
import numpy as np
import matplotlib.pyplot as plt
sp = np.fft.fft( s[:1024]*np.hanning(1024) )
plt.plot( np.linspace(0,22050, 512) , np.sqrt( sp[:512].real**2 + sp[:512].imag**2 ) )
'''
if play_audio:
    sd.play( s , sr )

# %% aliased sawtooth with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.3 , dur_secs=dur , sr=sr )
s = au.make_sawtooth_aliased_with_adsr( freq=freq , amp=amp , phase=0.0 , adsr=a, sr=sr )

if play_audio:
    sd.play( s , sr )

# %% sawtooth with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.3 , dur_secs=dur , sr=sr )
s = au.make_sawtooth_with_adsr( freq=5000 , amp=amp , phase=0.0 , adsr=a, sr=sr )

'''
sp = np.fft.fft( s[:1024] )
plt.plot( np.linspace( 0, 22050, 512 ) , np.sqrt( sp[:512].real**2 + sp[:512].imag**2 ) )

play_audio = True
'''

if play_audio:
    sd.play( s , sr )

# %% triangle with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.3 , dur_secs=dur , sr=sr )
s = au.make_triangle_with_adsr( freq=freq , amp=amp , phase=0.0 , adsr=a, sr=sr )

if play_audio:
    sd.play( s , sr )