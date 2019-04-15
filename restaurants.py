import json
import requests 
import urllib
import ssl
import sqlite3
# from private_keys import *

# !! no private keys needed !!

r = requests.get("https://us-restaurant-menus.p.rapidapi.com/restaurants/search?distance=50&lat=42.277060&lon=-83.738076",
  headers={
    "X-RapidAPI-Host": "us-restaurant-menus.p.rapidapi.com",
    "X-RapidAPI-Key": "8239bf9de3mshf28d53a7b1a9797p12cb1cjsn907f7900db86"
  }
)

result_json = json.loads(r.text)
list_of_restaurants = result_json['result']['data']

print("Number of restaurants found: " + str(len(list_of_restaurants)))

dict_of_restaurants = {}

for restaurant in list_of_restaurants:
    if (len(restaurant['cuisines']) > 1):
        dict_of_restaurants[restaurant['restaurant_name']] = restaurant['cuisines'][1]
    elif (len(restaurant['cuisines']) == 1):
        dict_of_restaurants[restaurant['restaurant_name']] = restaurant['cuisines'][0]

print(dict_of_restaurants)

conn = sqlite3.connect('annarbor.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS AnnArbor")
cur.execute('CREATE TABLE AnnArbor (restaurant TEXT, cuisine TEXT)')

for entry in dict_of_restaurants.items():
    _restaurant = entry[0]
    _cuisine = entry[1]
    cur.execute('''INSERT OR IGNORE INTO AnnArbor (restaurant, cuisine) 
        VALUES ( ?, ?)''', ( _restaurant, _cuisine ) )

conn.commit()