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

def rest():
    time.sleep(3)

def main_menu():
    print "Please enter a command:\n"
    print "1.) Start timer"
    print "2.) Add time manually"
    print "3.) Run statistics"
    print "4.) Exit"
    print "\n> ",


def subject_menu():
    print "\nWhich subject?"
    print "1.) COMP9444"
    print "2.) COMP3222"
    print "3.) COMP2041"
    print "4.) MATH3411"


def clock():
    while True:
        os.system('clear')
        main_menu()
        command = raw_input()

        if command == '1':
            time = timer()
            subject_menu()
            subject = raw_input();
            if subject == '1':
                print "\nYou studied COMP9444 for %d seconds\n" % time
                rest()
            elif subject == '2':
                print "\nYou studied COMP3222 for %d seconds\n" % time
                rest()
            elif subject == '3':
                print "\nYou studied COMP2041 for %d seconds\n" % time
                rest()
            elif subject == '4':
                print "\nYou studied MATH3411 for %d seconds\n" % time
                rest()
            elif subject == '5':
                print "\nYou worked on a project for %d seconds\n" % time
                rest()
            else:
                print "\nYou had a break for %d seconds\n" % time
                rest()
        elif command == '2':
            os.system('clear')
            print "How much time would you like to add? ",
            time = int(raw_input())
            subject_menu()
            subject = raw_input()
            if subject == '1':
                print "\nAdding %d seconds to COMP9444\n" % time
                rest()
            elif subject == '2':
                print "\nAdding %d seconds to COMP3222\n" % time
                rest()
            elif subject == '3':
                print "\nAdding %d seconds to COMP2041\n" % time
                rest()
            elif subject == '4':
                print "\nAdding %d seconds to MATH3411\n" % time
                rest()
            elif subject == '5':
                print "\nAdding %d seconds to project\n" % time
                rest()
            else:
                print "\nAdding %d seconds to break\n" % time
                rest()
        elif command == '4':
            print "Goodbye"
            exit(0)

clock()
