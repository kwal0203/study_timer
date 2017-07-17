#Todo:
#1. Add todo list
#2. Manually enter minutes DONE
#3. Daily minute countdown

import os
import time
import sys
import sqlite3
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
    time.sleep(1)

def main_menu():
    print "Please enter a command:\n"
    print "1.) Start timer"
    print "2.) Add time manually"
    print "3.) Run statistics"
    print "4.) Exit"
    print "\n> ",

def read_database():
    db = sqlite3.connect('User.db') 
    cursor = db.cursor()
    sql = "SELECT * FROM users"
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        name = results[1]
        subj1 = results[2]
        subj2 = results[3]
        subj3 = results[4]
        subj4 = results[5]
        subj5 = results[6]
        subj6 = results[7]
        print "\nName: %s" % name
        print "COMP9444: %d" % subj1
        print "COMP3222: %d" % subj2
        print "COMP2041: %d" % subj3
        print "MATH3411: %d" % subj4
        print "Project:  %d" % subj5
        print "Break:    %d" % subj6
        print "\nPress any key to continue",
        finish = raw_input()
    except:
        print "No data mate"
    db.close()

def add_time(subject, time):
    
    #convert raw seconds to hours:minutes:seconds
    hours = time / 3600
    remainder = time % 3600
    minutes = remainder / 60 
    seconds = remainder % 60
    
    #output for user
    print "\nAdding %d hours" % hours,
    print "%d minutes" % minutes,
    print "%d seconds" % seconds,
    print "to " + subject 
    rest()
    
    #sql command to add in raw seconds to database
    sql = 'UPDATE users SET ' + subject + '=' + subject + ' + ' + \
        str(time) + ' WHERE ID = 1'
    
    #debug
    #print "SQL: %s" % sql
    #deb = raw_input()
    
    #carry out database operation
    db = sqlite3.connect('User.db') 
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def subject_menu():
    print "\nWhich subject?"
    print "1.) COMP9444"
    print "2.) COMP3222"
    print "3.) COMP2041"
    print "4.) MATH3411"
    print "5.) Project"
    print "6.) Break"

def clock():
    while True:
        os.system('clear')
        main_menu()
        command = raw_input()

        if command == '1':
            #raw time in seconds
            time = timer()
            time = int(time)

            #select subject to add time to
            subject_menu()
            subject = raw_input();
            
            if subject == '1':
                add_time("COMP9444", time)
                rest()
            elif subject == '2':
                add_time("COMP3222", time)
                rest()
            elif subject == '3':
                add_time("COMP2041", time)
                rest()
            elif subject == '4':
                add_time("MATH3411", time)
                rest()
            elif subject == '5':
                add_time("PROJECT", time)
                rest()
            elif subject == '6':
                add_time("BREAK", time)
                rest()
        elif command == '2':
            os.system('clear')

            print "How much time would you like to add (minutes)? ",
            time = int(raw_input()) * 60
 
            #select subject from menu
            subject_menu()
            subject = raw_input()
 
            if subject == '1':
                add_time("COMP9444", time)
                rest()
            elif subject == '2':
                add_time("COMP3222", time)
                rest()
            elif subject == '3':
                add_time("COMP2041", time)
                rest()
            elif subject == '4':
                add_time("MATH3411", time)
                rest()
            elif subject == '5':
                add_time("PROJECT", time)
                rest()
            elif subject == '6':
                add_time("BREAK", time)
                rest()
        elif command == '3':
            read_database()
        elif command == '4':
            print "Goodbye"
            exit(0)
clock()
