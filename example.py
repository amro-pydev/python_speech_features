#!/usr/bin/env python

from python_speech_features import *

import scipy.io.wavfile as wav

(rate,sig) = wav.read("english.wav")

plot_mono_signal(sig,rate)

mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

print mfcc_feat.shape
print mfcc_feat

plot_mfcc(mfcc_feat)
