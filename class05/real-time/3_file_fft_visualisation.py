# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:57:55 2021

@author: user
"""

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
# n = np.zeros(1)
global_block = np.zeros( WINDOW_SIZE*2 )
fft_to_plot = np.array( WINDOW_SIZE//2 )
win = np.hamming(WINDOW_SIZE)

#------------------------------------------------------------------------------------

f = wave.open( 'audio_files/019.wav', 'rb' )


# %% call back with global

def callback( in_data, frame_count, time_info, status):
    global global_block, f, fft_to_plot, win
    global_block = f.readframes(WINDOW_SIZE)
    n = np.frombuffer( global_block , dtype='int16' )
    # begin with a zero buffer
    b = np.zeros( (n.size , CHANNELS) , dtype='int16' )
    # 0 is left, 1 is right speaker / channel
    b[:,0] = n
    # for plotting
    # audio_data = np.fromstring(in_data, dtype=np.float32)
    if len(win) == len(n):
        frame_fft = np.fft.fft( win*n )
        p = np.abs( frame_fft )*2/np.sum(win)
        fft_to_plot = 20*np.log10( p[ :WINDOW_SIZE//2 ] / 32678 )
    return (b, pyaudio.paContinue)

# %% create output stream
f.setpos(0)

p = pyaudio.PyAudio()
output = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=WINDOW_SIZE,
                stream_callback=callback)

output.start_stream()

# after starting, check when n empties (file ends) and stop
while len(global_block) == WINDOW_SIZE*2:
    plt.clf()
    plt.plot(fft_to_plot)
    plt.axis([0,WINDOW_SIZE//2, -120,0])
    plt.show()
    plt.pause(0.01)

print('stopping audio')
output.stop_stream()

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