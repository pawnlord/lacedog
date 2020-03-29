import socket
import sys
import os
import subprocess
port = 0
listening = 1 # how many times to listen
for i in range(len(sys.argv)):
    if sys.argv[i] == '-p':
        i+=1
        port = sys.argv[i]
    if sys.argv[i] == '-L':
        i+=1
        if i < len(sys.argv): 
            listening = int(sys.argv[i])
        else:
            listening = 5

if port == 0:
    print("laceworkdog: Needs port!")
    port = int(input("Port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12345))
host_ip = socket.gethostbyname(socket.gethostname())
print("Connect to: " + host_ip + " on port " + str(port))

while listening != 0:
    s.listen(1)
    c, addr = s.accept()
    c.send(("Welcome to LaceworkDog! this is a Netcat thing.\nyou are on port: " + str(port) + " connected to " + host_ip).encode('utf-8'))
    print("conntection from " + str(addr))
    conntype = c.recv(1024).decode('utf-8')
    print("connection type: " + conntype)
    while True:
        msg = ""
        msg = c.recv(2048).decode('utf-8')
        if msg == "exit":
            break
        if conntype == "backdoor":
            try:
                proc = subprocess.Popen(msg.split(' '),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                                        
                )
                stdout, stderr = proc.communicate()
                c.send(stdout)
            except Exception as e:
                c.send(('laceworkdog: ' + msg + ': Not a command!\nError: ' + str(e)).encode('utf-8'))
    c.close()
    listening-=1


