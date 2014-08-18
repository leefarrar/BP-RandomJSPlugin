#!/usr/bin/python
import random
import threading
import sys
import socket

hostname=socket.gethostname()
def poll():
	# Select an even number in 100 <= number < 1000
	print "LF_PYRand ", random.randrange(100, 1000, 2), hostname
	threading.Timer(1,poll).start()
 
poll()