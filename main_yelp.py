from health import *
from calculations_yelp import *

if __name__ == "__main__":
    soup = getSoupObjFromURL("https://www.michigan-demographics.com/cities_by_population")
    # conn = sqlite3.connect(r"\Users\Owner'\Documents\si206\206final\nutrition.sqlite")
    conn = sqlite3.connect(r'/Users/josephchoi/Desktop/si206/206final/nutrition.sqlite')

    cur = conn.cursor()

    

    top_n = create_tuple(calculate(conn, cur), 20)
    visualize(top_n)


    
