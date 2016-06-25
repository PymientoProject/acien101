import pyaudio
import wave
import time
import threading

wf = wave.open("audio/bird.wav", 'rb')
wf2 = wave.open("audio/cat.wav", 'rb')

#init obj
p = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()

# define callback (2)
def callback1(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

def callback2(in_data, frame_count, time_info, status):
    data2 = wf2.readframes(frame_count)
    return (data2, pyaudio.paContinue)

def worker(streams, wfs):
    streams.start_stream()
    while streams.is_active():
        time.sleep(0.1)

    streams.stop_stream()
    streams.close()

    wfs.close()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback1)

stream2 = p2.open(format=p2.get_format_from_width(wf2.getsampwidth()),
                 channels=wf2.getnchannels(),
                 rate=wf2.getframerate(),
                 output=True,
                 stream_callback=callback2)

t = threading.Thread(target=worker, args=(stream, wf,), name='primero')
w = threading.Thread(target=worker, args=(stream2, wf2,), name='segundo')

w.start()
t.start()

while w.isAlive and t.is_alive():
    time.sleep(0.1)
p.terminate()

