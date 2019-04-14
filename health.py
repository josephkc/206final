from yelp.client import Client
import json
import requests
import sqlite3
import re

MY_API_KEY = "2DpBTLaOVW58XXsNb3Co7v16k4HbdCfYT1-Fv-OUSubypgNCyBRjQky5xCg97GfIYqfEDu4grwKNecEw5hSdC4AuPV7LOxr-0oCzXrWbm_19lKN_pefao5kEarGqXHYx" 
headers = {'Authorization': 'Bearer %s' % MY_API_KEY}

url='https://api.yelp.com/v3/businesses/search'
params = {'term' : 'restaurants', 'location':'New York City', 'sort_by': 'rating', 'limit': "1"}

client = Client(MY_API_KEY)
req=requests.get(url, params=params, headers=headers)
 
# proceed only if the status code is 200
#print('The status code is {}'.format(req.status_code))


# printing the text from the response 
yelp_obj  =json.loads(req.text)
yelpdata_dict = {'restaurant': yelp_obj['businesses'][0]['name'], 'cuisine': yelp_obj['businesses'][0]['categories'][0]['alias'], 'location': params['location']}

#create connection with database

conn = sqlite3.connect('yelp.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Yelp")
cur.execute('CREATE TABLE Yelp (restaurant TEXT, cuisine TEXT, location TEXT)')

for restaurant in yelpdata_dict:
    restaurant = yelpdata_dict['restaurant']
    cuisine = yelpdata_dict['cuisine']
    location = yelpdata_dict['location']

    cur.execute('''INSERT OR IGNORE INTO Yelp (restaurant, cuisine, location)
        VALUES ( ?, ?, ? )''', ( restaurant, cuisine, location ) )
conn.commit()

#print (req.text)


