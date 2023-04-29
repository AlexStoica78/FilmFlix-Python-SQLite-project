import sqlite3 as sql  # import the sqlite mode

# database connection object
conn = sql.connect("filmflix.db")  # add the path


cursor = conn.cursor()  # use to query db  by calling its execute method
