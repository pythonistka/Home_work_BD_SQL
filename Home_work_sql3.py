import sqlite3

with sqlite3.connect("MusicSiteNewVersion.db") as db:
    cursor = db.cursor()

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

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Stadium Arcadium", "2006")""")
db.commit()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Everyday Life", "2019")""")
db.commit()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Попроси у облаков", "2007")""")
db.commit()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Олимп", "2016")""")
db.commit()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Погода в доме", "1997")""")
db.commit()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("К тебе", "2008")""")
db.commit()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Не молчи", "2015")""")
db.commit()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Магнит", "2021")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("1", "1")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("2", "2")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("3", "3")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("4", "4")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("5", "5")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("6", "6")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("7", "7")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("8", "8")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("1", "Dani California", "4:42")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("1", "Snow", "5:35")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("2", "Sunrise", "2:31")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("2", "Daddy", "4:58")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("3", "Я твоя", "3:17")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("3", "Ты мой", "3:22")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("4", "Домой", "3:06")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("4", "Мага", "3:50")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("5", "Погода в доме", "4:18")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("5", "Диета", "3:25")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("6", "Чувства", "3:12")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("6", "Кино", "3:30")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("7", "Малыш", "3:32")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("7", "Телепорт", "3:16")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("8", "Привет", "3:35")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("8", "Отпусти", "3:46")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Хиты", "2022")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Лучшее", "2021")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Музыкалити", "2020")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Рок", "2021")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Музыкалити 2.0", "2022")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Рок 2.0", "2022")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Лучшее 2.0", "2022")""")
db.commit()

cursor.execute("""INSERT INTO Collection(name, year)
VALUES("Русская Попса", "2020")""")
db.commit()


cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("1", "1")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("3", "1")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("5", "1")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("7", "1")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("2", "2")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("4", "2")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("6", "2")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("8", "2")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("9", "3")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("11", "3")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("13", "3")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("15", "3")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("1", "4")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("2", "4")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("3", "6")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("4", "6")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("10", "5")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("12", "5")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("14", "5")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("16", "5")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("1", "7")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("2", "7")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("3", "7")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("4", "7")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("5", "7")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("6", "8")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("7", "8")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("8", "8")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("15", "8")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("16", "8")""")
db.commit()

db.close()
