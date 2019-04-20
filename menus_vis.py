from menus import *

import json
import requests 
import urllib
import ssl
import sqlite3

import plotly.plotly as py
import plotly.graph_objs as go

def count_cuisines(cur):
    cuisines_dict = {}
    cur.execute("SELECT cuisine FROM AnnArbor")
    for row in cur:
        if row[0] not in cuisines_dict:
            cuisines_dict[row[0]] = 1
        else:
            cuisines_dict[row[0]] += 1

    return(cuisines_dict)

def calculate_top_five(cuisines_dict):

    cuisines_tuples = cuisines_dict.items()
    tuples = []
    for tup in cuisines_tuples:
        tuples.append(tup)
    cuisines_sorted = sorted(tuples, reverse = True, key = lambda tup: tup[1])

    return cuisines_sorted[:5]

def visualize(tuple_list):
    # py.tools.set_credentials_file(username = "josephkc", api_key="3Q6YJh0ZIkkQuKBdRKb6")
    keys = []
    values = []

    for x in tuple_list:
        keys.append(x[0])
        values.append(x[1])

    trace1 = go.Bar(
    x = keys, 
    y = values
    )
    data = [trace1]

    print(py.plot(data, filename = 'menus_bar_graph', auto_open=True))