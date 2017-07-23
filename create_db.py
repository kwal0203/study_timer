#!/usr/bin/python

import sqlite3
import sys

con = sqlite3.connect('User.db')

with con:
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE users( \
        ID INT,              \
        NAME TEXT,           \
        COMP9444 INT,        \
        COMP2041 INT,        \
        MATH3411 INT,        \
        COMP3222 INT,        \
        ALGORITHM INT,       \
        PROJECT  INT,        \
        COMP9444_TIME INT,   \
        COMP2041_TIME INT,   \
        MATH3411_TIME INT,   \
        COMP3222_TIME INT,   \
        ALGORITHM_TIME INT,  \
        PROJECT_TIME  INT)"
    )
    cur.execute(
        "INSERT INTO users VALUES(1, 'Kane', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
