#!/usr/bin/python3
"""
    write one script that is safe from MySQL injections!
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
                WHERE name = %s \
                ORDER BY states.id ASC", (name_searched, ))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
