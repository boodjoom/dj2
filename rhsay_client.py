#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import math
import time
import sys

HOST = "192.168.0.191"                 
PORT = 33333              
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

#time.sleep(1)
loop=True

def send_text(text_to_say):
	sock.send(text_to_say+"\n")
	ack = sock.recv(1024)
	if(ack=="NACK"):
		print "FAILED"
	else:
		print "OK"

if len(sys.argv)>1:
	text_to_say = sys.argv[1]
	send_text(text_to_say)
	loop = False

while(loop):
	text_to_say=raw_input("text:")
	if(text_to_say=="x"):
		break;
	send_text(text_to_say)
	
sock.close()
