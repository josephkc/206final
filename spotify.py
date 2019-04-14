#SI206 Final Project
#Christina Li, Carolyn Wu, Joseph Choi

#This project will grab data from the Nutritionix API and...FILL THIS IN!!

import requests
import json
import sqlite3


lst_fruit = ["apple", "banana", "pear", "grapes", "persimmon", "kiwi", "blueberries", "watermelon", "grapefruit", "guava", "plum", "mango", "peach", "cantaloupe", "pomegranate", "papaya", "apricot", "cranberry", "blackberries", "nectarine"]

fruit_dct = {}

for x in lst_fruit:
    fruit = x

    r = requests.get("https://nutritionix-api.p.rapidapi.com/v1_1/search/" + str(fruit) + "?fields=item_name%2Cnf_calories%2Cnf_total_fat",
    headers={
        "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
        "X-RapidAPI-Key": "cf4e917886msh55aa777294792f6p184fc7jsn65800e83c44f"
    }
    )

    req_obj = json.loads(r.text)

    fruit_dct[fruit] = []

    fruit_dct[fruit].append((req_obj['hits'][1]['fields']['item_name']))
    fruit_dct[fruit].append((req_obj['hits'][1]['fields']['nf_calories']))
    fruit_dct[fruit].append((req_obj['hits'][1]['fields']['nf_total_fat']))

conn = sqlite3.connect('nutrition.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Nutrition")
cur.execute('CREATE TABLE Nutrition (food TEXT, cals INTEGER, fat INTEGER)')

for f in fruit_dct:
    fruit = fruit_dct[f][0]
    cals = fruit_dct[f][1]
    fat = fruit_dct[f][2]

    cur.execute('''INSERT OR IGNORE INTO Nutrition (food, cals, fat) 
        VALUES ( ?, ?, ? )''', ( fruit, cals, fat ) )
conn.commit()

#the code below grabs data 20 vegetables
lst_vegetables = ["carrot", "lettuce", "celery", "kale", "cauliflower", "eggplant", "onion", "zucchini", "pumpkin", "artichoke", "peas", "asparagus", "beets", "chayote", "collards", "edamame", "leeks", "okra", "radish", "turnip"]

vegetables_dct = {}

for x in lst_vegetables:
    vegetable = x

    r = requests.get("https://nutritionix-api.p.rapidapi.com/v1_1/search/" + str(vegetable) + "?fields=item_name%2Cnf_calories%2Cnf_total_fat",
    headers={
        "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
        "X-RapidAPI-Key": "cf4e917886msh55aa777294792f6p184fc7jsn65800e83c44f"
    }
    )

    req_obj = json.loads(r.text)

    vegetables_dct[vegetable] = []

    vegetables_dct[vegetable].append((req_obj['hits'][1]['fields']['item_name']))
    vegetables_dct[vegetable].append((req_obj['hits'][1]['fields']['nf_calories']))
    vegetables_dct[vegetable].append((req_obj['hits'][1]['fields']['nf_total_fat']))

for v in vegetables_dct:
    veg = vegetables_dct[v][0]
    v_cals = vegetables_dct[v][1]
    v_fat = vegetables_dct[v][2]

    cur.execute('''INSERT OR IGNORE INTO Nutrition (food, cals, fat) 
        VALUES ( ?, ?, ? )''', ( veg, v_cals, v_fat ) )
conn.commit()