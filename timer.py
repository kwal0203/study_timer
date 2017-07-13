import os
import time
import sys
from math import floor

def timer():
    try:
        start = int(time.time())
        while True:
            os.system('clear')
            print int(time.time()) - start, "seconds elapsed"
            time.sleep(1)
    except KeyboardInterrupt:
       return time.time() - start 

def clock():
    while True:
        print "Please enter a command:",
        command = raw_input()

        if command == 'timer':
            time = timer()
            print "\nYou studied for %d seconds" % time

clock()
