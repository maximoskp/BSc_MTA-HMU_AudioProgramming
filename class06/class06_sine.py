#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:16:46 2021

@author: max
"""

import numpy as np

sample_rate = 44100

t = np.arange( sample_rate )/sample_rate

freq = 150

s = np.sin( 2*np.pi * freq * t )

# %% 

import matplotlib.pyplot as plt
plt.plot( t, s, '.-' )

# %% 

import sounddevice as sd

sd.play(s, 44100)