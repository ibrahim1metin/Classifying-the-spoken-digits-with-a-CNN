import wave
import numpy as np
import matplotlib.pyplot as plt
from spectrum import getDurationOfTheFile
def PlotSignal(f:wave.Wave_read):
    sp=np.linspace(0,getDurationOfTheFile(f),num=f.getnframes())
    samp=f.readframes(f.getnframes())
    waveArray=np.frombuffer(samp,np.int16)
    plt.figure(figsize=(10,10))
    plt.plot(sp,waveArray)
    plt.xlim(0,getDurationOfTheFile(f))
    plt.show()
if __name__=="__main__":
    f=wave.open("recordings/7_george_5.wav","r")
    PlotSignal(f)