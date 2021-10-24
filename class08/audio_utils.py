# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:20:13 2020

@author: user
"""

# CAUTION: audio file needs to be mono!

import numpy as np

def make_noise( amp=0.5 , dur_secs=0.5 , sr=44100 ):
    return amp*( 1 - 2*np.random.random( int(dur_secs*sr) ) )

def make_sine( freq=440 , amp=0.5 , phase=0.0 , dur_secs=0.5 , sr=44100 ):
    # phase is multiples of 2*pi
    t = np.arange(dur_secs*sr)/sr
    return amp*np.sin( 2*np.pi*freq*t + np.pi*2*phase )

def make_adsr( a=0.01 , d=0.03, s_level=0.3 , r=0.1 , dur_secs=0.5 , sr=44100 ):
    a_samples = int(np.floor(a*sr))
    d_samples = int(np.floor(d*sr))
    r_samples = int(np.floor(r*sr))
    total_samples = int(np.floor(dur_secs*sr))
    s_samples = total_samples - r_samples - a_samples - d_samples
    if s_samples < 0:
        s_samples = 1 # or whatever > 0 value
    a_part = np.linspace( 0, 1, a_samples )
    d_part = np.linspace( 1, s_level, d_samples )
    s_part = np.linspace( s_level, s_level, s_samples ) # s_level*np.ones( s_samples )
    r_part = np.linspace( s_level, 0, r_samples )
    return np.hstack( ( a_part , d_part , s_part , r_part ) )

def make_sine_with_adsr( freq=440 , amp=0.5 , phase=0.0 , adsr=np.ones(22050), sr=44100 ):
    t = np.arange(adsr.size)/sr
    return amp*np.sin( 2*np.pi*freq*t + np.pi*2*phase )*adsr

def make_square_aliased( freq=440 , amp=0.5 , phase=0.0 , dur_secs=0.5 , sr=44100 ):
    t = np.arange(dur_secs*sr)/sr
    return amp*( 1 - 2*( ( np.sin( 2*np.pi*freq*t + np.pi*2*phase ) > 0 ).astype(float) ) )

def make_square_aliased_with_adsr( freq=440 , amp=0.5 , phase=0.0 , adsr=np.ones(22050), sr=44100 ):
    t = np.arange(adsr.size)/sr
    return amp*( 1 - 2*( ( np.sin( 2*np.pi*freq*t + np.pi*2*phase ) > 0 ).astype(float) ) )*adsr

def make_square( freq=440 , amp=0.5 , phase=0.0 , dur_secs=0.5 , sr=44100 ):
    t = np.arange(dur_secs*sr)/sr
    s = np.sin( 2*np.pi*freq*t )
    i = 3
    freq_harmonics = freq*i
    while freq_harmonics <= sr/2:
        s += (1/i)*np.sin( 2*np.pi*freq_harmonics*t )
        i += 2
        freq_harmonics = freq*i
    return amp*s

def make_square_with_adsr( freq=440 , amp=0.5 , phase=0.0 , adsr=np.ones(22050), sr=44100 ):
    t = np.arange(adsr.size)/sr
    s = np.sin( 2*np.pi*freq*t )
    i = 3
    freq_harmonics = freq*i
    while freq_harmonics <= sr/2:
        s += (1/i)*np.sin( 2*np.pi*freq_harmonics*t )
        i += 2
        freq_harmonics = freq*i
    return amp*s*adsr

def make_sawtooth_aliased( freq=440 , amp=0.5 , phase=0.0 , dur_secs=0.5 , sr=44100 ):
    t = np.arange(dur_secs*sr)/sr
    return amp*( 1 - 2*( ((t*sr)%(sr/freq))/(sr/freq) ) )

def make_sawtooth_aliased_with_adsr( freq=440 , amp=0.5 , phase=0.0 , adsr=np.ones(22050), sr=44100 ):
    t = np.arange(adsr.size)/sr
    return amp*( 1 - 2*( ((t*sr)%(sr/freq))/(sr/freq) ) )*adsr

def make_sawtooth( freq=440 , amp=0.5 , phase=0.0 , dur_secs=0.5 , sr=44100 ):
    t = np.arange(dur_secs*sr)/sr
    s = np.sin( 2*np.pi*freq*t )
    i = 2
    freq_harmonics = freq*i
    while freq_harmonics <= sr/2:
        s += (1/i)*np.sin( 2*np.pi*freq_harmonics*t )
        i += 1
        freq_harmonics = freq*i
    return amp*s

def make_sawtooth_with_adsr( freq=440 , amp=0.5 , phase=0.0 , adsr=np.ones(22050), sr=44100 ):
    t = np.arange(adsr.size)/sr
    s = np.sin( 2*np.pi*freq*t )
    i = 2
    freq_harmonics = freq*i
    while freq_harmonics <= sr/2:
        s += (1/i)*np.sin( 2*np.pi*freq_harmonics*t )
        i += 1
        freq_harmonics = freq*i
    return amp*s*adsr

def make_triangle( freq=440 , amp=0.5 , phase=0.0 , dur_secs=0.5 , sr=44100 ):
    t = np.arange(dur_secs*sr)/sr
    s = np.sin( 2*np.pi*freq*t )
    i = 3
    a = ( (-1)**( (i-1)/2 ))*i**2
    freq_harmonics = freq*i
    while freq_harmonics <= sr/2:
        s += (1/a)*np.sin( 2*np.pi*freq_harmonics*t )
        i += 2
        a = ( (-1)**( (i-1)/2 ))*i**2
        freq_harmonics = freq*i
    return amp*s 

def make_triangle_with_adsr( freq=440 , amp=0.5 , phase=0.0 , adsr=np.ones(22050), sr=44100 ):
    t = np.arange(adsr.size)/sr
    s = np.sin( 2*np.pi*freq*t )
    i = 3
    a = ( (-1)**( (i-1)/2 ))*i**2
    freq_harmonics = freq*i
    while freq_harmonics <= sr/2:
        s += (1/a)*np.sin( 2*np.pi*freq_harmonics*t )
        i += 2
        a = ( (-1)**( (i-1)/2 ))*i**2
        freq_harmonics = freq*i
    return amp*s*adsr

def get_part( r , s=0 , e=-1 ):
    # r: recording numpy array
    # s: starting sample
    # e: ending sample - -1 means the end of the file
    # 
    
    # check if end is greater than recording length
    if e < 0 or e > r.size:
        e = r.size
    if s > e-1:
        s = e
    w = np.hanning( e-s )
    return w*r[s:e]

def get_random_part( r , s=0 , e=-1 , d_min=1000 , d_max=1000 ):
    # r: recording numpy array
    # s: starting sample
    # e: ending sample - -1 means the end of the file
    # d_min: minimum duration
    # d_max: maximum duration
    # 
    
    # define a duration
    if d_min < 100:
        d_min = 100
    if d_min > d_max:
        d_max = d_min
    if d_max > r.shape[0] - d_min :
        d_max = r.shape[0] - d_min
    dur = np.random.randint( d_min , d_max )
    
    # check if end is greater than recording length
    if e < 0 or e > r.size:
        e = r.size
    if e - dur < 0:
        e = dur
    if s > e-1:
        s = e - dur
    s_rand = np.random.randint( s , e )
    w = np.hanning( dur )
    return w*r[s_rand:(s_rand+dur)]

def get_stereo_random_part( r , s=0 , e=-1 , d_min=1000 , d_max=1000 , pan=0.5 ):
    if pan < 0:
        pan = 0
    if pan > 1:
        pan = 1
    p = get_random_part( r , s , e , d_min , d_max )
    return np.vstack( ( pan*p , (1-pan)*p ) ).T

# ====================== EXERCISES =============================
# hint: check random composition in example 1
# --
# --
# For bonus points: Implement all functions in audio_utils.py and
# your granular synth using functions that accept argumetns as
# arbitrary dictionaries, e.g. def get_stereo_random_part( **args )
# --
# --
# Exercise 1: Make a function that returns a random stereo part
# after applying a specific amplitude to it. Main program should
# decide the range of this amplitude (amp_min and amp_max)
# --
# --
# Exercise 2: Make a function that returns a random stereo part
# with random amplitude and random pitch shift - by scanning
# samples faster or slower. Hint: check np.linspace
# --
# --
# Exercise 3: Make a short segment of granular synthesis using 
# the methods you constructed (or/and others) on a file of your
# choice.