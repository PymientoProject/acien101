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

            x = line.decode('ascii', errors='replace')

            if x == '3\r\n':
                print("3")

            elif x == '0\r\n':
                print("0")

            elif x == '1\r\n':
                print("1")


        except KeyboardInterrupt:
            print("exiting")
            break
