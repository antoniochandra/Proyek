import thread
from Tampilan import *

HOST = string2 = open('ip2.txt', 'r').read()
string3 = open('port2.txt', 'r').read()
PORT = int(string3)
s = socket(AF_INET, SOCK_STREAM)


def ClickAction():
	#Write message to chat window
	EntryText = FilteredMessage(EntryBox.get("0.0",END))
	LoadMyEntry(ChatLog, EntryText)

	#Scroll to the bottom of chat windows
	ChatLog.yview(END)

	#Erace previous message in Entry Box
	EntryBox.delete("0.0",END)
				
	#Send my mesage to all others
	s.sendall(EntryText)

def PressAction(event):
	EntryBox.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
	EntryBox.config(state=DISABLED)

#Buat window
base = Tk()
base.title('Informatika UKP Chat')
base.iconbitmap('icon.ico')
base.geometry("600x470")
base.resizable(width=FALSE, height=FALSE)

#Buat chat window
ChatLog = Text(base, bd=0, bg="#55afd9", height="8", width="50", font="Arial",)
ChatLog.insert(END," ")
ChatLog.config(state=DISABLED)

#Scroll bar di chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="pirate")
ChatLog['yscrollcommand'] = scrollbar.set

#Buat Button untuk send message
SendButton = Button(base, font=30, text="Send", width="12", height=5,bd=0, bg="#841e08", activebackground="#841e08",command=ClickAction)

#Buat box untuk enter message
EntryBox = Text(base, bd=0, bg="#93bccf",width="39", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)

#Menempatkan Posisi
scrollbar.place(x=572,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=570)
EntryBox.place(x=6, y=401, height=60, width=465)
SendButton.place(x=480, y=401, height=60)


def ReceiveData():
	try:
		s.connect((HOST, PORT))
		LoadConnectionInfo(ChatLog, '                                              [ Succesfully connected ]\n-----------------------------------------------------------------------------------------------------------------')
	except:
		LoadConnectionInfo(ChatLog, '											   [ Tidak bisa join ]\n-----------------------------------------------------------------------------------------------------------------')
		return
		
	while 1:
		try:
			data = s.recv(1024)
		except:
			LoadConnectionInfo(ChatLog, '\n [ lawan chatmu disconnect ] \n')
			break
		if data != '':
			LoadOtherEntry(ChatLog, data)
			if base.focus_get() == None:
				playsound('notif.wav')
					
		else:
			LoadConnectionInfo(ChatLog, '\n [ lawan chatmu disconnect ] \n')
			break

thread.start_new_thread(ReceiveData,())

base.mainloop()

