#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:49:04 2022

@author: max
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

import audio_utils as au

sr = 44100

dur = 3
freq = 100
amp = 0.4


'''
t = np.arange( dur*sr )/sr
s = amp*np.sin( 2*np.pi* freq *t )

'''

'''
# CAUTION: aliasing if (i+2)*freq > sr/2
for i in range(10):
    amp /= 2
    freq1 = (i+2)*freq
    print('i: ' + str(i) + ' - amp: ' + str(amp) + ' - freq1: ' + str(freq1))
    s += amp*np.sin( 2*np.pi* freq1 *t )
'''

'''
i = 2
freq1 = i*freq
while i*freq < sr/2:
    amp /= 2
    print('i: ' + str(i) + ' - amp: ' + str(amp) + ' - freq1: ' + str(freq1))
    s += amp*np.sin( 2*np.pi* freq1 *t )
    i += 1
    freq1 = i*freq
'''

def make_sawtooth( freq=440, amp=0.7, dur=1, sr=44100 ):
    t = np.arange( dur*sr )/sr
    s = amp*np.sin( 2*np.pi* freq *t )
    i = 2
    freq1 = i*freq
    while i*freq < sr/2:
        amp /= 2
        print('i: ' + str(i) + ' - amp: ' + str(amp) + ' - freq1: ' + str(freq1))
        s += amp*np.sin( 2*np.pi* freq1 *t )
        i += 1
        freq1 = i*freq
    return s
    # end while i*freq < sr/2:
# end make_sawtooth

s = make_sawtooth( amp=0.5, dur=3, freq=200 )

s1 = au.make_sawtooth( amp=0.5, dur_secs=3, freq=200 )

# plt.plot( t , s , 'x-' )
# plt.plot( t , s )

# sd.play( s , sr )