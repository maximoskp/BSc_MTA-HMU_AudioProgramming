# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:16:44 2021

@author: user
"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class AudioFileRepresentation:
    
    def __init__(self, file_path, sr=44100, keep_audio=False):
        self.sr = sr
        s, sr = librosa.load( file_path , self.sr)
        self.audio = s
        self.extract_power_spectrum()
        if not keep_audio:
            del self.audio
    # end constructor
    
    def extract_power_spectrum(self):
        p = librosa.stft(self.audio, n_fft=2048, hop_length=1024)
        self.power_spectrum = librosa.amplitude_to_db( np.abs(p), ref=np.max )
    # end extract_power_spectrum
    
    def plot_spectrum(self, range_low=20, range_high=5000):
        fig , plt_alias =  plt.subplots()
        librosa.display.specshow(self.power_spectrum, sr=self.sr, x_axis='time', y_axis='linear', ax=plt_alias)
        plt_alias.set_ylim([range_low, range_high])
    # end plot_spectrum
    
    def plot_save_spectrum(self, figure_file_name='test.png', range_low=20, range_high=5000):
        fig , plt_alias =  plt.subplots()
        librosa.display.specshow(self.power_spectrum, sr=self.sr, x_axis='time', y_axis='linear', ax=plt_alias)
        plt_alias.set_ylim([range_low, range_high])
        plt.savefig( figure_file_name , dpi=300 )
    # plot_save_spectrum
# end class AudioFileRepresentation