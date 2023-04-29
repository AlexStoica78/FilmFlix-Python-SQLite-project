from connect import *
from readFilm import *
import time


def delete():
    "  filmID,  title, yearReleased, rating, duration, genre"
    # (1, 'Dance', 'Em Jay', 'Pop')
    idField = input("Enter FilmID of the record to be deleted: ")

    cursor.execute(f"DELETE FROM tblFilms WHERE FilmID = {idField}")
    conn.commit()

    print(f"{idField} deleted from films table")
    time.sleep(3)

    # call/invoke the read films function from the readFilm.py file
    read()


if __name__ == "__main__":
    delete()
