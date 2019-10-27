import socket
import tkinter
import threading
import ClientGui
class Client:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.mySocket=socket.socket()
    def connect_host(self):
        self.mySocket.connect((self.host,self.port))
        print("connected")
    def recieve_mssg(self):
        while True:
            data=self.mySocket.recv(1024)
            print(str(data,"utf-8"))
            ClientGui.recievedmssg.insert("end",str(data,"utf-8"))
            self.mySocket.send(str.encode("hi"))

def ce():
    client = Client("192.168.56.1", 143)
    client.connect_host()
    client.recieve_mssg()


if __name__ == '__main__':
    window=tkinter.Tk()
    threading.Thread(target=ce).start()
    window.mainloop(0)
