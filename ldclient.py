import socket
import sys

s = socket.socket()
port = 0
host = '127.0.0.1'

for i in range(len(sys.argv)):
    if sys.argv[i] == '-a':
        host = sys.argv[i]
        i+=1
    if sys.argv[i] == '-p':
        port = int(sys.argv[i])
        i+=1
if port == 0:
    print("Needs Port!")
    port = int(input("Port: "))

s.connect((host, port))
conntype = "backdoor"
print(s.recv(2048).decode('utf-8'))
s.send(conntype.encode('utf-8'))
print("You are in " + conntype + " mode") 
while True:
    msg = input()
    s.send(msg.encode('utf-8'))
    print(s.recv(8192).decode('utf-8'))
    if msg == "exit":
        print("ldclient: exiting!")
        break;
s.close()
