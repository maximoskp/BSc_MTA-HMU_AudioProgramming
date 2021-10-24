# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:08:28 2020

@author: user
"""

import audio_utils as au
import soundfile as sf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

s = au.make_sine()

adsr = au.make_adsr()

plt.subplot(311)
plt.plot( np.arange( s.size ) , s )
plt.subplot(312)
plt.plot( np.arange( adsr.size ) , adsr )
plt.subplot(313)
plt.plot( np.arange( adsr.size ) , adsr*s )

sd.play( s*adsr , 44100 )