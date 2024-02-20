#!/usr/bin/python3
"""Displays all values in 'state' table that match user-inputted argument
"""
import MySQLdb
import sys


def state_filter():
    user = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        db=database_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    #  %s used as placeholder, will be replaced next line with state_name
    cursor.execute(query, (state_name,))

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    state_filter()
