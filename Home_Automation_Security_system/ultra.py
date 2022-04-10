import Mail as m
import time
import RPi.GPIO as ss
import os
ss.setmode(ss.BCM)
ss.setwarnings(False)
TRIG = 23
ECHO = 24
object =3500
start_time=0
ss.setup(TRIG,ss.OUT)
ss.setup(ECHO,ss.IN)
def ultra():
 mail=0
 ss.output(TRIG,False)
 print("waiting for sensor to settel")
 time.sleep(2)
 ss.output(TRIG,True)
 time.sleep(0.00001)
 ss.output(TRIG,False)
 while ss.input(ECHO)==0:
  start_time = time.time()
 while ss.input(ECHO)==1:
  Bounce_back_time = time.time()
 pulse_duration = Bounce_back_time - start_time
 distance = pulse_duration * 17150
 distance = round(distance,2)
 print("Distance:",distance,"cm")
 time.sleep(0.5)
 if(distance <= object):
  os.system('sudo fswebcam -r 1250x720 cap.png')
  print('CAMERA OUT')
  m.sendmail()
  mail+=1
  print("Mailed")
  time.sleep(10)
  mail=0
  print("!! FLAG RESET !!")


