#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    cn = MySQLdb.connect(host="localhost", port=3306, user=usr,
                         passwd=pwd, db=db_name, charset="utf8")

    csr = cn.cursor()
    csr.execute("SELECT * FROM states ORDER BY id ASC")
    sql_fetch = csr.fetchall()
    for row in sql_fetch:
        print(row)
    csr.close()
    cn.close()
