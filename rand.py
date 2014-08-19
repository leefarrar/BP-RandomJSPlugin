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
	#this is a non looping script, if it was we'd need the below and to pass in an interval
	#threading.Timer(1,poll).start()
 
poll()





