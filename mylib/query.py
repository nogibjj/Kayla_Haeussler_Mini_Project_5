"""Query the database"""

import sqlite3


def create():
    """Create a fake data"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Candy_DB VALUES ('Data Engineering','0','0','0','0', '0','0','0','0', '0','0','0','0')"
    )
    conn.commit()
    conn.close()
    return "Sucessfully created!"


def read():
    """Read and print the database for all the rows of the candy table"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Candy_DB")
    print(cursor.fetchall())
    conn.close()
    return "Successfully read!"


def update():
    """Update day of week value of 1 and set the births to 1000"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Candy_DB SET competitorname = 'LOSER' WHERE winpercent < '50';"
    )
    conn.commit()
    conn.close()
    return "Successfully updated!"


def delete():
    """Delete all rows where candy contains chocolate"""
    conn = sqlite3.connect("Candy_DB.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Candy_DB WHERE chocolate = '1';")
    conn.commit()
    conn.close()
    return "Sucessfully deleted!"


if __name__ == "__main__":
    create()
    read()
    update()
    delete()
