import json
import sqlite3
from health import *

def calculate(conn, cur):
    
    cur.execute('SELECT * FROM Yelp') 
    dict_sum = {}
    sum = 0
    
    for row in cur:
        sum = sum + row[1]
        if row[0] % 6 == 0:
            dict_sum[row[2]] = sum/6
            sum = 0
  
    print(dict_sum)
    
    cur.close()