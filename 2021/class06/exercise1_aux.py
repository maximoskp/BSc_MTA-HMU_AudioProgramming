#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:32:45 2021

@author: max
"""

d = {
    'name': 'Max',
    'height': 1.69,
    'laptops_owned': ['macbook', 'lenovo', 'dell'],
    'is_clever': False
}

# %% χωρίς deep copy
x = [1,2,3]
y = x # ρηχή αντιγραφή
y[1] = 5 # αλλάζει και του x
print(x)

# %% με deep copy
import copy

x = [1,2,3]
y = copy.deepcopy(x) # βαθιά αντιγραφή
y[1] = 5 # ΔΕΝ αλλάζει και του x
print(x)

# %%

def ex1_function( dictionary_in ):
    dictionary_out = copy.deepcopy(dictionary_in)
    dictionary_out['name'] = 'George'
    return dictionary_out
# ex1_function

# %%

d_out =  ex1_function( d )

# %%

def ex2_function( dictionary_in, key='name', value='George' ):
    dictionary_out = copy.deepcopy(dictionary_in)
    dictionary_out[ key ] = value
    return dictionary_out
# ex1_function

# %%

d_out =  ex2_function( d, 'Giannis' )

# %% 


print(d_out)
















