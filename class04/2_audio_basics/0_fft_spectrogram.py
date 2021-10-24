import numpy as np
import matplotlib.pyplot as plt

# %% make audio

fs = 44100
t = np.arange(1024)/fs
freq = 5000
x = np.sin( 2*np.pi*freq*t )

# %% compute and plot fft

y = np.fft.fft( x )

plt.subplot(311)
plt.plot( np.arange( y.size )/y.size*fs , y.real )
plt.subplot(312)
plt.plot( np.arange( y.size )/y.size*fs , y.imag )
mag = np.sqrt( np.power( y.real , 2 ) + np.power( y.imag , 2 ) )
plt.subplot(313)
plt.plot( np.arange( y.size )/y.size*fs , mag )
plt.savefig('figs/fft.png', dpi=300)
# Question: why keeping the first half is fine?
# Exercise: change bin size and show why it is useful

# %% test windowing

# apply window
w = np.hanning( 1024 )
x_windowed = w*x[:1024]
# to discuss: matrix vs elementwise multiplication

y = np.fft.fft( x_windowed )
mag = np.sqrt( np.power( y.real , 2 ) + np.power( y.imag , 2 ) )
plt.subplot(411)
plt.plot( np.arange( 1024 ) , x[:1024] )
plt.subplot(412)
plt.plot( np.arange( 1024 ) , w[:1024] )
plt.subplot(413)
plt.plot( np.arange( 1024 ) , x_windowed[:1024] )
plt.subplot(414)
plt.plot( np.arange( y.size//2 )/y.size*fs , mag[:y.size//2] )
plt.savefig('figs/fft.png', dpi=300)