import argparse

import sounddevice as sd
import numpy as np

from numba import jit

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata * -1

with sd.Stream(channels=2, callback=callback):
    print("noise cancellation active")
    print("press enter to quit at anytime")
    input()
