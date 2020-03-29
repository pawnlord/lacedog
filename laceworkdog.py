import socket
import sys
import os
import subprocess
port = 0
if len(sys.argv) < 2 or (len(sys.argv) < 3 and sys.argv[:6] == "python"):
    print("laceworkdog: Needs port!")
    port = int(input("Port: "))
elif sys.argv[0] == python:
    print("Port: " + sys.argv[2])
    port = int(sys.argv[2])
else:
    print("Port: " + sys.argv[1])
    port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12345))
host_ip = socket.gethostbyname(socket.gethostname())
print("Connect to: " + host_ip + " on port " + str(port))
s.listen(1)
c, addr = s.accept()
c.send(("Welcome to LaceworkDog! this is a Netcat thing.\nyou are on port: " + str(port) + " connected to " + host_ip).encode('utf-8'))
print("conntection from " + str(addr))
while True:
    msg = ""
    msg = c.recv(2048).decode('utf-8')
    try:
        proc = subprocess.Popen(msg.split(' '),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
                                
        )
        stdout, stderr = proc.communicate()
        c.send(stdout)
    except Exception as e:
        c.send(('laceworkdog: ' + msg + ': Not a command!\nError: ' + str(e)).encode('utf-8'))
    if msg == "exit":
        break
c.close()


