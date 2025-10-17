# Home Automation and Security system using RPi

In this Project we are using multiple of sensors as an inputs for the Home Automation and IOT based security system. 
which we have intergrated with RPi.

**Hardware Used In this Project :**

> Raspberry pi 3b+

>DHT11 (Temperature and Humidity Sensor)

>Ultrasoic Sensor -HC-SR-04 (Motion Dectection)

>MQ6 (Gas and Fire Sensor)

>Bluetooth Module (HC-05)

>PCF8591 (I2C Module with ADC)

>USB Camera

**Software Used In this Project:**

>Twilio (for Messaging service)

-------------------------------------------------------------------------------------------------------------------------------------------------

**Project Description :**

1) In this Project the Temperature Sensor continuosly sense the temperature and Humidity of the surroundings.

2) Ultrasonic sensor continously sense the area around it, and if it detects any motion the USB-camera will capture photo and mail to the dedicated mail (Authority) with Subject which is customizeable.
   *Example:-* Mail Subject: Intruder Alert and Captured Photo attached.
   
4) MQ6 Gas/Fire sensor is also reading the surroundings, if it detect Fire/Gas Leak if will send the message (MSG) to the Authority/Owner using Twilio Services.
   
5) Bluetooth (HC-05) module is used to wirelessly device to turn ON LED/DC-FAN (IOT) and can also send Message if Authority/Owner wants to communicate wirelessly using Bluetooth.

-------------------------------------------------------------------------------------------------------------------------------------------------

The Project Hardware Setup is Shown below :
![IMG20220221181020](https://user-images.githubusercontent.com/101791916/162619037-48a726ba-478b-4f8f-b7e5-cd4edcbc306e.jpg)
![IMG20220122180252](https://user-images.githubusercontent.com/101791916/162619049-341bcd7d-a042-421c-8890-ab3dc208a770.jpg)
