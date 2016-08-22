import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)

with ser:
    while True:
        try:
            line = ser.readline()
            if not line:
                continue

		
            print(line)


        except KeyboardInterrupt:
            print("exiting")
            break
