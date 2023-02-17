import wave
import numpy as np
import matplotlib.pyplot as plt
def getDurationOfTheFile(file:wave.Wave_read):
    return file.getnframes()/file.getframerate()
def GetSpectrumsOfAFile(f:wave.Wave_read,fileName:str,saveMode=True):
    samp=f.readframes(f.getnframes())
    waveArray=np.frombuffer(samp,np.int16)
    fig=plt.figure(figsize=(3,3))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(waveArray, Fs=f.getframerate(), vmin=-30, vmax=50)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    if not saveMode:
        plt.show()
    else:
        plt.savefig(fileName,bbox_inches="tight", pad_inches=0)
if __name__=="__main__":
    f=wave.open("recordings/6_george_2.wav","r")
    GetSpectrumsOfAFile(f,"",False)