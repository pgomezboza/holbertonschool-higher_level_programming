#!/usr/bin/python3
"""
lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    cn = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, passwd=pwd, db=db_name)

    crs = cn.cursor()
    crs.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    sql = crs.fetchall()
    for row in sql:
        print(row)
