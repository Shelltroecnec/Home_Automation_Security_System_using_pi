from mail import *
from time  import sleep
from gpiozero import DistanceSensor
object=0.3
dist_sensor = DistanceSensor(echo=23,trigger=24,max_distance=4,threshold_distance=0.3)

def object_in_range(sensor):
 print("Object detected in range (%.1f cm)."%(sensor.distance*100))


def object_out_of_range(sensor):
 print("Object detected out of range (%.1f cm)."%(sensor.distance*100))

print("Press CTRL-C to exit.\n")
while True:
 print("Distance Sensor read %.1f cm."%(dist_sensor.distance*100))
 sleep(1)
 if (object <= dist_sensor):
  sendmail()
#  dist_sensor.when_in_range = object_in_range
#ist_sensor.when_out_of_range = object_out_of_range
