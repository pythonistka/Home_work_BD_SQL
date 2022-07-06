import sqlite3

with sqlite3.connect("MusicSiteNewCorrectVersion.db") as db:
    cursor = db.cursor()

cursor.execute("""INSERT INTO Track(album_id, name, duration)
VALUES("10", "Cat work", "2:59")""")
db.commit()

db.close()

