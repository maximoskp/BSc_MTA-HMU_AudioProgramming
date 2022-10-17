# create synthesised sounds and analyse them with librosa

import audio_utils as au
import sounddevice as sd
import librosa_plotter as lp

play_audio = False
sr = 44100

freq = 440
amp = 0.7

dur = 0.8

# %% noise

s = au.make_noise( amp=amp , dur_secs=dur , sr=sr )
# s = au.make_noise( amp=0.1 )

if play_audio:
    sd.play( s , sr )

lp.array_spectrogram_plot( s )

# %% sine with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.5 , dur_secs=dur , sr=sr )
s = au.make_sine_with_adsr( freq=freq , amp=amp , phase=0.0 , adsr=a, sr=sr )

if play_audio:
    sd.play( s , sr )

lp.array_spectrogram_plot( s )

# %% square with adsr

a = au.make_adsr( a=0.01 , d=0.01, s_level=0.3 , r=0.3 , dur_secs=dur , sr=sr )
s = au.make_square_with_adsr( freq=freq , amp=amp , phase=0.0 , adsr=a, sr=sr )
'''
import numpy as np
import matplotlib.pyplot as plt
sp = np.fft.fft( s[:1024]*np.hanning(1024) )
plt.plot( np.linspace(0,22050, 512) , np.sqrt( sp[:512].real**2 + sp[:512].imag**2 ) )
'''
if play_audio:
    sd.play( s , sr )

lp.array_spectrogram_plot( s )
