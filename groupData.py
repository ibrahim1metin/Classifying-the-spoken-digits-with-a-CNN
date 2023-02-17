import os
import wave
from spectrum import GetSpectrumsOfAFile
names=[str(i) for i in range(10)]
path="data/"
if __name__ =="__main__":
    for i in names:
        if not os.path.exists(path+i):
            os.makedirs(path+i)
        else:
            print("Directory already exists.")
    for file in os.listdir("recordings/"):
        #This number can be changed depending on the files whose spectrums are going to be saved. I executed this line for all files.
        if file.startswith("9"):
            fileContent=wave.open("recordings/"+file,"r")
            GetSpectrumsOfAFile(fileContent,f"data/{file[0]}/"+file[:-4:]+".png")