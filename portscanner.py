
#!/usr/bin/python

import socket
import random

sock = socke.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("")
port = 443

def portScanner(port):
	if sock.connect_ex((host,port)):
		print("port %d is closed" % {port})
	else:
		print("port %d is opened" % {port})
portcanner(port)