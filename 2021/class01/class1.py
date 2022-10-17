# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:39:33 2020

@author: user
"""

x = 1
y = 1.2

s = 'my name is max'

t = [1,3,5,6,8]
ts = ['my ', 'name ', 'is']

z = x + y

p = t + ts
p = ts + t

xdouble = 2*x

q = ' your name is min'

d = s + q


# How can we add two lists numerically?
t1 = [1,2,3]*1000000
t2 = [4,5,6]*1000000
# t = t1 + t2 # we would like to have t = [5, 7, 9]
import time
start_time = time.time()
t = []
for i in range( len( t1 ) ):
    t.append( t1[i] + t2[i] )
duration_for = time.time() - start_time

# we can do it with the numpy library
import numpy as np
nt1 = np.array( t1 )
nt2 = np.array( t2 )
start_time = time.time()
nt = nt1 + nt2
duration_numpy = time.time() - start_time

import scipy.io.wavfile as wf
import matplotlib.pyplot as plt

# load an audio file
sr, a = wf.read('audio_files/ah.wav')

plt.plot( np.arange(a.shape[0]) , a[:,0] )

import sounddevice as sd
sd.play(a , sr)

