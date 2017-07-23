#Todo:
#1. Add todo list
#2. Manually enter minutes              DONE
#3. Daily minute countdown              DONE
#4. Add in SQR3 memory function
#5. Seperate break timer                DONE
#6. Add function to add/remove subjects

import os
import time
import sys
import sqlite3
import webbrowser
from math import floor

def timer(subject):
    try:
        #get daily time remaining for subject
        db = sqlite3.connect('User.db') 
        cursor = db.cursor()
        sql = "SELECT " + subject + " FROM users WHERE ID = 1";
        cursor.execute(sql)
        minsLeft = cursor.fetchone()[0]
        db.close()
 
        start = time.time()
        while True:
            os.system('clear')
            #current study length
            elapsed = int(time.time() - start)
            print elapsed, "seconds elapsed\n"
            if elapsed > 1500:
                print "Take a break\n"
            #decrement daily subject timer
            minsLeft -= 1
            print int(minsLeft), "seconds left"

            time.sleep(1)
    except KeyboardInterrupt:
        return_time = int(time.time() - start)
    
        #get daily time remaining for subject
        db = sqlite3.connect('User.db') 
        cursor = db.cursor()
        
        #sql command to decrement daily timer
        sql = 'UPDATE users SET ' + subject + '=' + subject + ' - ' + \
        str(return_time) + ' WHERE ID = 1'
        cursor.execute(sql)
        db.commit()
        db.close()
        return return_time 

def rest():
    time.sleep(1)
        
def rest_timer():
    start = time.time()
    try:
        while True:
            os.system('clear')
            #current break length
            elapsed = int(time.time() - start)
            print elapsed, "seconds elapsed\n"
            if elapsed > 300:
                print "Back to work\n"
            time.sleep(1)
    except KeyboardInterrupt:
        return

def main_menu():
    print "Please enter a command:\n"
    print "1.) Start timer"
    print "2.) Add time manually"
    print "3.) Run statistics"
    print "4.) See spaced repetition schedule"
    print "5.) Reset daily time counters"
    print "6.) Exit"
    print "\n> ",

def srs():
    webbrowser.open('http://www.studygs.net/texred2.htm', new=2)
    time.sleep(2)
    os.system('clear')
    print "* two hours per day per subject"
    print "* on algorithm days, two hours CLRS and two hours problems"
    print "  minimum"
    print "* one day off / work on project"
    raw_input("Press any key to continue")

def read_database():
    db = sqlite3.connect('User.db') 
    cursor = db.cursor()
    sql = "SELECT * FROM users"
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        print "\nName: %s"    % results[1]
        print "COMP9444:  %d" % results[2]
        print "COMP2041:  %d" % results[3]
        print "MATH3411:  %d" % results[4]
        print "COMP3222:  %d" % results[5]
        print "Algos:     %d" % results[6]
        print "Project:   %d" % results[7]
        print "COMP9444T: %d" % results[8]
        print "COMP2041T: %d" % results[9]
        print "MATH3411T: %d" % results[10]
        print "COMP3222T: %d" % results[11]
        print "AlgosT:    %d" % results[12]
        print "ProjectT:  %d" % results[13]
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
    
    #carry out database operation
    db = sqlite3.connect('User.db') 
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def reset():
    db = sqlite3.connect('User.db') 
    sql = "UPDATE users SET COMP9444_TIME = 7200"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    sql = "UPDATE users SET PROJECT_TIME = 7200"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    sql = "UPDATE users SET COMP2041_TIME = 7200"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    sql = "UPDATE users SET MATH3411_TIME = 7200"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    sql = "UPDATE users SET COMP3222_TIME = 7200"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    sql = "UPDATE users SET ALGORITHM_TIME = 7200"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def subject_menu():
    print "\nWhich subject?"
    print "1.) COMP9444"
    print "2.) COMP2041"
    print "3.) MATH3411"
    print "4.) COMP3222"
    print "5.) Algorithms"
    print "6.) Project"

def clock():
    while True:
        os.system('clear')
        main_menu()
        command = raw_input()

        if command == '1':
            #select subject to add time to
            subject_menu()
            subject = raw_input();
            
            if subject == '1':
                time = timer("COMP9444_TIME")
                time = int(time)
                add_time("COMP9444", time)
                rest()
            elif subject == '2':
                time = timer("COMP2041_TIME")
                time = int(time)
                add_time("COMP2041", time)
                rest()
            elif subject == '3':
                time = timer("MATH3411_TIME")
                time = int(time)
                add_time("MATH3411", time)
                rest()
            elif subject == '4':
                time = timer("COMP3222_TIME")
                time = int(time)
                add_time("COMP3222", time)
                rest()
            elif subject == '5':
                time = timer("ALGORITHM_TIME")
                time = int(time)
                add_time("ALGORITHM", time)
                rest()
            elif subject == '6':
                time = timer("PROJECT_TIME")
                time = int(time)
                add_time("PROJECT", time)
                rest()
            elif subject == '7':
                rest_timer()
                print "\nReturning to main menu\n"
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
                add_time("COMP2041", time)
                rest()
            elif subject == '3':
                add_time("MATH3411", time)
                rest()
            elif subject == '4':
                add_time("COMP3222", time)
                rest()
            elif subject == '5':
                add_time("ALGORITHM", time)
                rest()
            elif subject == '6':
                add_time("PROJECT", time)
                rest()
        elif command == '3':
            read_database()
        elif command == '4':
            srs()
        elif command == '5':
            reset()
        elif command == '6':
            print "Goodbye"
            exit(0)
clock()
