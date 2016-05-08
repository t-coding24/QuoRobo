import webiopi
import serial
import time
import os

ser = serial.Serial('/dev/ttyUSB0', 9600)

@webiopi.macro
def move(tilt,pan):
  global ser
  time.sleep(0.5)
  val = str(tilt) + ":" +str(pan) + ":"
  ser.write(bytes(val,'utf8'))

@webiopi.macro
def eye(str):
  global ser
  time.sleep(0.5)
  ser.write(bytes(str,'utf8'))

@webiopi.macro
def stop():
  global ser
  time.sleep(1)
  ser = serial.Serial('/dev/ttyUSB0', 9600)
  ser.close()

@webiopi.macro
def voice(str):
  os.system('/home/pi/aquestalkpi/AquesTalkPi "' + str + '" | aplay&')
