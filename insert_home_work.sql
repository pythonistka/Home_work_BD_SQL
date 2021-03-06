INSERT INTO Genre(name)
VALUES("Рок");

INSERT INTO Genre(name)
VALUES("Поп");

INSERT INTO Genre(name)
VALUES("Рнб");

INSERT INTO Genre(name)
VALUES("Джаз");

INSERT INTO Genre(name)
VALUES("Хип-Хоп");

INSERT INTO Musician(name)
VALUES("Red Hot Chili Peppers");

INSERT INTO Musician(name)
VALUES("Coldplay");

INSERT INTO Musician(name)
VALUES("Полина Гагарина");

INSERT INTO Musician(name)
VALUES("Тимати");

INSERT INTO Musician(name)
VALUES("Лариса Долина");

INSERT INTO Musician(name)
VALUES("Баста");

INSERT INTO Musician(name)
VALUES("Дима Билан");

INSERT INTO Musician(name)
VALUES("Юлия Савичева");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("1", "1");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("1", "2");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("2", "3");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("3", "4");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("4", "5");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("5", "6");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("2", "7");

INSERT INTO MusicianGenre(genre_id, musician_id)
VALUES("2", "8");

INSERT INTO Album(name, year)
VALUES("Stadium Arcadium", "2006");

INSERT INTO Album(name, year)
VALUES("Everyday Life", "2019");

INSERT INTO Album(name, year)
VALUES("Попроси у облаков", "2007");

INSERT INTO Album(name, year)
VALUES("Олимп", "2016");

INSERT INTO Album(name, year)
VALUES("Погода в доме", "1997");

INSERT INTO Album(name, year)
VALUES("К тебе", "2008");

INSERT INTO Album(name, year)
VALUES("Не молчи", "2015");

INSERT INTO Album(name, year)
VALUES("Магнит", "2021");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("1", "1");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("2", "2");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("3", "3");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("4", "4");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("5", "5");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("6", "6");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("7", "7");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("8", "8");

INSERT INTO Track(album_id, name, duration)
VALUES("1", "Dani California", "4:42");

INSERT INTO Track(album_id, name, duration)
VALUES("1", "Snow", "5:35");

INSERT INTO Track(album_id, name, duration)
VALUES("2", "Sunrise", "2:31");

INSERT INTO Track(album_id, name, duration)
VALUES("2", "Daddy", "4:58");

INSERT INTO Track(album_id, name, duration)
VALUES("3", "Я твоя", "3:17");

INSERT INTO Track(album_id, name, duration)
VALUES("3", "Ты мой", "3:22");

INSERT INTO Track(album_id, name, duration)
VALUES("4", "Домой", "3:06");

INSERT INTO Track(album_id, name, duration)
VALUES("4", "Мага", "3:50");

INSERT INTO Track(album_id, name, duration)
VALUES("5", "Погода в доме", "4:18");

INSERT INTO Track(album_id, name, duration)
VALUES("5", "Диета", "3:25");

INSERT INTO Track(album_id, name, duration)
VALUES("6", "Чувства", "3:12");

INSERT INTO Track(album_id, name, duration)
VALUES("6", "Кино", "3:30");

INSERT INTO Track(album_id, name, duration)
VALUES("7", "Малыш", "3:32");

INSERT INTO Track(album_id, name, duration)
VALUES("7", "Телепорт", "3:16");

INSERT INTO Track(album_id, name, duration)
VALUES("8", "Привет", "3:35");

INSERT INTO Track(album_id, name, duration)
VALUES("8", "Отпусти", "3:46");

INSERT INTO Collection(name, year)
VALUES("Хиты", "2022");

INSERT INTO Collection(name, year)
VALUES("Лучшее", "2021");

INSERT INTO Collection(name, year)
VALUES("Музыкалити", "2020");

INSERT INTO Collection(name, year)
VALUES("Рок", "2021");

INSERT INTO Collection(name, year)
VALUES("Музыкалити 2.0", "2022");

INSERT INTO Collection(name, year)
VALUES("Рок 2.0", "2022");

INSERT INTO Collection(name, year)
VALUES("Лучшее 2.0", "2022");

INSERT INTO Collection(name, year)
VALUES("Русская Попса", "2020");


INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("1", "1");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("3", "1");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("5", "1");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("7", "1");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("2", "2");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("4", "2");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("6", "2");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("8", "2");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("9", "3");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("11", "3");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("13", "3");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("15", "3");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("1", "4");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("2", "4");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("3", "6");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("4", "6");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("10", "5");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("12", "5");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("14", "5");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("16", "5");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("1", "7");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("2", "7");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("3", "7");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("4", "7");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("5", "7");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("6", "8");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("7", "8");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("8", "8");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("15", "8");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("16", "8");

INSERT INTO Album(name, year)
VALUES("Гучи", "2018");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("4", "9");

INSERT INTO Track(album_id, name, duration)
VALUES("9", "Гучи", "3:31");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("17", "8");

INSERT INTO Album(name, year)
VALUES("Cat Style", "2020");

INSERT INTO MusicianAlbum(musician_id, album_id)
VALUES("2", "10");

INSERT INTO Track(album_id, name, duration)
VALUES("10", "Cat Cat Cat", "3:15");

INSERT INTO CollectionTrack(track_id, collection_id)
VALUES("18", "4")

