# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:07:38 2021

@author: user
"""

import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

WINDOW_SIZE = 2048
CHANNELS = 2
RATE = 44100

#------------------------------------------------------------------------------------

f = wave.open( 'audio_files/019.wav', 'rb' )

# %% check out successive blocks

# make sure file is starting over
f.setpos(0)

user_continue = True

while user_continue:
    b = np.zeros( (WINDOW_SIZE , CHANNELS) , dtype='int16' )
    b_even = f.readframes(WINDOW_SIZE)
    n = np.frombuffer( b_even , dtype='int16' )
    plt.plot(n)
    plt.axis([0,WINDOW_SIZE, -2**15, 2**15])
    plt.show()
    plt.pause(0.1)
    k = input('press enter to continue - press s (and then enter) to stop')
    plt.clf()
    if k == 's' or k == 'S':
        user_continue = False

# %% it is not possible to have a callback that uses the same principles but also draws
# matplotlib needs to be called within the main thread...
# the following callback will NOT plot

def impossible_callback( in_data, frame_count, time_info, status):
    # begin with a zero buffer
    b = np.zeros( (WINDOW_SIZE , CHANNELS) , dtype='int16' )
    b_even = f.readframes(WINDOW_SIZE)
    n = np.frombuffer( b_even , dtype='int16' )
    plt.plot(n)
    plt.axis([0,WINDOW_SIZE, -2**15, 2**15])
    plt.show()
    plt.clf()
    # 0 is left, 1 is right speaker / channel
    b[:,0] += n
    return (b, pyaudio.paContinue)

# %% create output stream - will NOT plot
p = pyaudio.PyAudio()
output = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=WINDOW_SIZE,
                stream_callback=impossible_callback)

# %% stop output stream

output.stop_stream()