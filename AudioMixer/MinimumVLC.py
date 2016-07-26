import vlc
import os.path
import time

'''Example of the minimum that has to have a project with vlc. This example plays the 10 first seconds of a song'''

instance = vlc.Instance()
mediaplayer = instance.media_player_new()

media = instance.media_new(os.path.normpath("/home/amil101/Descargas/The Avalanches - Since I Left You/01 Since I Left You.mp3"))
mediaplayer.set_media(media)

mediaplayer.play()

time.sleep(10)