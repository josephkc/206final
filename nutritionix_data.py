import requests
import json
import sqlite3

def getData(list_items):
    items_dct = {}

    for item in list_items:
        food = item

        r = requests.get("https://nutritionix-api.p.rapidapi.com/v1_1/search/" + str(food) + "?fields=item_name%2Cnf_calories%2Cnf_total_fat",
        headers={
            "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
            "X-RapidAPI-Key": "cf4e917886msh55aa777294792f6p184fc7jsn65800e83c44f"
        }
        )

        req_obj = json.loads(r.text)

        items_dct[food] = []

        items_dct[food].append((req_obj['hits'][1]['fields']['item_name']))
        items_dct[food].append((req_obj['hits'][1]['fields']['nf_calories']))
        items_dct[food].append((req_obj['hits'][1]['fields']['nf_total_fat']))
    
    return items_dct

def createTable(conn, cur):
    cur.execute("DROP TABLE IF EXISTS Nutrition")
    cur.execute('CREATE TABLE Nutrition (food TEXT, cals INTEGER, fat INTEGER)')


def setUpTable(dct, conn, cur):
    for food in dct:
        food_name = dct[food][0]
        cals = dct[food][1]
        fat = dct[food][2]

        cur.execute('''INSERT OR IGNORE INTO Nutrition (food, cals, fat) 
            VALUES ( ?, ?, ? )''', ( food_name, cals, fat ) )
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('nutrition.sqlite')

    cur = conn.cursor()

    lst_fruit = ["apple", "banana", "pear", "grapes", "persimmon", "kiwi", "blueberries", "watermelon", "grapefruit", "guava", "plum", "mango", "peach", "cantaloupe", "pomegranate", "papaya", "apricot", "cranberry", "honeydew", "nectarine"]
    fruit_dct = getData(lst_fruit)
    lst_veggies = ["bokchoy", "chollardgreens", "celery", "kale", "cauliflower", "eggplant", "onion", "zucchini", "pumpkin", "artichoke", "cucumber", "brusselsprouts", "beets", "chayote", "collards", "edamame", "leeks", "okra", "parsnips", "turnip"]
    veg_dct = getData(lst_veggies)
    lst_carbs = ["cornbread", "oatmeal", "wholegrainbread", "rolls", "pretzels", "pita", "cereal", "granola", "cheerios", "bagel", "buns", "pancake", "waffle", "tortilla", "pasta", "rice", "potato", "baguette", "stuffing", "ramen"]
    carbs_dct = getData(lst_carbs)
    lst_proteins = ["chicken", "pork", "groundbeef", "lamb", "sausage", "cod", "turkey", "tuna", "salmon", "lentils", "beans", "chickpeas", "veal", "bacon", "duck", "steak", "hotdog", "patty", "salami", "crab"]
    proteins_dct = getData(lst_proteins)
    lst_dairy = ["skimmilk", "yoghurt", "pudding", "wholemilk", "mozzarella", "creamcheese", "whippedcream", "lassi", "goatmilk", "condensedmilk"]
    dairy_dct = getData(lst_dairy)
    lst_desserts = ["chocolatechipcookie", "brownie", "cake", "glazeddonut", "shortbread", "chocolatebar", "cinnamonroll", "blondie", "tart", "pastry"]
    desserts_dct = getData(lst_desserts)

    createTable(conn, cur)

    setUpTable(fruit_dct, conn, cur)
    setUpTable(veg_dct, conn, cur)
    setUpTable(carbs_dct, conn, cur)
    setUpTable(proteins_dct, conn, cur)
    setUpTable(dairy_dct, conn, cur)
    setUpTable(desserts_dct, conn, cur)