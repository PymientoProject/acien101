import CustomVLCClass
import serial
import time
import threading

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

    elif(inputdata == '00'):
        a.mute()
        inputListener()
    elif(inputdata == '01'):
        a.unmute()
        inputListener()

def arduinoListener():
    while True:
        try:
            line = ser.readline()
            if not line:
                continue

            x = line.decode('ascii', errors='replace')

            if x == '3\r\n':
                print("3")
                a.mute()
                b.mute()

            elif x == '0\r\n':
                print("0")
                a.unmute()

            elif x == '1\r\n':
                print("1")
                b.unmute()


        except KeyboardInterrupt:
            print("exiting")
            break


ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)

a = CustomVLCClass.CustomVLCClass(filename="song0.mp3")
b = CustomVLCClass.CustomVLCClass(filename="song1.mp3")

inputArduinoThread = threading.Thread(target=arduinoListener, name="inputAduino")
inputArduinoThread.start()

while a.mediaplayer.is_playing() and b.mediaplayer.is_playing:
    time.sleep(0.1)
