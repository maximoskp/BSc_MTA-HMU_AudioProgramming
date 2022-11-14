# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:41:21 2021

@author: user
"""

import pyaudio
import wave
import numpy as np


WINDOW_SIZE = 1024
CHANNELS = 2
RATE = 44100

#------------------------------------------------------------------------------------

def load_sound_file_into_memory( path ):
    audio_data = wave.open( path, 'rb' )
    return audio_data

f = load_sound_file_into_memory( 'audio_files/019.wav' )
# f = load_sound_file_into_memory( 'audio_files/test_stereo.wav' )

# %%

def callback( in_data, frame_count, time_info, status):
    # begin with a zero buffer
    b = np.zeros( (WINDOW_SIZE , CHANNELS) , dtype='int16' )
    b_even = f.readframes(WINDOW_SIZE)
    n = np.frombuffer( b_even , dtype='int16' )
    # b[:,0] += np.hstack( ( n[::2], n[::2] ) )
    b[:,0] += n
    return (b, pyaudio.paContinue)

def create_start_running_output_stream():
    p = pyaudio.PyAudio()
    output = p.open(format=pyaudio.paInt16,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=WINDOW_SIZE,
                    stream_callback=callback)
    output.start_stream()
    return output

# %% output stream is created and started here

output = create_start_running_output_stream()

# %% CAUTION: output stream needs to stop before starting it again!
output.stop_stream()
