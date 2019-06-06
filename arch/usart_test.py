#!/usr/bin/python3

import serial
from time import sleep

ser = serial.Serial('/dev/ttyS0',9600)

ser.write(b'a')
sleep(3)
ser.write(b'b')
sleep(3)
print("complete")
