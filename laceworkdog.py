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
    filename = ""
    if conntype == "filetransfer": # get the new file name
        msg = c.recv(2048).decode('utf-8')
        c.send(("MAKING FILE: " + msg).encode('utf-8'))
        filename = msg
        with open(filename, "w") as f:
            print("made file")
    while True: # main connection loop
        msg = "" # information they sent us
        print("retrieving message...")
        msg = c.recv(2048).decode('utf-8')
        print("msg: " + msg)
        if msg == "exit": # exit condition
            break
        if conntype == "backdoor": # backdoor, for running commands/applications
            try:
                stdout = subprocess.check_output(msg, shell=True).decode('utf-8') + "\ncompleted"
                c.send(stdout.encode('utf-8'))
            except Exception as e:
                c.send(('laceworkdog: ' + msg + ': Not a command!\nError: ' + str(e)).encode('utf-8'))
        if conntype == "filetransfer": # file 
            with open(filename, "a") as file:
                print("WRITING TO FILE: ")
                print("CONTETS: " + msg)
                file.write(msg)
                c.send(("Written " + str(len(msg)) + " to file " + filename).encode('utf-8'))
    c.close()
    listening-=1


