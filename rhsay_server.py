#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, string
import subprocess
import sys

def do_something(x):
	key_code =0
	#if x == "PREV\n":
	#else :
	#	return "NACK"
	retcode = subprocess.call(["/usr/local/bin/rhsay", '"'+x+'"'])
	if(retcode>0):
                print retcode
		return "NACK"
	else:
		return "ACK"

HOST = "127.0.0.1"                 
PORT = 33333

if len(sys.argv)>1:
	HOST = sys.argv[1]
else:
	print "Usage: "+sys.argv[0]+" server_ip"
	sys.exit()

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))

while 1:
	print "Слушаю "+HOST+":"+str(PORT)
	srv.listen(1)            
	sock, addr = srv.accept()
	while 1:
		try:
			pal = sock.recv(1024)
		except:
			break;
		if not pal:
			break
		print "Получено от %s:%s:" % addr, pal
		lap = do_something(pal)
		print "Отправлено %s:%s:" % addr, lap
		sock.send(lap)
	sock.close()
