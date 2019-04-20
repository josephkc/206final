import json
import sqlite3
from health import *

def calculate(conn, cur):
    dict_count = {}
    cur.execute('SELECT * FROM Yelp')    
    for row in cur:
        if row[1] in dict_count:
            dict_count[row[1]] += 1
        else:
            dict_count[row[1]] = 1
    return dict_count
    cur.close()