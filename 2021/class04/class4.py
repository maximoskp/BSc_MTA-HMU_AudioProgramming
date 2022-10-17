# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:17:22 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

sr = 44100

window_size = 8192  # corresponds to window_size/sr seconds
t = np.arange( window_size )/sr

f = 200

s = np.sin( 2*np.pi*f*t )

# construct a hunning window
w = np.hanning( window_size )
'''
plt.plot( np.arange(window_size) , s )
plt.plot( np.arange(window_size) , w )
plt.plot( np.arange(window_size) , w*s )
'''
# windowed signal - ready for FFT
windowed_signal = w*s;

y = np.fft.fft( windowed_signal )
# y includes as many frequency bins as the width of the window size
# each frequency bin represents the power of the spectrum in 
# window_size (e.g. 2048) equally-spaced frequency bands
r = y.real
m = y.imag
mag = np.sqrt( r**2 + m**2 )

frequency_bins = np.arange( window_size )/window_size*sr

plt.plot( frequency_bins[:window_size//2] , mag[:window_size//2] )

# fft computation
# 1) take a small part of the signal of size 2**k, e.g. 2048
# 2) apply a hanning window on the signal
# 3) apply fft on the windowed signal
# 4) if we are interested only for which frequencies are present
# in the signal, without phase information, then take the 
# power spectrum as: mag = np.sqrt( r**2 + m**2 )

