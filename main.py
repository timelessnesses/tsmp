import pydub
import pydub.playback
import os
import signal

signal.signal(2,lambda x,y: exit())
signal.signal(15,lambda x,y:exit())


while True:
        for file in os.listdir('.'):
                if ".py" in file:
                        continue
                print(f'loaded {file}')
                pydub.playback.play(pydub.AudioSegment.from_file(file,format="wav")-6)
