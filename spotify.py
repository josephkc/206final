#SI206 Final Project
#Christina Li, Carolyn Wu, Joseph Choi

#This project will grab data from the Spotify API so that we 
#can calculate the frequence of each genre of music in the
#top 50 playlists. Then, we will visually represent our data
#with bar graphs that show the frequence of each genre of music
#in the top 50 playlists. 

import requests
import json
import sqlite3


lst_fruit = ["apple", "banana", "pear", "grapes", "persimmon", "kiwi", "blueberries", "watermelon", "grapefruit", "guava", "plum", "mango", "peach", "cantaloupe", "pomegranate", "papaya", "apricot", "cranberry", "blackberries", "nectarine"]

lst_name_fruit = []
lst_fruit_cals = []
lst_fruit_fat = []

for x in lst_fruit:
    fruit = x

    r = requests.get("https://nutritionix-api.p.rapidapi.com/v1_1/search/" + str(fruit) + "?fields=item_name%2Cnf_calories%2Cnf_total_fat",
    headers={
        "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
        "X-RapidAPI-Key": "cf4e917886msh55aa777294792f6p184fc7jsn65800e83c44f"
    }
    )

    req_obj = json.loads(r.text)

    lst_name_fruit.append((req_obj['hits'][1]['fields']['item_name']))
    lst_fruit_cals.append((req_obj['hits'][1]['fields']['nf_calories']))
    lst_fruit_fat.append((req_obj['hits'][1]['fields']['nf_total_fat']))

print(lst_name_fruit)
print(lst_fruit_cals)
print(lst_fruit_fat)

conn = sqlite3.connect('nutrition.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Nutrition")
cur.execute('CREATE TABLE Nutrition (fruit TEXT, cals INTEGER, fat INTEGER)')

for x in lst_name_fruit:
    fruit = x
    cur.execute('''INSERT OR IGNORE INTO Nutrition (fruit) 
        VALUES ( ? )''', ( fruit ) )

for y in lst_fruit_cals:
    cals = y
    cur.execute('''INSERT OR IGNORE INTO Nutrition (cals) 
        VALUES ( ? )''', ( cals ) )

for z in lst_fruit_fat:
    fat = z
    cur.execute('''INSERT OR IGNORE INTO Nutrition (fat) 
        VALUES ( ? )''', ( fat ) )