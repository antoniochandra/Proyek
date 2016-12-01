import thread
import os
from Tampilan import *

def CClickAction():
	f = open("ip.txt", "w")
	f.write(IP_txt.get())
	f.close()
	text_file = open("port.txt", "w")
	text_file.write(PORT_txt.get())
	text_file.close()
	filename = 'host.py'
	os.startfile(filename)
	bas.destroy()

def PPressAction(event):
	CClickAction()
def DDisableEntry(event):
	EEntryBox.config(state=DISABLED)

bas = Tk()
bas.title('Informatika UKP Chat')
bas.iconbitmap('icon.ico')
bas.geometry("325x150")
bas.resizable(width=FALSE, height=FALSE)
IP_txt = StringVar()
PORT_txt = StringVar()

#Create the label
IPL= Label(bas,text="IP ADDRESS : ",width="15",height="1")
PORTL= Label(bas,text="PORT : ",width="15",height="1")

#Create tombol button
JOIN = Button(bas, font=10, text="JOIN", width="15", height="1",command=CClickAction)

#Create Text untuk Input
IPBox = Entry(bas, textvariable=IP_txt)
PORTBox = Entry(bas, textvariable=PORT_txt)
IPL.place(x=6,y=22)
IPBox.place(x=128, y=22)

PORTL.place(x=20,y=66)
PORTBox.place(x=128, y=66)

JOIN.place(x=90,y=100)


bas.mainloop()



