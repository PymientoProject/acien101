import vlc
import os.path
import time
import CustomVLCClass

def inputListener():
    inputdata = input('0 to quit the first song, 1 to quit the second song')
    if(inputdata == '0'):
        if a.mediaplayer.is_playing() :
            a.pause()
        else:
            a.play()

        print("Quiting 0")

        inputListener() #Starting another time the inputListener
    elif(inputdata == '1'):
        if b.mediaplayer.is_playing():
            b.pause()
        else:
            b.play()

        print("Quiting 1")

        inputListener() #Starting another time the inputListener


a = CustomVLCClass.CustomVLCClass(filename="song0.mp3")
b = CustomVLCClass.CustomVLCClass(filename="song1.mp3")

inputListener()

while a.mediaplayer.is_playing() and b.mediaplayer.is_playing:
    time.sleep(0.1)
