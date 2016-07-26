import vlc
import os.path
import time
import threading

def threadFunction(filename):
    instance = vlc.Instance()
    mediaplayer = instance.media_player_new()

    media = instance.media_new(
        os.path.normpath(os.getcwd() + "/audio/" + filename))
    mediaplayer.set_media(media)
    mediaplayer.play()

t = threading.Thread(target=threadFunction, args=("song1.mp3",), name="first")
s = threading.Thread(target=threadFunction, args=("song0.mp3",), name="second")

t.start()
s.start()

time.sleep(10)