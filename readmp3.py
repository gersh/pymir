# Example showing how to read mp3 files
from pymir.audio import mp3

a = mp3.load("audio_files/test-stereo.mp3")
#t=stft(a)
#a=istft(a)
mp3.play(a)
