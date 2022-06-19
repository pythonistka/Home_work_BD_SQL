-- Комментарий: Создаем таблицы в базе данных
CREATE TABLE IF NOT EXISTS Genre(
id integer PRIMARY KEY,
name text NOT NULL)

CREATE TABLE IF NOT EXISTS Musician(
id integer PRIMARY KEY,
name text NOT NULL,
genre_id integer REFERENCES Genre(id))

CREATE TABLE IF NOT EXISTS Album(
id integer PRIMARY KEY,
musician_id integer REFERENCES Musician(id),
name text NOT NULL,
year integer NOT NULL)

CREATE TABLE IF NOT EXISTS Track(
id integer PRIMARY KEY,
album_id integer REFERENCES Album(id),
name text NOT NULL,
duration integer NOT NULL)