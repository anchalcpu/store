import socket
import sys
import threading

SIZE = 2048
FORMAT = "utf-8"
stream_lock = threading.Lock()

class client():
    
    def __init__(self):
        #self.downloadPath=downloads
        self.uploadPath="storage/"
  
    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 5006))
        return client
    
    def uploadFiles(self,filenames):
        #client=self.connect()
        for filename in filenames:
            client=self.connect()
            client.send(("add").encode(FORMAT))
            t=client.recv(SIZE).decode(FORMAT)
            file = open(filename, "r") 
            data = file.read()
            
            client.send((filename).encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)
            print(f" [SERVER]: {msg}")
            client.send(data.encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)
            
            print(f"[SERVER]: {msg}")
            file.close()
        stream_lock.acquire()
        stream_lock.release()
        client.close()

       
    def accessfiles(self,filename):
        client=self.connect()
        client.send(("update").encode(FORMAT))
        t=client.recv(SIZE).decode(FORMAT)
        file = open(filename, "r")
        data = file.read()
        client.send((filename).encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f" [SERVER]: {msg}")
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        file.close()
        
        stream_lock.acquire()
        stream_lock.release()
        client.close()

    def list(self):
        client=self.connect()
        client.send(("list").encode(FORMAT))
        t=client.recv(SIZE).decode(FORMAT)
        cmd="ls store/storage/"
        client.send((cmd).encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        client.close()


    def remove(self,filename):
        client=self.connect()
        client.send(("del").encode(FORMAT))
        t=client.recv(SIZE).decode(FORMAT)
        client.send(filename.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        #print(f"[SERVER]: {msg}")
        #client.send((filename).encode(FORMAT))
        #msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        stream_lock.acquire()
        stream_lock.release()
        client.close()

    def count(self,filename):
        client=self.connect()
        client.send(("wc").encode(FORMAT))
        t=client.recv(SIZE).decode(FORMAT)
        client.send(filename.encode(FORMAT))
        wc = client.recv(SIZE).decode(FORMAT)
        print("Total words:", wc)

    def frequency(self,order):
        client=self.connect()
        client.send(("fwo").encode(FORMAT))
        print(client.recv(SIZE).decode(FORMAT))
        client.send(order.encode(FORMAT))
        print(client.recv(SIZE).decode(FORMAT))

        client.close()









