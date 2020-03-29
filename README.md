# lacedog  
A Netcat clone with less features  
  
## what does it do?
lacedog is meant to imitate some of the features of netcat, including backdoor access, file transfer, and HTTP Requests.  

## usage
unlike netcat, lacedog is separated into client and host. These both have different arguements.  

## host usage
```
python3 lacedog.py [-p port_number] [-L listen_number]  
```
the host is lacedog.py, and uses python 3.  
it has 2 command line arguements, port (-p) and listening times (-L).  
- **-p**: port number to use  
- **-L**: how many times to listen for clients, so you can connect multiple times off of one run.  

## client usage
```
python3 ldclient.py [-httpreq] [-a client_addr] [-p port_number] [-tf file_to_transfer new_file_name]  
```
the client is ldclient.py, also python 3.  
it has more command line arguements, including connection types.  
- **-a:** address of host. **arg:** address.  
- **-p:** port to use. **arg:** port number.  
- **-tf:** use file transfer mode (automatic is backdoor mode). **args:** input file, file to output to on host machine.  
- **-httpreq:** starts the http request functionality. The actual request is prompted for and this has no arguements.  
# connection types

## backdoor
this is the automatic connection type.  
This can execute commands and applications on the host device.  
Thats about it right now.  
cannot change directories yet, but I'm working on it!  
  
## file transfer
```
ldclient.py -a ... -tf file_to_transfer new_file_name 
```  
you don't need to do anything special on the hosts side.  
2 arguements: name of the file you want to transfer, and name of the file you want to write to on the host machine.  

## http requests
```
ldclient.py -httpreq
```
So far, I have tested GET requests to google successfully.  
It will prompt you for the request.  
so far, requests only have the method and request_url working, but I will add more as time goes on.  
the formatting of responses is wonky because some don't decode into utf-8 and some do.  
  
# TODO
- Implement more features  
	- ~~HTTP Requests~~  
		- Needs to format correctly, but cannot decode  
- Figure out how to change directories
- Test on other devices  
	- ~~Linux~~
		- Different Distros
  
## maybes  
- Change file transfer to FTP for file transfer  
	- unlikely, as FTP would be a different type of connection  
- Test on Mac  
