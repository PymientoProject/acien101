import vlc
import os.path
import time
import threading

def threadFunction(filename):
    instance = vlc.Instance()
    mediaplayer = instance.media_player_new()

    media = instance.media_new(
        os.path.normpath(filename))
    mediaplayer.set_media(media)
    mediaplayer.play()

t = threading.Thread(target=threadFunction, args=())

time.sleep(10)