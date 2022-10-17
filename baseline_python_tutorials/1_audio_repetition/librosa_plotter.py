# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 08:12:58 2021

@author: user
"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def array_spectrogram_plot(s , sr=44100 , figure_file_name='figs/spec_lbrs.png'):
    p = librosa.stft(s, n_fft=2048, hop_length=1024)
    d = librosa.amplitude_to_db( np.abs(p), ref=np.max )
    librosa.display.specshow(d, sr=sr, x_axis='time', y_axis='linear')
    plt.savefig( figure_file_name , dpi=300 )

def file_spectrogram_plot(file_name , sr=44100 , figure_file_name='figs/spec_lbrs.png', range_low=20, range_high=22050):
    s, sr = librosa.load( file_name , sr=sr)
    p = librosa.stft(s, n_fft=2048, hop_length=1024)
    d = librosa.amplitude_to_db( np.abs(p), ref=np.max )
    fig , plt_alias =  plt.subplots()
    librosa.display.specshow(d, sr=sr, x_axis='time', y_axis='linear', ax=plt_alias)
    plt_alias.set_ylim([range_low, range_high])
    plt.savefig( figure_file_name , dpi=300 )
    return d