#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:15:11 2021

@author: max
"""

import numpy as np

# το πρόγραμμα μαντεύει έναν αριθμό
number_random = np.random.randint(10)

# αρχικοποίηση της μεταβλητής που μετράει τις προσπάθειες του χρήστη
n = 0

# αρχικοποίηση της μεταβλητής για το αν ο χρήστης βρήκε
# τον σωστό αριθμό
number_found = False

# επανάληψης του παιχνιδιού
# αν ο χρήστης πατήσει "q" τότε το παιχνίδι σταματάει
while not number_found:
    n += 1
    number_input = input('Guess a number (try ' + str(n) + ') (press "q" to quit): ')
    if number_input == str(number_random):
        number_found = True
        print('Congratulations! Correct number was: ', number_random)
    if number_input == 'q' or number_input == 'Q':
        print('quitting...')
        # number_found = True
        break


















