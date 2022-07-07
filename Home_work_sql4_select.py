import sqlite3

with sqlite3.connect("MusicSiteNewCorrectVersion.db") as db:
    cursor = db.cursor()

# 1 количество исполнителей в каждом жанре
cursor.execute("""SELECT genre_id, COUNT(*)
FROM MusicianGenre
GROUP BY genre_id""")
for x in cursor.fetchall():
    print(x)

print()
# 2 количество треков, вошедших в альбомы 2019-2020 годов
cursor.execute("""SELECT COUNT(*) 
FROM Track 
WHERE Track.album_id 
IN (SELECT id 
FROM Album 
WHERE year <= 2020 AND year >= 2019) """)
for x in cursor.fetchall():
    print(x)

print()
# 2 количество треков, вошедших в альбомы 2019-2020 годов
cursor.execute("""SELECT COUNT(*)
FROM Track t
JOIN Album a ON t.album_id = a.id
WHERE year <= 2020 AND year >= 2019""")
for x in cursor.fetchall():
    print(x)

print()
# 3 средняя продолжительность треков по каждому альбому
cursor.execute("""SELECT album_id, AVG (duration)
FROM Track
GROUP BY album_id""")
for x in cursor.fetchall():
    print(x)

print()
# 4 все исполнители, которые не выпустили альбомы в 2020 году
cursor.execute("""
SELECT name FROM Musician WHERE ID NOT IN (
    SELECT musician_id
    FROM MusicianAlbum
    WHERE MusicianAlbum.album_id 
    NOT IN (
        SELECT id 
        FROM Album
        WHERE year != 2020
    )
)
""")
for x in cursor.fetchall():
    print(x)

print()
# 5 названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
cursor.execute("""
SELECT name FROM Collection WHERE ID IN (
    SELECT collection_id
    FROM CollectionTrack
    WHERE CollectionTrack.track_id 
    IN (
        SELECT id 
        FROM Track
        WHERE album_id
        IN (
            SELECT id
            FROM Album
            WHERE Album.id
            IN (
                SELECT album_id
                FROM MusicianAlbum
                WHERE musician_id = 5
                )
            )
        )
)
""")
for x in cursor.fetchall():
    print(x)

print()
# 6 название альбомов, в которых присутствуют исполнители более 1 жанра
cursor.execute("""
    SELECT name
    FROM Album
    WHERE Album.id
    IN (
        SELECT album_id
        FROM MusicianAlbum
        WHERE MusicianAlbum.musician_id
        IN (
            SELECT id
            FROM Musician
            WHERE Musician.id
            IN (
                SELECT musician_id
                FROM MusicianGenre
                GROUP BY musician_id
                HAVING COUNT(musician_id) > 1
                )
            )
        )                 
""")
for x in cursor.fetchall():
    print(x)


print()
# 7 наименование треков, которые не входят в сборники
cursor.execute("""
    SELECT name FROM Track WHERE ID NOT IN 
    (
        SELECT track_id
        FROM CollectionTrack
        WHERE CollectionTrack.track_id
    )
""")
for x in cursor.fetchall():
    print(x)

# 8 исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)





print()
# 9 название альбомов, содержащих наименьшее количество треков
cursor.execute("""
    SELECT name 
    FROM Album
    WHERE id = (
        SELECT album_id FROM (
            SELECT album_id, MIN(track_count) as count
            FROM (
                    SELECT album_id, COUNT(*) AS track_count
                    FROM Track
                    GROUP BY album_id
            )
        )
    )

""")
for x in cursor.fetchall():
    print(x)

