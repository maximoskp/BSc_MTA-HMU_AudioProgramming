# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:12:01 2020

@author: user
"""

'''
CAUTION
- make sure you understand how linspace works
- keep in mind that pitch alteration, using this technique, means length alteration
- this technique is usefull in the context of granular synthesis
- applying this technique for pitch shifting larger audio segments without
  altering their size is possible, by splitting it in smaller overlapping
  grains and applying pitch shifting to them
'''

import numpy as np
import sounddevice as sd

# %%
# create a sinusoidal waveform
sr = 44100
duration = 0.8 # secs
freq = 300
t = np.arange( duration*sr )/sr
s_original = np.sin( 2*np.pi*freq*t )

# hear it
sd.play( s_original , sr )

# %%

# select a speed/pitch value
pitch_multiplier = 1.5

# alter length according to inverse pitch_multiplier
s_altered = s_original[ np.linspace( 0 , s_original.size, int(s_original.size/pitch_multiplier) , endpoint=False).astype(int) ]

# compare pitch alteration
s = np.hstack( (s_original , s_altered) )
sd.play( s , sr )

# %%
