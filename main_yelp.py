from health import *
from calculations_yelp import *

if __name__ == "__main__":
    soup = getSoupObjFromURL("https://www.michigan-demographics.com/cities_by_population")
    conn = sqlite3.connect(r"\Users\Owner'\Documents\si206\206final\nutrition.sqlite")
    cur = conn.cursor()

    get_cities(soup)
    create_table(soup)
    calculate(conn, cur)


    
