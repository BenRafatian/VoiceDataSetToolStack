import wave
import os
import contextlib
import shutil

inputpath = './data/'

if(os.makedirs('./output',exist_ok=True)):
    pass
outputpath = './output/'

srcfiles = os.listdir(inputpath)

goodfiles=[]

for file in srcfiles:
    with contextlib.closing(wave.open(inputpath + file,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        
        if 3 < duration <7 :
            goodfiles.append(file)

for gf in goodfiles:

    shutil.copy(inputpath + gf, outputpath)

remainingFiles = os.listdir(outputpath)
i = 1
for file in remainingFiles:
    os.rename(outputpath + file,outputpath + str(i) +' .wav')
    i += 1