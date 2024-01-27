import socket
import threading
import os.path
import subprocess

IP = socket.gethostbyname(socket.gethostname())
PORT = 7000
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"

class server():
    stream_lock = threading.Lock()
 
    def __init__(self):
        self.th=[]
        self.server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def starts(self):
        print("[STARTING] Server is starting.")
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.server.bind(('0.0.0.0', 5006)) 
        self.server.listen() 
        print("Server is listening")
        while True:
            conn, addr = self.server.accept()
            op = conn.recv(SIZE).decode(FORMAT)
            conn.send("op recived".encode(FORMAT))
            #print(op)
            if(op=="del"):
                self.th.append(threading.Thread(target=self.removeFiles, daemon=True, args=(conn,)).start())
            elif(op=="add"):
                self.th.append(threading.Thread(target=self.upload, daemon=True, args=(conn,)).start())
            elif(op=="update"):
                self.th.append(threading.Thread(target=self.updateFiles, daemon=True, args=(conn,)).start())
            elif(op=="list"):
                self.th.append(threading.Thread(target=self.listFiles, daemon=True, args=(conn,)).start())
            elif(op=="wc"):
                self.th.append(threading.Thread(target=self.wordCount, daemon=True, args=(conn,)).start())
        
    def upload(self,conn):
        filename= conn.recv(SIZE).decode(FORMAT)  
        filename="storage/"+filename
        print(f"[NEW CONNECTION]  connected.")
        conn.send("Filename recived".encode(FORMAT))
        if (os.path.isfile(filename)):
            conn.send(("File already exist").encode(FORMAT))
        
        else:
            file = open(filename, "w")
            while True:
                data = conn.recv(SIZE).decode(FORMAT)
                if  not data:
                    break
                self.stream_lock.acquire()
                file.write(data)            
                self.stream_lock.release()
                conn.send("File data recived".encode(FORMAT))
                file.close()                                  
        conn.close()
      
    def updateFiles(self,conn):
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[NEW CONNECTION]  connected.") 
        
        conn.send("Filename recived".encode(FORMAT))
        file_client = open("storage/"+filename, "w")
        while True:
            data = conn.recv(SIZE).decode(FORMAT)
            if  not data:
                break
            self.stream_lock.acquire()
            file_client.write(data)
            self.stream_lock.release()
            conn.send("File data received".encode(FORMAT))
            file_client.close()
        conn.close()

    def listFiles(self,conn):
        command = conn.recv(SIZE).decode(FORMAT)
        print ("Command is:",command)
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        op.wait(7)
  
        if op:
            output=str(op.stdout.read())
            #print(output)
            conn.send(output.encode(FORMAT))
        else:
            error=str(op.stderr.read())
            print ("Error:",error)
            conn.send(error.encode(FORMAT))

    def removeFiles(self,conn):
        filename = conn.recv(SIZE).decode(FORMAT)
        filename="storage/"+filename

        command="rm"+" "+filename
        #print ("Command is:",command)
        print(os.path.isfile(filename))
        if (os.path.isfile(filename)):
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            op.wait()
            if op:
                output=str(op.stdout.read())
                #print(output)
                conn.send(output.encode(FORMAT))
            else:
                error=str(op.stderr.read())
                print ("Error:",error)
                conn.send(error.encode(FORMAT))
        else:
            print("File doesn't exist")
            conn.send(("File doesn't exist").encode(FORMAT))
        self.stream_lock.acquire()
        self.stream_lock.release()
        conn.close()
    
    def wordCount(self,conn):
        filename = conn.recv(SIZE).decode(FORMAT)
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
        conn.send(str(word_count).encode(FORMAT))
        






       





