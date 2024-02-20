#!/usr/bin/python3
"""Takes a state name as an argument and returns a list of all
    cities within that state contained in the hbtb_0e_4_usa database
"""
import MySQLdb
import sys

def cities_by_state():
    user = sys.arg[1]
    password = sys.arg[2]
    database = sys.arg[3]