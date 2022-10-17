# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 08:46:22 2021

@author: user
"""

import copy

# %%

x = 10
y = x # actually a shallow copy but...
y = 5 # here it is re-instantiated
print( 'x: ' + str(x) + ' - y: ' + str(y) )

# %% a deeper look
x = 10
y = x # actually a shallow copy but...
print('before y = 5: id(x): ' + str(id(x)) + ' - id(y): ' + str(id(y)))
y = 5 # here it is re-instantiated - new id
print('after  y = 5: id(x): ' + str(id(x)) + ' - id(y): ' + str(id(y)))
print( 'x: ' + str(x) + ' - y: ' + str(y) )

# %%

x = 10
y = x # can be considered as deep copy
y += 1
print( 'x: ' + str(x) + ' - y: ' + str(y) )

# %%

x = [1,2,3]
y = x # shallow copy but...
y = [4,5,6] # re-instantiation of y - lost relation with x
print( 'x: ' + repr(x) + ' - y: ' + repr(y) )

# %% a deeper look
x = [1,2,3]
y = x # shallow copy but...
print('before y = [4,5,6]: id(x): ' + str(id(x)) + ' - id(y): ' + str(id(y)))
y = [4,5,6] # re-instantiation of y - lost relation with x
print('after  y = [4,5,6]: id(x): ' + str(id(x)) + ' - id(y): ' + str(id(y)))
print( 'x: ' + str(x) + ' - y: ' + str(y) )

# %%

x = [1,2,3]
y = x # shallow copy and...
y[0] = 4
y[1] = 5
y[2] = 6 # each address is modified
print( 'x: ' + repr(x) + ' - y: ' + repr(y) )

# %%

x = [1,2,3]
y = copy.deepcopy( x ) # deep copy and...
y[0] = 4
y[1] = 5
y[2] = 6 # new addresses have been created
print( 'x: ' + repr(x) + ' - y: ' + repr(y) )

# %% shallow copy

x = {'name': 'Maria', 'age': 10}
y = x
y['name'] = 'George'
y['age'] = 5
print( 'x: ' + str(x) + ' - y: ' + str(y) )

# %% deep copy

x = {'name': 'Maria', 'age': 10}
y = copy.deepcopy( x )
y['name'] = 'George'
y['age'] = 5
print( 'x: ' + str(x) + ' - y: ' + str(y) )

# %% in function

def change_info( s ):
    s['name'] = 'George'
    s['age'] = 5
# end change_info

x = {'name': 'Maria', 'age': 10}
y = x

change_info( y )
print( 'x: ' + str(x) + ' - y: ' + str(y) )

# %% Exercises
'''
1) Create a function that does deep copy with deepcopy.

2) Create a function that does deep copy by creating a new object and returning it.

3) Explore what happens with the id() values of elements in arrays.
- What if all values are integer?
- What if all values are float?
- What if all values are strings?
- What if one value changes inside the array?
Hint: you can check the id differences between, say, the first and the second element.
Additionally, you can re-instantiate the same object multiple times to check if the id 
values remain the same.
'''
