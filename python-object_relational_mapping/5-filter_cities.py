#!/usr/bin/python3
"""Takes a state name as an argument and returns a list of all
    cities within that state contained in the hbtn_0e_4_usa database
"""
import MySQLdb
import sys


def cities_by_state():
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        database=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities \
                   JOIN states on cities.state_id = states.id \
                   WHERE states.name = %s \
                   ORDER BY cities.id ASC", (state_name,))

    list_cities = cursor.fetchall()

    cities_str = ", ".join(city[0] for city in list_cities)
    print(cities_str)


if __name__ == "__main__":
    cities_by_state()
