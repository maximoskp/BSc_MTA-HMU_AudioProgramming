#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:33:07 2021

@author: max
"""

d = {
    'name': 'Max',
    'height': 1.69,
    'laptops_owned': ['macbook', 'lenovo', 'dell'],
    'is_clever': False
}

# %% 

print( d['name'] )

# %% 

d['name'] = 'George'

# %% 

def change_value( x , x_key='name', x_value='Marina' ):
    if x_key in x.keys():
        x[ x_key ] = x_value
    else:
        print('Invalid key. Valid keys are: ', x.keys())
    return x
# change_value

# %% 

d = {
    'name': 'Max',
    'height': 1.69,
    'laptops_owned': ['macbook', 'lenovo', 'dell'],
    'is_clever': False
}

print('before 1st call: ', d)
d = change_value( d )
print('after 1st call: ', d)
d = change_value( d, x_value='Christos' )
print('after 2nd call: ', d)
d = change_value( d , 'height', 1.70 )
print('after 3rd call: ', d)

# %% 

k = input('press something: ')

print(k)

















