import matplotlib.pyplot as plt

import sounddevice as sd
import numpy as np

duration = 5

original_sound = np.array([])
cancelled_sound = np.array([])

def callback(indata, outdata, frames, time, status):
    global original_sound, cancelled_sound

    if status:
        print(status)
    outdata[:] = indata * -1

    original_sound = np.append(original_sound, indata)
    cancelled_sound = np.append(cancelled_sound, indata * -1)

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))

plt.plot(np.arange(0, original_sound.shape[0]), original_sound, "g-")
plt.plot(np.arange(0, cancelled_sound.shape[0]), cancelled_sound, "b-")
plt.plot(np.arange(0, original_sound.shape[0]), (original_sound + cancelled_sound), "r-")
plt.show()

print(original_sound + cancelled_sound)