#! /Users/piotrjankiewicz/code/connector/env python3

import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True,
}


if __name__ == '__main__':
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = ('select * from user')

    cursor.execute(query)

    for (row) in cursor:
        print("%s\n"%row.FirstName)

    cursor.close()
    cnx.close()