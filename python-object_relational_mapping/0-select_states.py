#!/usr/bin/python3
"""Lists all states in 'hbtn_0e_0_usa' database in MySQL server
"""
import MySQLdb
import sys


def list_all_states():
    """Function that will connect to hbtn_0e_0_usa database and list all states
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         password=password,
                         database=database_name)
    
    cursor = db.cursor()  # creates cursor object

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    allstates = cursor.fetchall()
    for state in allstates:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_states()
