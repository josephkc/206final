import json
import requests 
import urllib
import ssl
import sqlite3
# from private_keys import *

def create_db(conn, cur):
	cur.execute("DROP TABLE IF EXISTS Menus")
	cur.execute('CREATE TABLE Menus (restaurant TEXT, cuisine TEXT)')

def collect_data(conn, cur):
	for page in range(1, 7): #1, 2, 3, 4, 5, 6
		r = requests.get("https://us-restaurant-menus.p.rapidapi.com/restaurants/search?distance=6&lat=42.277060&lon=-83.738076&page=" + str(page),
		headers={
		"X-RapidAPI-Host": "us-restaurant-menus.p.rapidapi.com",
		"X-RapidAPI-Key": "8239bf9de3mshf28d53a7b1a9797p12cb1cjsn907f7900db86"
		}
		)

		result_json = json.loads(r.text)
		list_of_restaurants = result_json['result']['data']

		dict_of_restaurants = {}

		count = 0
		for restaurant in list_of_restaurants:
			if ( (len(restaurant['cuisines']) > 0) and ("New" not in restaurant['cuisines'][0]) and (len(dict_of_restaurants)) < 20 ):
				if ( (len(restaurant['cuisines']) == 1) ):
					dict_of_restaurants[restaurant['restaurant_name']] = restaurant['cuisines'][0]
					count += 1
				elif ( (len(restaurant['cuisines']) > 1) ):
					dict_of_restaurants[restaurant['restaurant_name']] = restaurant['cuisines'][1]
					count += 1

		print("Number of restaurants found: " + str(count))
		print(dict_of_restaurants)

		for entry in dict_of_restaurants.items():
			_restaurant = entry[0]
			_cuisine = entry[1]
			cur.execute('''INSERT OR IGNORE INTO Menus (restaurant, cuisine) 
					VALUES ( ?, ?)''', ( _restaurant, _cuisine ) )

		conn.commit()