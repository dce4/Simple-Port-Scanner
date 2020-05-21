#!/bin/python3
#imports first
import socket
import sys

#checking input lenght and identifying our target with given 2nd argument
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate the hostname to IPv4, "gethosbyname_ex()" for IPv6 support
else:
	print("Valid syntax: python3 simportscan.py <ip or hostname>")

#writing a simple banner
print("="*70)
print("connecting to {}".format(sys.argv[1]))
print("="*70) 

#try-catch, identify s with socket ipv4 and socket, set a timeout, identify result as connecting output, print
try:
	for port in range(1,65535):
		con = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # identify address family as inet IPv4
		socket.setdefaulttimeout(1) # setting a default timeout
		conresult = con.connect_ex((target,port)) # making connection, it returns 0 when it connected, 1 else.
		if conresult == 0: # returns 0 when it succeeds and 1 for else
			print("{}:{} is open".format(target,port))
		con.close() #closing our connection

#write down exceptions of ctrl+c, getaddrinfo and socket.error
except socket.gaierror: #gai stands for getaddrinfo()
	print("Hostname resolution wasn't succesful.")
	sys.exit()
except socket.error:
	print("socket.error based error.")
	sys.exit()
except KeyboardInterrupt:
	print("\nInterrupted.")
	sys.exit()
