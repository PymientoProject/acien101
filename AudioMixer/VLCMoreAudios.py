import vlc
import os.path
import time
import CustomVLCClass

def inputListener():
    inputdata = input('0 to quit the first song, 1 to quit the second song')
    if(inputdata == '0'):
        a.pause()
        print("Quiting 0")
    elif(inputdata == '1'):
        b.pause()
        print("Quiting 1")



a = CustomVLCClass.CustomVLCClass(filename="song0.mp3")
b = CustomVLCClass.CustomVLCClass(filename="song1.mp3")

inputListener()

time.sleep(10)

