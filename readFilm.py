from connect import *


def read():
    # select all records from table film  - this select it is not displaying like in database
    cursor.execute("select * from tblFilms")
    # fetch all records from table film    - this will display all records in table songs
    row = cursor.fetchall()
    # loop through all records

    if len(row) == 0:
        print("No data found.")
    else:
        for record in row:
            print(record)

    for record in row:
        print(record)


def printByGenre():
    # print("Here is the output of printing by Genre " + genre)
    # inserting the variable parameter genre into the sql statement
    genre = input("Enter Genre: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE Genre = '{genre}'")
    # create a variable called rows to hold all the records selected from the database
    row = cursor.fetchall()  # fetchall, fetches all the selected records
    # if not data returned then you tell the user
    if len(row) == 0:
        print("No data found.")
    else:
        # loop through all the fetched records held in the variable row
        for record in row:
            print(record)


def printByYear():
    YearReleased = input("Enter Year Released: ")
    cursor.execute(
        f"SELECT * FROM tblFilms WHERE YearReleased = '{YearReleased}'")
    row = cursor.fetchall()
    if len(row) == 0:
        print("No data found.")
    else:
        for record in row:
            print(record)


def printByRating():
    rating = input("Enter Rating: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}'")
    row = cursor.fetchall()
    if len(row) == 0:
        print("No data found.")
    else:
        for record in row:
            print(record)


def printByDuration():
    duration = input("Enter Duration: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE duration = '{duration}'")
    row = cursor.fetchall()
    if len(row) == 0:
        print("No data found.")
    else:
        for record in row:
            print(record)


# run automatically if the parent file readSongs.py is run directly
# otherwise, don't automatically run this file if it is imported in another file
if __name__ == '__main__':
    read()
