# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:41:34 2021

@author: user
"""

import os
import audio_file_representation as afr
import pickle

main_folder = 'C:\\Users\\user\\Documents\\MastersCourses\\programming2\\speech_sentiment_part\\'

actor_folders = os.listdir( main_folder )

audio_samples = []

# %% takes up too much time! run only once if possible
for a in actor_folders:
    if a[:5] == 'Actor':
        print('running for actor: ' + a)
        for f in os.listdir( os.path.join( main_folder , a ) ):
            print('running for file: ' + f)
            audio_samples.append( afr.AudioFileRepresentation( os.path.join( main_folder , a , f ) ) )

# %% save in pickle format
with open('audio_samples.pickle', 'wb') as handle:
    pickle.dump(audio_samples, handle, protocol=pickle.HIGHEST_PROTOCOL)

# %% check size of variable
print( 'size of saved structure: ' + str(len(pickle.dumps(audio_samples, -1))) )