#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:48:24 2021

@author: max
"""

import numpy as np

# lists in python
x = [1,2,3]
y = [4,5,6]
z = x + y

# arrays in numpy
nx = np.array( x )
ny = np.array( y )
nz = nx + ny

# %% apply in functions
y = 2 * nx ** 2 + 5

# %%
y = np.sin(nx**3 + 2*nx**2 + 5)

# %% size of arrays in operations should be the same
# results is the same size as the inputs

a = np.array( [1,2,3] )
b = np.array( [4,5,6,7] )
# c = a + b
# c = a**2 + np.cos(b)
c = np.sin(a**3 + 2*b**2 + 5)

# %% sequence in python
s = range(100)
for i in s:
    print(i)

s_list = list(s)

# %% sequences in numpy
s = np.arange(100)
y = np.sin(2*np.pi*s)

# get items from the 3rd to the 15th - εύρος στοιχείων από 3 έως 15 (έως και 14)
r = s[3:15]
# αρχίζοντας από την αρχή έως ένα σημείο
r = s[:15]
# από ένα σημείο ως το τέλος
r = s[95:]
# με διαφορετικό βήμα
r = s[::5]

# %% 2-διάσταστα διανύσματα (2D arrays)

# python: λίστα από λιστες
x = [ [1,2,3] , [4,5,6], [7,8,9], [2,4,6] ]
# numpy: 2Δ πίνακας
nx = np.array(x)
print('shape: ', nx.shape)
print('size: ', nx.size)

# %%

n = nx[2,1]

n = nx[:2,1:]

















