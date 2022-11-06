#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:54:11 2022

@author: max
"""

x = 5
x
y = 5.1
v = [4,6,8]
# v[6]
v[1]
v[0]
g = [4,6.1,8]
g = [4,6.1,[1,2,3]]
# g[3]
g[2]
g[2][1]
v1 = [2,4,6]
v2 = [3,5,7]
v = v1 + v2
h = 5*v1

r = list( range(44100) )/44100 # python can't do it
# TypeError: unsupported operand type(s) for /: 'list' and 'int'

print('cell 1')

# %% introduction to numpy

print('cell 2')

import numpy as np

n1 = np.array([2,4,6])
n2 = np.array( v2 )

n = n1 + n2
m = 5*n1

dur = 5 # in seconds
t = np.arange( dur*44100 )/44100
amp = 0.5
f = 200

'''
s0 = amp*np.sin( 2*np.pi* 1*f *t )
s1 = (amp/2)*np.sin( 2*np.pi* 2*f *t )
s2 = (amp/4)*np.sin( 2*np.pi* 3*f *t )

s = s0 + s1 + s2
'''

s = amp*np.sin( 2*np.pi* f *t )

for i in range(50):
    print(i)
    s = s + ( amp/ (2**(i+1)) )*np.sin( 2*np.pi*(i+2)*f *t )

# %% introduction to matplotlib

import matplotlib.pyplot as plt

'''
plt.plot( t , s0 )
plt.plot( t, s1 )
plt.plot( t, s2 )
'''
plt.plot( t , s )

# %% make sound

import sounddevice as sd

sd.play(s, 44100)