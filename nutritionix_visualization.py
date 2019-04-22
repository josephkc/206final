#this file selects data from the database and calculates the 
#averages of the calories and total fat for each food group
#Then, graph these points onto a scatterplot using plotly.

import sqlite3
import plotly.plotly as py 
import plotly.graph_objs as go 
import statistics

def calc_average_cals(list_tup, start_pos, end_pos):
    lst_cals = []

    for tup in list_tup[start_pos:end_pos]:
        cals = tup[0]
        lst_cals.append(cals)

    avg = statistics.mean(lst_cals)
    return avg

def calc_average_fat(list_tup, start_pos, end_pos):
    lst_fat = []

    for tup in list_tup[start_pos:end_pos]:
        fat = tup[1]
        lst_fat.append(fat)

    avg = statistics.mean(lst_fat)
    return avg


if __name__ == "__main__":
    conn = sqlite3.connect('nutrition.sqlite')
    cur = conn.cursor()

    cur.execute("SELECT cals, fat FROM Nutrition")
    list_tuples = cur.fetchall()
    print(list_tuples)

    avg_fruit_cals = calc_average_cals(list_tuples, 0, 20)
    avg_veg_cals = calc_average_cals(list_tuples, 20, 40)
    avg_carb_cals = calc_average_cals(list_tuples, 40, 60)
    avg_prot_cals = calc_average_cals(list_tuples, 60, 80)
    avg_dairy_cals = calc_average_cals(list_tuples, 80, 90)
    avg_dess_cals = calc_average_cals(list_tuples, 90, 100)

    avg_fruit_fat = calc_average_fat(list_tuples, 0, 20)
    avg_veg_fat = calc_average_fat(list_tuples, 20, 40)
    avg_carb_fat = calc_average_fat(list_tuples, 40, 60)
    avg_prot_fat = calc_average_fat(list_tuples, 60, 80)
    avg_dairy_fat = calc_average_fat(list_tuples, 80, 90)
    avg_dess_fat = calc_average_fat(list_tuples, 90, 100)


#use plotly to create scatterplot of average cals (x-axis) versus average fat (y-axis)
trace0 = go.Scatter(
    x = [avg_fruit_cals],
    y = [avg_fruit_fat],
    name = 'Fruits'
)

trace1 = go.Scatter(
    x = [avg_veg_cals],
    y = [avg_veg_fat],
    name = 'Vegetables'
)

trace2 = go.Scatter(
    x = [avg_carb_cals],
    y = [avg_carb_fat],
    name = 'Carbs'
)

trace3 = go.Scatter(
    x = [avg_prot_cals],
    y = [avg_prot_fat],
    name = 'Protein'
)

trace4 = go.Scatter(
    x = [avg_dairy_cals],
    y = [avg_dairy_fat],
    name = 'Dairy'
)

trace5 = go.Scatter(
    x = [avg_dess_cals],
    y = [avg_dess_fat],
    name = 'Desserts'
)

data = [trace0, trace1, trace2, trace3, trace4, trace5]

layout = go.Layout(
    title = go.layout.Title(
        text = 'Average Calories verses Average Fat for Six Food Groups',
        xref = 'paper',
        x=0
    )
    # xaxis = go.layout.XAxis(
    #     title = go.layout.xaxis.Title(
    #         text = 'Average Calories',
    #         font = dict(
    #             family = 'Courier New, monospace',
    #             size = 18,
    #             color = '#7f7f7f'
    #         )
    #     )
    # ),

    # yaxis = go.layout.YAxis(
    #     title = go.layout.yaxis.Title(
    #         text = 'Average Grams of Fat',
    #         font = dict(
    #             family = 'Courier New, monospace',
    #             size = 18,
    #             color = '#7f7f7f'
    #         )
    #     )
    # )
)
fig = go.Figure(data=data, layout=layout)

print(py.plot(fig, filename = 'scatterplot', auto_open=True))