import json
import requests
import urllib
import ssl
import sqlite3

from menus import *
from menus_vis import *

if __name__ == "__main__":
	conn = sqlite3.connect(r'/Users/josephchoi/Desktop/si206/206final/nutrition.sqlite')
	cur = conn.cursor()
	
	create_db(conn, cur)
	collect_data(conn, cur)

	cuisines_dict = count_cuisines(cur)

	top_five = calculate_top_five(cuisines_dict)
	
	visualize(top_five)