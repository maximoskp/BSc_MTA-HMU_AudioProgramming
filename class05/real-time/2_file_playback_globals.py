# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:08:32 2021

@author: user
"""

import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

WINDOW_SIZE = 2048
CHANNELS = 2
RATE = 44100

# global
global_block = np.zeros( WINDOW_SIZE*2 )
# b = np.zeros( (WINDOW_SIZE , CHANNELS) , dtype='int16' )

#------------------------------------------------------------------------------------

f = wave.open( 'audio_files/019.wav', 'rb' )


# %% call back with global

def callback( in_data, frame_count, time_info, status):
    global global_block
    global_block = f.readframes(WINDOW_SIZE)
    n = np.frombuffer( global_block , dtype='int16' )
    # begin with a zero buffer
    global b
    b = np.zeros( (n.size , CHANNELS) , dtype='int16' )
    # 0 is left, 1 is right speaker / channel
    b[:,0] = n
    return (b, pyaudio.paContinue)

# %% create output stream

p = pyaudio.PyAudio()
output = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=WINDOW_SIZE,
                stream_callback=callback)

output.start_stream()

f.setpos(0)

# after starting, check when n empties (file ends) and stop
# while len(global_block) > 0: # NOT WORKING as intended
keep_plotting = True
# while len(global_block) == WINDOW_SIZE*2:
while keep_plotting:
    plt.clf()
    plt.plot(b)
    plt.axis([0,WINDOW_SIZE, -2**15, 2**15])
    plt.show()
    plt.pause(0.01)
    sleep(0.01)
    print('global_block: ' + str(len(global_block)))
    if len(global_block) < WINDOW_SIZE*2:
        keep_plotting = False

print('stopping audio')
output.stop_stream()

plt.clf()
plt.plot(b)
plt.axis([0,WINDOW_SIZE, -2**15, 2**15])
plt.show()

# %% let's start over and introduce some keyboard controls

user_quit = False

while not user_quit:
    k = input('type p to start playback, s to stop and q to quit')
    if k == 'p':
        output.stop_stream()
        f.setpos(0)
        output.start_stream()
    elif k == 's':
        output.stop_stream()
    elif k == 'q':
        output.stop_stream()
        user_quit = True

# exescise: allow user to type a number and start/jump playback from this time
# (in seconds?) in the recording