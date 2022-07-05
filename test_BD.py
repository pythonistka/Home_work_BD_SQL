import sqlite3

with sqlite3.connect("TEST.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Genre(
id integer PRIMARY KEY,
name text UNIQUE NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Musician(
id integer PRIMARY KEY,
name text UNIQUE NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS MusicianGenre(
genre_id integer NOT NULL REFERENCES Genre(id),
musician_id integer NOT NULL REFERENCES Musician(id),
constraint MusicianGenre_genre_id_musician_id_pk PRIMARY KEY (genre_id, musician_id));""")

cursor.execute("""INSERT INTO Genre(name)
VALUES("Рок")""")
db.commit()

cursor.execute("""INSERT INTO Genre(name)
VALUES("Поп")""")
db.commit()

cursor.execute("""INSERT INTO Genre(name)
VALUES("Рнб")""")
db.commit()

cursor.execute("""INSERT INTO Genre(name)
VALUES("Джаз")""")
db.commit()

cursor.execute("""INSERT INTO Genre(name)
VALUES("Хип-Хоп")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Red Hot Chili Peppers")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Coldplay")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Полина Гагарина")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Тимати")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Лариса Долина")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Баста")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Дима Билан")""")
db.commit()

cursor.execute("""INSERT INTO Musician(name)
VALUES("Юлия Савичева")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("1", "1")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("1", "2")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("2", "3")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("3", "4")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("4", "5")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("5", "6")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("2", "7")""")
db.commit()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("2", "8")""")
db.commit()

db.close()