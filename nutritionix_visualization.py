#this file selects data from the database and calculates the 
#averages of the calories and total fat for each food group
#Then, graph these points onto a scatterplot using plotly.

import sqlite3
import plotly.plotly as py 
import plotly.graph_objs as go 
import statistics

#this function calculates average calories
def calc_average_cals(list_tup, start_pos, end_pos):
    lst_cals = []

    for tup in list_tup[start_pos:end_pos]:
        cals = tup[0]
        lst_cals.append(cals)

    avg = statistics.mean(lst_cals)
    return avg

#this function calculates average grams of fat
def calc_average_fat(list_tup, start_pos, end_pos):
    lst_fat = []

    for tup in list_tup[start_pos:end_pos]:
        fat = tup[1]
        lst_fat.append(fat)

    avg = statistics.mean(lst_fat)
    return avg


#writes calculations of average calories and grams of fat for the six food groups to a txt file
def write_file():
    outFile = open('NutritionData.txt', 'w')

    outFile.write("Average fruit calories: " + str(round(avg_fruit_cals, 2)) + "\n")
    outFile.write("Average fruit grams of fat: " + str(round(avg_fruit_fat, 2)) + "\n")
    outFile.write("Average vegetable calories: " + str(round(avg_veg_cals, 2)) + "\n")
    outFile.write("Average vegetable grams of fat: " + str(round(avg_veg_fat, 2)) + "\n")
    outFile.write("Average carbs calories: " + str(round(avg_carb_cals, 2)) + "\n")
    outFile.write("Average carbs grams of fat: " + str(round(avg_carb_fat, 2)) + "\n")
    outFile.write("Average protein calories: " + str(round(avg_prot_cals, 2)) + "\n")
    outFile.write("Average protein grams of fat: " + str(round(avg_prot_fat, 2)) + "\n")
    outFile.write("Average dairy calories: " + str(round(avg_dairy_cals, 2)) + "\n")
    outFile.write("Average dairy grams of fat: " + str(round(avg_dairy_fat, 2)) + "\n")
    outFile.write("Average dessert calories: " + str(round(avg_dess_cals, 2)) + "\n")
    outFile.write("Average dessert grams of fat: " + str(round(avg_dess_fat, 2)) + "\n")

    outFile.close()


#use plotly to create scatterplot of average cals (x-axis) versus average fat (y-axis)
def create_scatter(data):
    layout = go.Layout(
    title = go.layout.Title(
        text = 'Average Calories verses Average Fat for Six Food Groups',
        xref = 'paper',
        x=0
    ),
    xaxis = go.layout.XAxis(
        title = go.layout.xaxis.Title(
            text = 'Average Calories',
            font = dict(
                family = 'Roboto',
                size = 18,
                color = '#7f7f7f'
            )
        )
    ),

    yaxis = go.layout.YAxis(
        title = go.layout.yaxis.Title(
            text = 'Average Grams of Fat',
            font = dict(
                family = 'Roboto',
                size = 18,
                color = '#7f7f7f'
            )
        )
    )

    )
    fig = go.Figure(data=data, layout=layout)

    print(py.plot(fig, filename = 'scatterplot', auto_open=True))


#use plotly to create bar graph of average calories (y-axis) of each food group
def create_bar(x, y):
    trace6 = go.Bar(
    x = x_axis,
    y = lst_avg_cals,
    marker=dict(
        color=[
            "rgba(255,102,102,0.8)",
            "rgba(153,255,51,0.7)",
            "rgba(255,153,51,0.8)",
            "rgba(102,178,255,0.8)",
            "rgba(255,255,102,0.8)",
            "rgba(178,102,255,0.8)",
        ]
    ),
    )

    data = [trace6]
    layout = go.Layout(
        title=go.layout.Title(
            text='Average Calories for Each Food Group',
            xref='paper',
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="Food Groups",
                font=dict(
                    family="Roboto"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="Average Calories",
                font=dict(
                    family="Roboto"
                )
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)
    print(py.plot(fig, filename="nutrition_bar_graph", auto_open=True))



if __name__ == "__main__":
    conn = sqlite3.connect('nutrition.sqlite')
    cur = conn.cursor()

    cur.execute("SELECT cals, fat FROM Nutrition")
    list_tuples = cur.fetchall()

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

    #write caclulations of averages to txt file
    write_file()
    
    #create scatter plot
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
    create_scatter(data)

    #create bar graph for extra credit
    x_axis = ["Fruits", "Vegetables", "Carbs", "Protein", "Dairy", "Desserts"]
    lst_avg_cals = [avg_fruit_cals, avg_veg_cals, avg_carb_cals, avg_prot_cals, avg_dairy_cals, avg_dess_cals]
    create_bar(x_axis, lst_avg_cals)