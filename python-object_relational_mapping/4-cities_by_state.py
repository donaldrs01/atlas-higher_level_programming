#!/usr/bin/python3
"""Lists all cities, along with their corresponding state,
in the hbtn_0e_4_usa database
"""
import MySQLdb
import sys


def list_cities():
    user = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        password=password,
        database=database_name
    )

    cursor = db.cursor()

    query = ("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON states.id = cities.state_id \
            ORDER BY cities.id ASC")

    cursor.execute(query)

    list_of_cities = cursor.fetchall()

    for row in list_of_cities:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
