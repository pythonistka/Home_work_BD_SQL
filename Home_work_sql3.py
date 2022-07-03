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

db.close()