import thread
import os
from Tampilan import *

s = socket(AF_INET, SOCK_STREAM)

HOST = string2 = open('ip.txt', 'r').read()
string3 = open('port.txt', 'r').read()
PORT = int(string3)
conn = ''
s.bind((HOST, PORT))

def ClickAction():
	#Write message to chat window
	EntryText = FilteredMessage(EntryBox.get("0.0",END))
	LoadMyEntry(ChatLog, EntryText)

	#Scroll to the bottom of chat windows
	ChatLog.yview(END)

	#Erace previous message in Entry Box
	EntryBox.delete("0.0",END)
						
	#Send my mesage to all others
	conn.sendall(EntryText)
				
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

#Buat chat di window
ChatLog = Text(base, bd=0, bg="#55afd9", height="8", width="50", font="Arial",)
ChatLog.insert(END, "Menunggu Lawan Chat Join...\n")
ChatLog.config(state=DISABLED)

#Buat scrollbar di window chat
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="pirate")
ChatLog['yscrollcommand'] = scrollbar.set

#Buat button untuk send message
SendButton = Button(base, font=30, text="Send", width="12", height=5,bd=0, bg="#841e08", activebackground="#841e08",command=ClickAction)

#Buat slot untuk mengirim pesan
EntryBox = Text(base, bd=0, bg="#93bccf",width="39", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)

#Meletakan semua posisi
scrollbar.place(x=572,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=570)
EntryBox.place(x=6, y=401, height=60, width=465)
SendButton.place(x=480, y=401, height=60)


def GetConnected():
    s.listen(1)
    global conn
    conn, addr = s.accept()
    LoadConnectionInfo(ChatLog, 'Lawan Chat Mu Connected : ' + str(addr) + '\n-----------------------------------------------------------------------------------------------------------------')
    
    while 1:
        try:
            data = conn.recv(1024)
            LoadOtherEntry(ChatLog, data)
            if base.focus_get() == None:
                playsound('notif.wav')
        except:
            LoadConnectionInfo(ChatLog, '\n [ lawan chatmu disconnected ]\n [ menunggu sampai lawan chat bergabung kembali...] \n  ')
            GetConnected()

    conn.close()
    
thread.start_new_thread(GetConnected,())


base.mainloop()
