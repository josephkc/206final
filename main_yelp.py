from yelp import *
from calculations_yelp import *


if __name__ == "__main__":
    soup = getSoupObjFromURL("https://www.michigan-demographics.com/cities_by_population")
    conn = sqlite3.connect("nutrition.sqlite")

    cur = conn.cursor()

    get_cities(soup)
    create_table(soup)
    calculate(conn, cur)
    top_n = create_tuple(calculate(conn, cur), 20)
    visualize(top_n)


    
