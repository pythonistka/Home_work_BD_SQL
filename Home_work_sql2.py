import sqlite3

with sqlite3.connect("MusicSiteNewVersion.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Genre(
id integer PRIMARY KEY,
name text UNIQUE NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Musician(
id integer PRIMARY KEY,
name text UNIQUE NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS MusicianGenre(
genre_id integer REFERENCES Genre(id),
musician_id integer REFERENCES Musician(id),
constraint pk PRIMARY KEY (genre_id, musician_id));""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Album(
id integer PRIMARY KEY,
name text NOT NULL,
year integer NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS MusicianAlbum(
musician_id integer REFERENCES Musician(id),
album_id integer REFERENCES Album(id),
constraint pk PRIMARY KEY (musician_id, album_id));""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Track(
id integer PRIMARY KEY,
album_id integer REFERENCES Album(id) NOT NULL,
name text NOT NULL,
duration time NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Collection(
id integer PRIMARY KEY,
name text NOT NULL,
year integer NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS CollectionTrack(
track_id integer REFERENCES Track(id),
collection_id integer REFERENCES Collection(id),
constraint pk PRIMARY KEY (track_id, collection_id));""")

db.close()
