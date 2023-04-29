from connect import *
from readFilm import *
import time


def insertFilm():
    # create an empty list
    film = []

   # ask for user input for Title, yearReleased, rating duration and genre
   # we don't need filmId as is autoincrement

    title = input("Enter film Title: ")
    yearReleased = input("Enter film year released: ")
    rating = input("Enter film rating: ")
    duration = input("Enter film duration: ")
    genre = input("Enter film genre: ")

    # append data from above to the film list
    film.append(title)
    film.append(yearReleased)
    film.append(rating)
    film.append(duration)
    film.append(genre)
    # or we can do the below way
    # film.extend([title, yearReleased, duration,rating, genre)

    # Insert/add data from the films list into the database in the song table
    cursor.execute(
        "INSERT INTO tblFilms(title,yearReleased, duration, rating, genre) VALUES (?,?,?,?,?)", film)
    # sql injection would be 1 = 1
    conn.commit()  # make changes permanently
    print(f"{title} added to tblFilms table")
    time.sleep(3)  # sleep for 3 second
    read()  # call read function


if __name__ == "__main__":
    insertFilm()  # call insertFilm function

    # FilmID,
