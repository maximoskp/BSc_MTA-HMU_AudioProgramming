#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:23:24 2021

@author: max
"""

# this is a comment - will not be executed

# %% this is a block

x = 5
y = 6

z = x + y

print('block 1')

# %% this is another block

s = 'I am a string'

print('block 2')

# %% this is the history of what we've written so far

'''

x = 5
x = 15
y = x + 4

x = 45.7
a = [1,2,3,4]
a[0]
s = 'lala'
s[1]
s[2]
s[3]
s[4]
s[1:3]
s[:3]
s[1:]
a = [ 1, 2, 'lalala', 4.5, [4,5,6] ]
a[2]
a[2][2]
a[2][:2]

s[2] = 'x'
b = [1,2,3,4]
b[2]
b[2] = 'lolo'

a[4][1] = 'xixi'
'''

# %% strings in python
s = 'My name is '
t = 'Maximos'
# string concatenation
q = s + t


# %% adding python lists

import time

a = [1.1,2.2,3.3]*1000000
b = [4.1,5.2,6.3]*1000000

python_sum = a + b

'''
for x in a:
    print(x)
'''

for i in range(3):
    # indentation level 1: within the for loop
    print( 'i: ', i )
    for j in range(5, 20, 3):
        print( 'j: ', j)
# indentation back to the beginning, we are outside the for loop
# see it as a list
r = list( range(3) )

numeric_sum = []

start_1 = time.time()
for i in range( len(a) ):
    # print( 'a[' + str(i) + '] = ' + str(a[i]) )
    # print( 'b[' + str(i) + '] = ' + str(b[i]) )
    numeric_sum.append( a[i] + b[i] )
end_1 = time.time()
for_duration = end_1 - start_1

# %% list "multiplication"

a = [1,2,3]*5

# %% array and matrix manipulation in python with the
# numpy library

import numpy as np

'''
x = [1,2,'xaxa']
n = numpy.array( x )
'''

x = [1.1,2.1,3.1]*1000000
n = np.array( x )

y = [4.1,5.1,6.1]*1000000
m = np.array( y )

z = x + y
start_2 = time.time()
k = n + m # as for in lines 88-91
end_2 = time.time()
numpy_sum_duration = end_2 - start_2


# %% 

t = np.arange(5*44100)/44100

s = np.sin( 2*np.pi*100*t )

import matplotlib.pyplot as plt

plt.plot( t, s )

import sounddevice as sd

sd.play(s, samplerate=44100)










