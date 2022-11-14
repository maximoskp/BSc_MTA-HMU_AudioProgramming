# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:48:15 2021

@author: user
"""

import pyaudio
# import wave
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from threading import Thread

WINDOW_SIZE = 2048
CHANNELS = 1
RATE = 44100

FFT_FRAMES_IN_SPEC = 20

# global
# n = np.zeros(1)
global_block = np.zeros( WINDOW_SIZE*2 )
fft_frame = np.array( WINDOW_SIZE//2 )
win = np.hamming(WINDOW_SIZE)
spec_img = np.zeros( ( WINDOW_SIZE//2 , FFT_FRAMES_IN_SPEC ) )

user_terminated = False

#------------------------------------------------------------------------------------

# f = wave.open( 'audio_files/019.wav', 'rb' )


# %% call back with global

def callback( in_data, frame_count, time_info, status):
    global global_block, f, fft_frame, win, spec_img
    # global_block = f.readframes(WINDOW_SIZE)
    n = np.frombuffer( in_data , dtype='int16' )
    # begin with a zero buffer
    b = np.zeros( (n.size , CHANNELS) , dtype='int16' )
    # 0 is left, 1 is right speaker / channel
    b[:,0] = n
    # for plotting
    # audio_data = np.fromstring(in_data, dtype=np.float32)
    if len(win) == len(n):
        frame_fft = np.fft.fft( win*n )
        p = np.abs( frame_fft )*2/np.sum(win)
        if np.any( p != 0 ):
            fft_frame = 20*np.log10( p[ :WINDOW_SIZE//2 ] / 32678 )
        else:
            fft_frame = np.zeros( p[ :WINDOW_SIZE//2 ].shape )
        spec_img = np.roll( spec_img , -1 , axis=1 )
        spec_img[:,-1] = fft_frame[::-1]
    return (b, pyaudio.paContinue)

def user_input_function():
    k = input('press "s" to terminate (then press "Enter"): ')
    if k == 's' or k == 'S':
        global user_terminated
        user_terminated = True

# %% check available devices
p = pyaudio.PyAudio()
# keep index for input and output devices
device_in_idx = 0
device_out_idx = 0

# show devices
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    # print(device_info)
    if 'Microphone' in device_info['name']:
        print('input device: ')
        print(device_info)
        device_in_idx = i
    if 'Speakers' in device_info['name']:
        print('output device: ')
        print(device_info)
        device_out_idx = i



# %% create input-output streams

output = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                input=True,
                frames_per_buffer=WINDOW_SIZE,
                stream_callback=callback,
                input_device_index=device_in_idx,
                output_device_index=device_out_idx)

output.start_stream()

threaded_input = Thread( target=user_input_function )
threaded_input.start()

# after starting, check when n empties (file ends) and stop
while output.is_active() and not user_terminated:
    plt.clf()
    plt.imshow( spec_img[ WINDOW_SIZE//4: , : ] , aspect='auto' )
    # plt.axis([0,WINDOW_SIZE//8, -120,0])
    plt.show()
    plt.pause(0.01)

print('stopping audio')
output.stop_stream()
