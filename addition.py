import sqlite3

with sqlite3.connect("MusicSiteNewVersion.db") as db:
    cursor = db.cursor()

cursor.execute("""INSERT INTO Album(name, year)
VALUES("Cat Style", "2020")""")
db.commit()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("2", "10")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("10", "Cat Cat Cat", "3:15")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("18", "4")""")
db.commit()

db.close()

