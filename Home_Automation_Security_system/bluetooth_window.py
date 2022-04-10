from Tkinter import *
import serial
s=serial.Serial(port="/dev/ttyS0",baudrate=9600)

def Bluemsg():
 y=s.readline()
 s.write(y)
 print(y)
 txt.insert(1.0,y)

#var=StringVar()
t=Tk()
t.title("Blue")
t.geometry("500x500")
b=Button(t,text="Exit",command=t.destroy,bg="Red")
b.pack()
b1=Button(t,text="Bluetooth Message",command=Bluemsg,fg="Blue")
b1.pack()
txt=Text(t,height=2,width=10,bg="pink")
txt.pack()
t.mainloop()
