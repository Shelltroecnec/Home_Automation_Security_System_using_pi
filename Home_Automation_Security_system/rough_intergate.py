#INTILIZATION
#import Mail as mail
import ultra as mu
import MQ as msg
import DHT as dht
import bluetooth as blue
import temp_iot as iot
import time

#Flags
ml=0
mq=0
bl=0

while True:
 dht.DHT()
 time.sleep(1)
 iot.thermometer()
 while( ml <= 5):
  mu.ultra()
  time.sleep(1)
  ml+=1
 ml=0
 if(mq == 0):
  msg.MQ()
  mq+=1
  print("Message")
 mq=0
 while(bl <= 5):
  blue.blue()
  bl+=1
 bl=0
 time.sleep(5)
