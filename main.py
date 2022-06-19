import sqlite3

with sqlite3.connect("MusicSite.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Genre(
id integer PRIMARY KEY,
name text NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Musician(
id integer PRIMARY KEY,
name text NOT NULL,
genre_id integer REFERENCES Genre(id));""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Album(
id integer PRIMARY KEY,
musician_id integer REFERENCES Musician(id),
name text NOT NULL,
year integer NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Track(
id integer PRIMARY KEY,
album_id integer REFERENCES Album(id),
name text NOT NULL,
duration integer NOT NULL);""")

db.close()

