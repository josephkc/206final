import json
import sqlite3
from health import *
#import plotly.plotly as py
#import plotly.graph_objs as go

def calculate(conn, cur):
    
    cur.execute('SELECT * FROM Yelp') 
    dict_sum = {}
    sum = 0
    
    for row in cur:
        sum = sum + row[1]
        if row[0] % 6 == 0:
            dict_sum[row[2]] = sum/6
            sum = 0
    json_file = json.dumps(dict_sum)
    f = open("yelp_calculations.json","w")
    f.write(json_file)
    f.close()
    cur.close()
    return dict_sum

    

def create_tuple(dict_sum, n):
    cuisines_tuples = dict_sum.items()
    tuples = []
    for tup in cuisines_tuples:
        tuples.append(tup)
    cuisines_sorted = sorted(tuples, reverse=True, key=lambda tup: tup[1])

    return cuisines_sorted[:n]
'''
def visualize(tuple_list):
    # plotly.tools.set_credentials_file(username = "josephkc", api_key="3Q6YJh0ZIkkQuKBdRKb6")
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
                "rgba(0,128,128,.8)",
                "rgba(222,45,38,.8)",
                "rgba(128,0,128,.8)",
                "rgba(222,222,0,.8)",
                "rgba(0,0,222,.8)",
                "rgba(0,128,128,.8)",
                "rgba(222,45,38,.8)",
                "rgba(128,0,128,.8)",
                "rgba(222,222,0,.8)",
                "rgba(0,0,222,.8)",
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
            text='Average Ratings of Korean Restaurants in Michigan',
            xref='paper',
            x=0
            y = 3
        )
    )
    fig = go.Figure(data=data, layout=layout)
    print(py.plot(fig, filename="yelp_bar_graph", auto_open=True))
    # py.plot(data)
'''