#!/usr/bin/python3
"""Lists all states in 'hbtb_0d_usa' database using MySQLdb module
"""
import MySQLdb
import sys


def list_all_states(user, password, db_name):
    """Function that will connect to hbtn_0e_0_usa database and list all states

    Args:
        user (str): MYSQL username
        password (str): MYSQL password
        db_name (str): name of database from MYSQL server
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         password=password,
                         database=db_name)
    cursor = db.cursor()  # creates cursor object
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    allstates = cursor.fetchall()
    for state in allstates:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
