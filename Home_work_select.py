import sqlite3

with sqlite3.connect("MusicSiteNewCorrectVersion.db") as db:
    cursor = db.cursor()

#название и год выхода альбомов, вышедших в 2018 году
cursor.execute("""SELECT Album.name, Album.year
 FROM Album WHERE year = 2018 """)
for x in cursor.fetchall():
    print(x)

print()
#название и продолжительность самого длительного трека
cursor.execute("""SELECT Track.name, Track.duration
 FROM Track WHERE duration = (SELECT MAX (duration) FROM Track)""")
for x in cursor.fetchall():
    print(x)

print()
#название треков, продолжительность которых не менее 3,5 минуты
cursor.execute("""SELECT Track.name
 FROM Track WHERE duration >= "3:5" """)
for x in cursor.fetchall():
    print(x)

print()
#названия сборников, вышедших в период с 2018 по 2020 год включительно
cursor.execute("""SELECT Collection.name
 FROM Collection WHERE 2018 <= year <= 2020 """)
for x in cursor.fetchall():
    print(x)

print()
#исполнители, чье имя состоит из 1 слова
cursor.execute("""SELECT Musician.name
 FROM Musician WHERE name NOT LIKE '% %' """)
for x in cursor.fetchall():
    print(x)

print()
#название треков, которые содержат слово "мой"/"my"
cursor.execute("""SELECT Track.name
 FROM Track WHERE name LIKE '%%мой%%' """)
for x in cursor.fetchall():
    print(x)
