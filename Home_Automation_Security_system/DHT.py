#import sys
import Adafruit_DHT
import time

def DHT():
 humidity,temp = Adafruit_DHT.read_retry(11,27)
 print'Temp:{0:0.1f}*C Humidity:{1:0.1f}%'.format(temp,humidity)
 time.sleep(1)
