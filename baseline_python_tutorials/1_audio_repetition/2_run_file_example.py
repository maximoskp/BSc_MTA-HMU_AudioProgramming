# import an audio file and manipulate with librosa

import librosa_plotter as lp

play_audio = False
sr = 44100

# %%
file1 = 'audio_files/example1.wav'

lp.file_spectrogram_plot( file1 , figure_file_name='figs/ex1.png', range_high=5000 )

# %%
file2 = 'audio_files/example2.wav'
d = lp.file_spectrogram_plot( file2 , figure_file_name='figs/ex2.png', range_high=5000 )