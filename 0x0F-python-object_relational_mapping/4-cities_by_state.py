#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    cn = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=usr,
                         passwd=pwd,
                         db=db_name)

    crs = cn.cursor()
    sql = "SELECT cities.id, cities.name, states.name\
          FROM cities LEFT JOIN states\
          ON states.id = cities.state_id\
          ORDER BY cities.id ASC"

    crs.execute(sql)
    sql_fa = crs.fetchall()

    for row in sql_fa:
        print(row)
    crs.close()
    cn.close()
