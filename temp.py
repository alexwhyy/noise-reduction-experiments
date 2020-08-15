from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

import sounddevice as sd
from numba import jit

duration = 10  # seconds

# sd.default.samplerate = 10000
# sd.default.blocksize = 128
sd.default.latency = 0.02

def callback(indata, outdata, frames, time, status):
    outdata[:] = indata * -1

with sd.Stream(channels=1, callback=callback):
    while True:
        pass

'''
sd.Stream(device=(args.input_device, args.output_device),
                   samplerate=args.samplerate, blocksize=args.blocksize,
                   dtype=args.dtype, latency=args.latency,
                   channels=args.channels, callback=callback)
'''
