# from urllib.request import urlopen
import urllib
# from bs4 import BeautifulSoup
import bs4
from yelp.client import Client
import json
import requests
import sqlite3
import re
import ssl


MY_API_KEY = "2DpBTLaOVW58XXsNb3Co7v16k4HbdCfYT1-Fv-OUSubypgNCyBRjQky5xCg97GfIYqfEDu4grwKNecEw5hSdC4AuPV7LOxr-0oCzXrWbm_19lKN_pefao5kEarGqXHYx" 
headers = {'Authorization': 'Bearer %s' % MY_API_KEY}


def getSoupObjFromURL(url):
	""" return a soup object from the url """
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	html = urllib.urlopen(url, context=ctx).read()
	soup = bs4.BeautifulSoup(html, "html.parser")
	return soup

def get_cities(soup):
	list_div = soup.find(class_ = 'ranklist span8')
	list_cities = list_div.find_all('a')
	return list_cities


def create_table(soup):
	url='https://api.yelp.com/v3/businesses/search'
	list_hundredcities = []
	count = 0
	while count < 20:
		list_hundredcities.append(get_cities(soup)[count].text)
		count = count + 1
	list_hundredcities.remove('Warren')
	conn = sqlite3.connect('nutrition.sqlite')
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS Yelp")
	cur.execute('CREATE TABLE Yelp (row INTEGER, rating INTEGER, location TEXT)')
	count = 0
	for location in list_hundredcities:
		params = {'term' : 'korean', 'location': location, 'sort_by': 'rating', 'limit': "6"}

		client = Client(MY_API_KEY)
		req=requests.get(url, params=params, headers=headers)
		
		# proceed only if the status code is 200
		#print('The status code is {}'.format(req.status_code))


		# printing the text from the response 
		yelp_obj = json.loads(req.text)
		list_restaurants = yelp_obj['businesses']
		yelpdata_dict = {}
		for restaurant in list_restaurants:
			yelpdata_dict[restaurant['rating']] = location
			count += 1
			# yelpdata_dict = {'rating': i['rating'], 'location': params['location']}
			for entry in yelpdata_dict.items():
				_rating = entry[0]
				_location = entry[1]
				_row = count 

			cur.execute('''INSERT OR IGNORE INTO Yelp (row, rating, location)
				VALUES (?, ?, ? )''', (_row, _rating, _location ) )
			conn.commit()
	
		
		#create connection with database

		




