#!/usr/bin/python3
"""
    lists all states with the name in input
    from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
        )
    name_searched = sys.argv[4]
    cursor = connection.cursor()
    cursor.execute("SELECT * \
                FROM states \
                WHERE BINARY name = '{}' \
                ORDER BY states.id ASC".format(name_searched))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
