import serial
import time
import RPi.GPIO as ss
ss.setwarnings(False)
ss.setmode(ss.BCM)
ss.setup(17,ss.OUT)
ss.setup(10,ss.OUT)
ss.output(17,True)
ss.output(10,False)
s=serial.Serial(port="/dev/ttyS0",baudrate=9600)

def blue():
  l=s.readline()
  print(l)
  y=s.read()
  if(y=='1'):
   s.write("led-on")
   print("led-on")
   ss.output(17,False)
  if(y=='2'):
   s.write("led-off")
   print("led-off")
   ss.output(17,True)
  if(y=='3'):
   s.write("Fan-On")
   print("Fan-On")
   ss.output(10,True)
  if(y=='4'):
   s.write("Fan-Off")
   print("Fan-Off")
   ss.output(10,False)
