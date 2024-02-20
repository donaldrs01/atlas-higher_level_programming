#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from hbtn_0e_0_usa database
"""
import MySQLdb
import sys

def list_N_states():
    """Connects with database and lists states with names starting with 'N'
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = user,
        password = password,
        database = database_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'; ")
    #  searches for state names that start with 'N'
    Nstates = cursor.fetchall()
    for state in Nstates:
        print(state)
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_N_states()