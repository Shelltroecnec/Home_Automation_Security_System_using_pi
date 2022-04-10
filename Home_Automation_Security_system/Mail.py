import smtplib
def sendmail():
	from email.MIMEMultipart import MIMEMultipart
	from email.MIMEText import MIMEText
	from email.MIMEImage import MIMEImage
	
	#Below two libraries are for mail attachment testing	
	import mimetypes
	import email.mime.application	

	sender='majorproject2209@gmail.com'
	receiver='majorproject2209@gmail.com'

##################################################################################################

#from to and subject details : 

	msgRoot=MIMEMultipart('alternative') 
	msgRoot['Subject']='!! INTRUDER ALERT !!'
	msgRoot['From']=sender
	msgRoot['To']=receiver
	#msgRoot.preamble='this is a multi-part message in the mime format'

####################################################################################################

#adding text to the body : 

	msgText=MIMEText('!! INTRUDER ALER !!\nOBJECT HAS BEEN DETECTED.')	
	msgRoot.attach(msgText)

####################################################################################################

#adding image to the body : 

	fp=open('/home/pi/Desktop/Shahid/_Project_/Rough/cap.png','rb')
	msgImg=MIMEImage(fp.read())
	fp.close()
	msgRoot.attach(msgImg)

####################################################################################################


#adding attachment to the body : 
#	filename = '/home/pi/Desktop/Shahid/_Project_/Rough.py'
#	fo = open(filename, 'rb')
#	file = email.mime.application.MIMEApplication(fo.read(),_subtype = "py")
#	fo.close()
#	#attach.add_header('Content-Disposition','attachment',filename='mail.py')
#	msgRoot.attach(file)

####################################################################################################

	server=smtplib.SMTP('smtp.gmail.com',587)
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(sender,'mbaex1234')  # password of the mail
	server.sendmail(sender,receiver,msgRoot.as_string())
	server.quit()
	####################################################################################################
if __name__ == '__main__' :
	
	sendmail()


