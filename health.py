from urllib.request import urlopen
from bs4 import BeautifulSoup
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

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup
soup = getSoupObjFromURL("https://www.michigan-demographics.com/cities_by_population")

def get_cities(soup):
        list_div = soup.find(class_ = 'ranklist span8')
        list_cities = list_div.find_all('a')
        return list_cities
url='https://api.yelp.com/v3/businesses/search'
list_hundredcities = []
count = 0
while count < 100:
        list_hundredcities.append(get_cities(soup)[count].text)
        count = count + 1

conn = sqlite3.connect(r"\Users\Owner'\Documents\si206\206final\yelp.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Yelp")
cur.execute('CREATE TABLE Yelp (restaurant TEXT, cuisine TEXT, location TEXT)')
for location in range(len(list_hundredcities)):
        params = {'term' : 'restaurants', 'location': list_hundredcities[location], 'sort_by': 'rating', 'limit': "1"}

        client = Client(MY_API_KEY)
        req=requests.get(url, params=params, headers=headers)
        
        # proceed only if the status code is 200
        #print('The status code is {}'.format(req.status_code))


        # printing the text from the response 
        yelp_obj = json.loads(req.text)
        yelpdata_dict = {'restaurant': yelp_obj['businesses'][0]['name'], 'cuisine': yelp_obj['businesses'][0]['categories'][0]['alias'], 'location': params['location']}

        #create connection with database

        for restaurant in yelpdata_dict:
                _restaurant = yelpdata_dict['restaurant']
                _cuisine = yelpdata_dict['cuisine']
                _location = yelpdata_dict['location']

        cur.execute('''INSERT OR IGNORE INTO Yelp (restaurant, cuisine, location)
                #VALUES ( ?, ?, ? )''', (_restaurant, _cuisine, _location ) )
        conn.commit()


