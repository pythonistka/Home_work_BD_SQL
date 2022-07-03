import sqlite3

with sqlite3.connect("MusicSiteNewVersion.db") as db:
    cursor = db.cursor()

cursor.execute("""INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("4", "9")""")
db.commit()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("9", "Гучи", "3:31")""")
db.commit()

cursor.execute("""INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("17", "8")""")
db.commit()

db.close()