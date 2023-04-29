from connect import *
from readFilm import *
import time


def update():
    "filmID, title, yearReleased, rating, duration, genre"
    # (1, 'Muppet', 2022, 'PG', 116,"Comedy")

    idField = input("Enter FilmID of the record to be updated: ")
    fieldName = input(
        "Enter( filmID,title, yearReleased, rating, duration, genre) as field name: ")  # .title()
    fieldValue = input(f"Enter the value for the {fieldName} field")
    print(fieldValue)

    fieldValue = "'" + fieldValue + "'"
    print(fieldValue)

    cursor.execute(
        f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID ={idField}")
    conn.commit()  # make the change permanent
    print(f"Record {idField} updated in the tblFilms table")
    time.sleep(3)  # delay for three seconds

    read()


if __name__ == "__main__":

    update()
