import socket
import tkinter
import threading

class Server:
    def __init__(self,port):
        self.port=port
        self.host=""
        self.mySocket=socket.socket()
    def bind(self):
        try:
            self.mySocket.bind((self.host,self.port))
            self.mySocket.listen(5)
            print("listning")
        except socket.error as error:
            print(error)
            self.bind()
    def accept_mssg(self):
        try:
            conn,adress = self.mySocket.accept()
            print("connected to client")
            conn.send(str.encode("Hello you are connected"))



        except socket.error as err:
            print(err)

def se():
    myServer = Server(143)
    myServer.bind()
    myServer.accept_mssg()

if __name__ == '__main__':
    window=tkinter.Tk()
    threading.Thread(target=se).start()
    window.mainloop(0)


