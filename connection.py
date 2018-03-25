#! /Users/piotrjankiewicz/code/connector/env/bin/python3.6


import mysql.connector
from PrettyTable import PrettyTable

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

    query = ('select FirstName from user')
    cursor.execute(query)

    t = PrettyTable(['Name', 'Age'])
    t.add_row(['Bob', 19])


    for (row) in cursor:
        t.add_row([row])

    print(t)

    cursor.close()
    cnx.close()