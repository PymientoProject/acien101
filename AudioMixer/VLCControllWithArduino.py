import CustomVLCClass
import serial
import time
import threading

time.sleep(20)

while True:
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
        past0 = 0     #For counting the last chip in the field
        past1 = 0
        past2 = 0
        past3 = 0
        past4 = 0

        while True:
            try:
                line = ser.readline()
                if not line:
                    continue

                x = line.decode('ascii', errors='replace')

                if x == '00\r\n':
                    print("00")
                    if past0 == 1:
                        a.mute()
                    if past0 == 2:
                        b.mute()
                    if past0 == 3:
                        c.mute()
                    if past0 == 4:
                        d.mute()
                    if past0 == 5:
                        e.mute()
                    if past0 == 6:
                        f.mute()
                    past0 = 0

                elif x == '01\r\n':
                    print("01")
                    past0 = 1
                    a.unmute()

                elif x == '02\r\n':
                    print("02")
                    past0 = 2
                    b.unmute()

                elif x == '03\r\n':
                    print("03")
                    past0 = 3
                    c.unmute()

                elif x == '04\r\n':
                    print("04")
                    past0 = 4
                    d.unmute()

                elif x == '05\r\n':
                    print("05")
                    past0 = 5
                    e.unmute()

                elif x == '06\r\n':
                    print("06")
                    past0 = 6
                    f.unmute()

                if x == '10\r\n':
                    print("10")
                    if past1 == 1:
                        a.mute()
                    if past1 == 2:
                        b.mute()
                    if past1 == 3:
                        c.mute()
                    if past1 == 4:
                        d.mute()
                    if past1 == 5:
                        e.mute()
                    if past1 == 6:
                        f.mute()
                    past1 = 0

                elif x == '11\r\n':
                    print("11")
                    past1 = 1
                    a.unmute()

                elif x == '12\r\n':
                    print("12")
                    past1 = 2
                    b.unmute()

                elif x == '13\r\n':
                    print("13")
                    past1 = 3
                    c.unmute()

                elif x == '14\r\n':
                    print("14")
                    past1 = 4
                    d.unmute()

                elif x == '15\r\n':
                    print("15")
                    past1 = 5
                    e.unmute()

                elif x == '16\r\n':
                    print("16")
                    past1 = 6
                    f.unmute()

                if x == '20\r\n':
                    print("20")
                    if past2 == 1:
                        a.mute()
                    if past2 == 2:
                        b.mute()
                    if past2 == 3:
                        c.mute()
                    if past2 == 4:
                        d.mute()
                    if past2 == 5:
                        e.mute()
                    if past2 == 6:
                        f.mute()
                    past1 = 0

                elif x == '21\r\n':
                    print("21")
                    past2 = 1
                    a.unmute()

                elif x == '22\r\n':
                    print("22")
                    past2 = 2
                    b.unmute()

                elif x == '23\r\n':
                    print("23")
                    past2 = 3
                    c.unmute()

                elif x == '24\r\n':
                    print("24")
                    past2 = 4
                    d.unmute()

                elif x == '25\r\n':
                    print("25")
                    past2 = 5
                    e.unmute()

                elif x == '26\r\n':
                    print("26")
                    past2 = 6
                    f.unmute()

                if x == '30\r\n':
                    print("30")
                    if past3 == 1:
                        a.mute()
                    if past3 == 2:
                        b.mute()
                    if past3 == 3:
                        c.mute()
                    if past3 == 4:
                        d.mute()
                    if past3 == 5:
                        e.mute()
                    if past3 == 6:
                        f.mute()
                    past3 = 0

                elif x == '31\r\n':
                    print("31")
                    past3 = 1
                    a.unmute()

                elif x == '32\r\n':
                    print("32")
                    past3 = 2
                    b.unmute()

                elif x == '33\r\n':
                    print("33")
                    past3 = 3
                    c.unmute()

                elif x == '34\r\n':
                    print("34")
                    past3 = 4
                    d.unmute()

                elif x == '35\r\n':
                    print("35")
                    past3 = 5
                    e.unmute()

                elif x == '36\r\n':
                    print("36")
                    past3 = 6
                    f.unmute()

                if x == '40\r\n':
                    print("40")
                    if past4 == 1:
                        a.mute()
                    if past4 == 2:
                        b.mute()
                    if past4 == 3:
                        c.mute()
                    if past4 == 4:
                        d.mute()
                    if past4 == 5:
                        e.mute()
                    if past4 == 6:
                        f.mute()
                    past4 = 0

                elif x == '41\r\n':
                    print("41")
                    past4 = 1
                    a.unmute()

                elif x == '42\r\n':
                    print("42")
                    past4 = 2
                    b.unmute()

                elif x == '43\r\n':
                    print("43")
                    past4 = 3
                    c.unmute()

                elif x == '44\r\n':
                    print("44")
                    past4 = 4
                    d.unmute()

                elif x == '45\r\n':
                    print("45")
                    past4 = 5
                    e.unmute()

                elif x == '46\r\n':
                    print("46")
                    past4 = 6
                    f.unmute()




            except KeyboardInterrupt:
                print("exiting")
                break


    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1.0)
    ser.setDTR(False)
    time.sleep(1)
    ser.flushInput()
    ser.setDTR(True)

    a = CustomVLCClass.CustomVLCClass(filename="/acien101/AudioMixer/audio/1.mp3")
    b = CustomVLCClass.CustomVLCClass(filename="/acien101/AudioMixer/audio/2.mp3")
    c = CustomVLCClass.CustomVLCClass(filename="/acien101/AudioMixer/audio/3.mp3")
    d = CustomVLCClass.CustomVLCClass(filename="/acien101/AudioMixer/audio/4.mp3")
    e = CustomVLCClass.CustomVLCClass(filename="/acien101/AudioMixer/audio/5.mp3")
    f = CustomVLCClass.CustomVLCClass(filename="/acien101/AudioMixer/audio/6.mp3")



    inputArduinoThread = threading.Thread(target=arduinoListener, name="inputAduino")
    inputArduinoThread.start()

    while a.mediaplayer.is_playing() and b.mediaplayer.is_playing:
        time.sleep(0.1)
