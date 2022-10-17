# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:52:52 2021

@author: user
"""

import audio_file_representation as afr
import pickle

with open('audio_samples.pickle', 'rb') as handle:
    s = pickle.load(handle)