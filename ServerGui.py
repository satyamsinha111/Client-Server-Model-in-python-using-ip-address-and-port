from tkinter import *
import threading
import socket
FONT = "Segoe UI"
import Server





hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
def send():
    pass
def se():
    global conn
    myServer = Server.Server(int(portInput.get()))
    myServer.bind()
    status.config(text="Listing to the ports")
    conn, adress = myServer.mySocket.accept()
    print("connected to client")
    conn.send(str.encode("Hello you are connected"))
    status.config(text="Connected to the client")
    while True:
        recievedmssg.insert("end",conn.recv(1024))


def sendmssg():
    conn.send(str.encode(message.get("1.0","end-1c"),"utf-8"))

def threadServer():
    myth=threading.Thread(target=se)
    myth.setDaemon(True)
    myth.start()




# my fonts = Segoe UI,Consolas
if __name__ == '__main__':
    root = Tk()
    root.title("Server Application")
    root.config(bg="#2F363F")
    root.resizable(0, 0)
    root.geometry("600x600")

    ''''
    header part starts here
    '''
    Header = Frame(root, bg="#DAE0E2", height=100, width=600)
    Header.anchor("ne")
    Header.anchor("nw")
    heading = Label(Header, text="Server Application", fg="#2C3335", bg="#DAE0E2")
    heading.config(font=(FONT, 20))
    heading.place(x=175, y=40)
    Header.pack(side="top")
    '''''
    header part ends here
    '''''
    '''''
    body starts here
    '''
    body = Frame(root, height=475, width=600, bg="white")

    ip = Label(body, text="your ip address:", fg="#2C3335", bg="white")
    ip.config(font=(FONT, 10))
    ip.place(x=5, y=5)
    ipaddress = Entry(body, fg="#2C3335", width=20)
    ipaddress.insert(0,IPAddr)
    ipaddress.config(state="disabled")
    ipaddress.place(x=5, y=30)
    port = Label(body, text="Enter your port:", fg="#2C3335", bg="white")
    port.config(font=(FONT, 10))
    port.place(x=5, y=55)
    portInput = Entry(body, fg="#2C3335", width=20)
    portInput.place(x=5, y=80)
    sendBtn = Button(body,text="Start listning",fg="white",bg="#218F76",width=10,height=1,command=threadServer)
    sendBtn.config(font=(FONT, 7))
    sendBtn.place(x=5,y=105)
    entersendmssg = Label(body, text="Enter your message:", fg="#2C3335", bg="white")
    entersendmssg.config(font=(FONT, 10))
    entersendmssg.place(x=5, y=130)
    message = Text(body, fg="#2C3335", width=50, height=5)
    message.place(x=5, y=160)
    sendbtn = Button(body, text="Send", bg="#218F76", fg="white", width=10, height=1,command=sendmssg)
    sendbtn.config(font=(FONT, 7))
    sendbtn.place(x=5, y=250)

    TxtRecievedmssg = Label(body, text="Recieving mssg updates here...", fg="#2C3335", bg="white")
    TxtRecievedmssg.config(font=(FONT, 10))
    TxtRecievedmssg.place(x=5, y=290)
    recievedmssg = Listbox(body, width=65, height=6)

    recievedmssg.place(x=5, y=320)

    body.pack()

    ''''
    body ends here
    '''
    '''''
    footer starts here
    '''
    footer = Frame(root, bg="#DAE0E2", width=600, height=25)
    status = Label(footer,text="Not connected to the client",fg="#B83227",bg="#DAE0E2")
    status.config(font=(FONT, 8))
    status.place(x=10,y=2)
    developerName = Label(footer, text="Developed by Satyam sinha", fg="#2C3335", bg="#DAE0E2")
    developerName.config(font=(FONT, 8))
    developerName.place(x=447, y=2)
    footer.pack(side="bottom")
    ''''
    footer ends here
    '''

    root.mainloop()