"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/candy-data.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)  # skip the first row
    conn = sqlite3.connect("Candy_DB.db")  # name this whatever you want
    c = conn.cursor()
    c.execute(
        "DROP TABLE IF EXISTS Candy_DB"
    )  # check if the table already exists, put the column of our tables below
    c.execute(
        "CREATE TABLE Candy_DB (competitorname, chocolate, fruity, caramel, peanutyalmondy, "
        "nougat, crispedricewafer, hard, bar, pluribus, sugarpercent, pricepercent, winpercent)"
    )

    # insert
    c.executemany(
        "INSERT INTO Candy_DB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", payload
    )
    conn.commit()
    conn.close()
    return (
        "Candy_DB.db"  # he uses this as a test to make sure the assert statement runs
    )


if __name__ == "__main__":
    load()
