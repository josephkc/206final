from menus import *

import json
import requests
import urllib
# import ssl
import sqlite3

import plotly.plotly as py
import plotly.graph_objs as go


def count_cuisines(cur):
    cuisines_dict = {}
    cur.execute("SELECT cuisine FROM Menus")
    for row in cur:
        if row[0] not in cuisines_dict:
            cuisines_dict[row[0]] = 1
        else:
            cuisines_dict[row[0]] += 1
    
    json_file = json.dumps(cuisines_dict)
    f = open("menus_calculations.json","w")
    f.write(json_file)
    f.close()

    return cuisines_dict


def calculate_top_n(cuisines_dict, n):

    cuisines_tuples = cuisines_dict.items()
    tuples = []
    for tup in cuisines_tuples:
        tuples.append(tup)
    cuisines_sorted = sorted(tuples, reverse=True, key=lambda tup: tup[1])

    return cuisines_sorted[:n]


def visualize(tuple_list):
    keys = []
    values = []

    for x in tuple_list:
        keys.append(x[0])
        values.append(x[1])

    trace1 = go.Bar(
        x=keys,
        y=values,
        marker=dict(
            color=[
                "rgba(0,128,128,.8)",
                "rgba(222,45,38,.8)",
                "rgba(128,0,128,.8)",
                "rgba(222,222,0,.8)",
                "rgba(0,0,222,.8)",
            ]
        ),
    )

    data = [trace1]
    layout = go.Layout(
        title=go.layout.Title(
            text='Most popular cuisines in Ann Arbor',
            xref='paper',
            x=0,
            font = dict(
                family = 'Roboto',
            )   
        ),
        xaxis = go.layout.XAxis(
            title = go.layout.xaxis.Title(
                text = 'Cuisine',
                font = dict(
                    family = 'Roboto',
                )
            )
        ),

        yaxis = go.layout.YAxis(
            title = go.layout.yaxis.Title(
                text = 'Number of restaurants',
                font = dict(
                    family = 'Roboto',
                )
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    print(py.plot(fig, filename="menus_bar_graph", auto_open=True))