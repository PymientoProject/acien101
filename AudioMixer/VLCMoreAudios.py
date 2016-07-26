import vlc
import os.path
import time
import threading

def inputListener():
    inputdata = input('0 to quit the first song, 1 to quit the second song')

def startSong(filename):
    instance = vlc.Instance()
    mediaplayer = instance.media_player_new()

    media = instance.media_new(
        os.path.normpath(os.getcwd() + "/audio/" + filename))
    mediaplayer.set_media(media)
    mediaplayer.play()

startSong("song0.mp3")
startSong("song1.mp3")

time.sleep(10)