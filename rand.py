#!/usr/bin/python
import random
import threading
import sys
import socket

hostname=socket.gethostname()
lowRange=int(sys.argv[1])
highRange=int(sys.argv[2])

def poll():
	# Select an even number between user selected range
	print "LF_PYRand1 ", random.randrange(lowRange, highRange, 2), hostname
	#threading.Timer(1,poll).start()
 
poll()





