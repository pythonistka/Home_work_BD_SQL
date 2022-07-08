# 1 количество исполнителей в каждом жанре
SELECT genre_id, COUNT(*)
FROM MusicianGenre
GROUP BY genre_id


# 2 количество треков, вошедших в альбомы 2019-2020 годов
SELECT COUNT(*) 
FROM Track 
WHERE Track.album_id 
IN (SELECT id 
FROM Album 
WHERE year <= 2020 AND year >= 2019) 


# 2 количество треков, вошедших в альбомы 2019-2020 годов
SELECT COUNT(*)
FROM Track t
JOIN Album a ON t.album_id = a.id
WHERE year <= 2020 AND year >= 2019


# 3 средняя продолжительность треков по каждому альбому
SELECT album_id, AVG (duration)
FROM Track
GROUP BY album_id


# 4 все исполнители, которые не выпустили альбомы в 2020 году
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



# 5 названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
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



# 6 название альбомов, в которых присутствуют исполнители более 1 жанра
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




# 7 наименование треков, которые не входят в сборники
    SELECT name FROM Track WHERE ID NOT IN 
    (
        SELECT track_id
        FROM CollectionTrack
        WHERE CollectionTrack.track_id
    )



# 8 исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
    SELECT name 
    FROM Musician
    WHERE Musician.id
    IN (
        SELECT musician_id
        FROM MusicianAlbum
        WHERE MusicianAlbum.album_id
        IN (
            SELECT album_id
            FROM Track
            WHERE duration = (
                SELECT MIN(duration) FROM Track)
            )
        )    




# 9 название альбомов, содержащих наименьшее количество треков
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

