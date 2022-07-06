import sqlite3

with sqlite3.connect("MusicSiteNewCorrectVersion.db") as db:
    cursor = db.cursor()

cursor.execute("""INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("5", "1")""")
db.commit()

db.close()

