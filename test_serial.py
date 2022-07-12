#!/usr/bin/python
import serial
import syslog
import time

#The following line is for serial over GPIO
port = '/dev/ttyUSB0' # note I'm using Mac OS-X


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

i = 0
setOn = "1"
setOff = "0"

def turn_led(value):
    ard.flush()
    print ("Python value sent: ", value)
    ard.write(str.encode(value))
    time.sleep(1)
    # Serial read section
    msg = ard.read(ard.inWaiting()) # read all characters in buffer
    print ("Message from arduino: ")
    print (msg)
    return

while (i < 4):
    # Serial write section
    turn_led(setOn)
    time.sleep(1)
    turn_led(setOff)
    print(i)
    i = i + 1
else:
    print("Exiting")
exit()