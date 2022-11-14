# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:17:35 2021

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

FFT_FRAMES_IN_SPEC = 20

# global
# n = np.zeros(1)
global_block = np.zeros( WINDOW_SIZE*2 )
fft_frame = np.array( WINDOW_SIZE//2 )
win = np.hamming(WINDOW_SIZE)
spec_img = np.zeros( ( WINDOW_SIZE//2 , FFT_FRAMES_IN_SPEC ) )

#------------------------------------------------------------------------------------

f = wave.open( 'audio_files/019.wav', 'rb' )


# %% call back with global

def callback1( in_data, frame_count, time_info, status):
    global global_block, f, fft_frame, win, spec_img
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
        fft_frame = 20*np.log10( p[ :WINDOW_SIZE//2 ] / 32678 )
        spec_img = np.roll( spec_img , -1 , axis=1 )
        spec_img[:,-1] = fft_frame[::-1]
    return (b, pyaudio.paContinue)

# %% create output stream
p = pyaudio.PyAudio()
output = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=WINDOW_SIZE,
                stream_callback=callback1)

output.start_stream()

# after starting, check when n empties (file ends) and stop
while len(global_block) == WINDOW_SIZE*2:
    plt.clf()
    plt.imshow( spec_img , aspect='auto' )
    # plt.axis([0,WINDOW_SIZE//8, -120,0])
    plt.show()
    plt.pause(0.01)

print('stopping audio')
output.stop_stream()