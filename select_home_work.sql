SELECT Album.name, Album.year
FROM Album WHERE year = 2018

SELECT Track.name, Track.duration
FROM Track WHERE duration = (SELECT MAX (duration) FROM Track)

SELECT Track.name
FROM Track WHERE duration > "3:5"

SELECT Collection.name
FROM Collection WHERE 2018 < year < 2020

SELECT Musician.name
FROM Musician WHERE name NOT LIKE '% %'

SELECT Track.name
FROM Track WHERE name LIKE '%%мой%%' OR name LIKE '%my%'