#Todo:
#1. Add todo list
#2. Manually enter minutes
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
        print "COMP9444: %d COMP3222 %d COMP2041 %d MATH3411 %d Project %d Break %d" \
            % (subj1, subj2, subj3, subj4, subj5, subj6)
        print "\nPress any key to continue",
        finish = raw_input()
    except:
        print "No data mate"
    db.close()

def add_time(sql):
    sql = sql
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
            time = timer()
            subject_menu()
            subject = raw_input();
            if subject == '1':
                print "\nAdding %d seconds to COMP9444\n" % time
                var = 'UPDATE users SET COMP9444 = COMP9444 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '2':
                print "\nAdding %d seconds to COMP3222\n" % time
                var = 'UPDATE users SET COMP3222 = COMP3222 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '3':
                print "\nAdding %d seconds to COMP2041\n" % time
                var = 'UPDATE users SET COMP2041 = COMP2041 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '4':
                print "\nAdding %d seconds to MATH3411\n" % time
                var = 'UPDATE users SET MATH3411 = MATH3411 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '5':
                print "\nAdding %d seconds to project\n" % time
                var = 'UPDATE users SET PROJECT = PROJECT + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            else:
                print "\nYou had a break for %d seconds\n" % time
                add_time(var)
                rest()
        elif command == '2':
            os.system('clear')
            print "How much time would you like to add? ",
            time = int(raw_input())
            subject_menu()
            subject = raw_input()
            if subject == '1':
                print "\nAdding %d seconds to COMP9444\n" % time
                var = 'UPDATE users SET COMP9444 = COMP9444 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '2':
                print "\nAdding %d seconds to COMP3222\n" % time
                var = 'UPDATE users SET COMP3222 = COMP3222 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '3':
                print "\nAdding %d seconds to COMP2041\n" % time
                var = 'UPDATE users SET COMP2041 = COMP2041 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '4':
                print "\nAdding %d seconds to MATH3411\n" % time
                var = 'UPDATE users SET MATH3411 = MATH3411 + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            elif subject == '5':
                print "\nAdding %d seconds to project\n" % time
                var = 'UPDATE users SET PROJECT = PROJECT + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
            else:
                print "\nAdding %d seconds to break\n" % time
                var = 'UPDATE users SET BREAK = BREAK + ' + str(time) + ' WHERE ID = 1'
                add_time(var)
                rest()
        elif command == '3':
            read_database()
        elif command == '4':
            print "Goodbye"
            exit(0)
clock()
