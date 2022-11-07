#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:57:57 2022

@author: max
"""

import audio_utils as au
import matplotlib.pyplot as plt

v = au.make_adsr()
s = au.make_sine(freq=100, amp=1, dur_secs=0.5)
s1 = au.make_sine_with_adsr(freq=100, amp=0.7, adsr=v)

vs = v*s

plt.plot( v )
plt.plot( s )
plt.plot( vs )
plt.plot( s1 )