from twilio.rest import Client
import time
import smbus
sm=smbus.SMBus(1)
sm.write_byte(0x48,0)
time.sleep(0.2)
#MQ="FIRE ALERT:MQ VALUE :"

def MQ():
 MQ='FIRE ALERT : MQ VALUE :' 
 print("READING VALUE !")
 time.sleep(3) 
 b=sm.read_byte(0x48)
 print b
 time.sleep (1)
 if(b >= 11):
  b=str(b)
  account_sid ="ACfd8f16bf68fbc83457e6f7b1f5c7c0a6" # Put your Twilio account SID here
  auth_token ="c1bfb566dac4852f357d441daadf5c2f" # Put your auth token here
  client = Client(account_sid, auth_token)
  message = client.api.account.messages.create(
  to="+917045860661", # Put your cellphone number here
  from_="+18596818918", # Put your Twilio number here
  body=MQ+b)
  print("RESETTING SENSOR")
  time.sleep(30)


