#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import serial, time
import ctypes

#initialization and open the port
#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call
#hand commands 

ser0 = serial.Serial()
#ser0.port = "/dev/serial/by-id/usb-067b_2303-if00-port0"
#ser.port = "/dev/ttyS2"
ser0.port = "/dev/rs485_5"
ser0.baudrate = 9600
ser0.bytesize = serial.EIGHTBITS #number of bits per bytes
ser0.parity = serial.PARITY_NONE #set parity check: no parity
ser0.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser0.timeout = 0             #non-block read
#ser.timeout = 2              #timeout block read
ser0.xonxoff = False     #disable software flow control
ser0.rtscts = False     #disable hardware (RTS/CTS) flow control
ser0.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser0.writeTimeout = 2     #timeout for write

is_sleep=0

fname=" "

if len(sys.argv)>1:
  fname = sys.argv[1]
else:
  print "Usage: "+sys.argv[0]+" file.shed"
  sys.exit()

try: 
    ser0.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()
data=[]
lines = [line.strip() for line in open(fname)]
for line in lines:
  lst=line.split(',')
  name=lst[0];
  print name
  start_time=float(lst[1])/1000.0;
  #print start_time
  duration_time=float(lst[2])/1000.0;
  #print duration_time
  i = 3
  while i < len(lst):
    data.append(chr(ctypes.c_ubyte(int(lst[i])).value));
    i=i+1;
  #data_len=i-3;
  i=0
  while i<len(data):
    #ser0.write(' '.join(data[i:i+6]))
    print data[i:i+6]
    #print ' '.join(data[i:i+6])
    for ch in data[i:i+6]:
      print ch
      ser0.write(ch)
      time.sleep(0.002)
    time.sleep(0.01);
    i=i+6
  print "sleep for "+str(duration_time)+" s"
  time.sleep(duration_time)
  
ser0.close()

