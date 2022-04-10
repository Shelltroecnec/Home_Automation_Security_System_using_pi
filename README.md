# Home_Automation_Security_System_using_pi
In this Project we use multiple of sensors and Intergrate with Raspberry pi. To develop Home automation with Security

Hardware Used In this Project :
> Raspberry pi 3b+

>DHT11 (Temperature and Humidity Sensor)

>Ultrasoic Sensor -HC-SR-04 (Motion Dectection)

>MQ6 (Gas and Fire Sensor)

>Bluetooth Module (HC-05)

>PCF8591 (I2C Module with ADC)

>USB Camera

Software Used In this Project:
>Twilio (for MSG)

Project Description : 1)In this Project the Temperature Sensor continuosly sense the temperature and Humidity.
2)Ultrasonic sensor contionous sense the area around it, if it detects the motion the Camera will capture Photo and mail to the dedicated mail(Authority) with Subject - Intruder Alert and Captured Photo attached.
3)MQ6 Gas/Fire sensor reads the area around it, if it detect Fire/Gas Leak if willl send the Message to the Authority/Owner using Twilio Services.
4)Bluetooth (HC-05) module is used to wireless turn on LED/DC-FAN and can also send Message if Authority/Owner wants to communicate wirelessly using Bluetooth.

The Project Hardware Setup is Shown below :
![IMG20220221181020](https://user-images.githubusercontent.com/101791916/162619037-48a726ba-478b-4f8f-b7e5-cd4edcbc306e.jpg)
![IMG20220122180252](https://user-images.githubusercontent.com/101791916/162619049-341bcd7d-a042-421c-8890-ab3dc208a770.jpg)
