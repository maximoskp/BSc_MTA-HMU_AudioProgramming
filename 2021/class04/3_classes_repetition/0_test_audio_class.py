# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:23:43 2021

@author: user
"""

import sys
# import os
import audio_file_representation as afr
import pickle

file_path = '../../audio_files/artificial_speech_1.wav'

# %% load object

test_obj = afr.AudioFileRepresentation( file_path, sr=22050 , keep_audio=False ) # actually, we're calling the constructor (__init__)

# %% check size
print( 'size of object: ' + str( sys.getsizeof(test_obj) ) )
print( 'more accurate size of object: ' + str(len(pickle.dumps(test_obj, -1))) )