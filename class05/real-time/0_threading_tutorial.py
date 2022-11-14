# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:43:44 2021

@author: user
"""

from threading import Thread
from time import sleep

def fun_1():
    counter1 = 0
    while counter1 < 10:
        print('fun_1: counter1 = ' + str(counter1))
        counter1 += 1
        sleep(1)

def fun_2():
    counter2 = 0
    while counter2 < 10:
        print('fun_2: counter2 = ' + str(counter2))
        counter2 += 1
        sleep(1)

# %% no threading

fun_1()
fun_2()

# %% one in thread - one in main

t1 = Thread( target = fun_1 )
t1.start()
sleep(0.01)
fun_2()


# %% both in threads

t1 = Thread( target = fun_1 )
t2 = Thread( target = fun_2 )
t1.start()
sleep(0.01)
t2.start()

# %% keyboard input freezes main thread

k = input('type something and press enter: ')
print('this does not print while input is pending...')
print('text typed: ' + k)

# %% input anticipated in separate thread

user_input_provided = False

def user_input_thread():
    k = input('type something and press enter: ')
    print('text typed:' + k)
    global user_input_provided
    user_input_provided = True

t = Thread( target = user_input_thread )
user_keyboard_input = t.start()
print('this does print while user input is pending')

while not user_input_provided:
    sleep(0.1)