import json
import sqlite3

conn = sqlite3.connect('nutrition.sqlite')
cur = conn.cursor()
cur.execute('SELECT cuisine FROM Yelp')    


cur.close()