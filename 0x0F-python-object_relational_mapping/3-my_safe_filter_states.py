#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == '__main__':

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    f = sys.argv[4]

    cn = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, passwd=pwd, db=db_name)

    crs = cn.cursor()
    sql = "SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC"
    crs.execute(sql, (f,))
    sql_fa = crs.fetchall()
    for row in sql_fa:
        print(row)
