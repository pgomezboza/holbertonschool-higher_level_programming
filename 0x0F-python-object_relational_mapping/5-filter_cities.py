#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]

    db_cn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=usr,
            passwd=pwd,
            db=db_name,
            charset="utf8")

    crs = db_cn.cursor()
    sql = "SELECT cities.name\
           FROM cities LEFT JOIN states\
           ON states.id = cities.state_id\
           WHERE states.name = %s\
           ORDER BY cities.id ASC"

    crs.execute(sql, (st_name,))
    sql_rows = crs.fetchall()
    print(", ".join([row[0] for row in sql_rows]))
    crs.close()
    db_cn.close()
