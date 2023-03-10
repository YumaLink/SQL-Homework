insert into janr(name)
		values('rock'), ('jazz'), ('rnb'), ('rap'), ('Electronic');
		
insert into artist(name)
		values('Земфира'), ('Queen'), ('Frank Sinatra'), ('Louis Armstrong'),
				('Rihanna'), ('Masego'), ('Eminem'), ('The Prodigy');
				
insert into janr_artist(janr_id, artist_id)
		values(1, 1), (1, 2), (2, 3), (2, 4),
				(3, 5), (3, 6), (4, 7), (5, 8);
				
insert into album(name, year_of_release)
		values('СПАСИБО', 2007), ('Hot Space', 1982), ('My Way', 1969),
				('Stardust', 1988), ('You Da One', 2011), ('Lady Lady', 2018),
				('Kamikaze', 2018), ('Omen', 2008);
				
insert into artist_album(artist_id, album_id)
		values(1, 1), (2, 2), (3, 3), (4, 4),
				(5, 5), (6, 6), (7, 7), (8, 8);

insert into track(name, duration, album_id)
		values('Дом', 230, 1), ('1000 лет', 250, 1), ('Dancer', 230, 2),
				('Cool Cat', 209, 2), ('Yesterday', 235, 3), ('My Way', 276, 3),
				('Honey, Do!', 160, 4), ('Mighty River', 166, 4), ('You Da One mix1', 231, 5),
				('You Da One mix2', 476, 5), ('Sugar Walls', 122, 6), ('Lady Lady', 158, 6),
				('The Ringer', 337, 7), ('Greatest', 226, 7), ('Omen', 194, 8);
				
insert into collection(name, year_of_release)
		values('Сборник Рок', 2015), ('Сборник Jazz', 2010), ('Сборник RnB', 2020),
				('Сборник Рэп', 2020), ('Сборник Electronic', 2012), ('Сборник Лучшие', 2022),
				('Сборник Популярное', 2021), ('Сборник лучшее из старых', 2010);
				
insert into collection_track(track_id, collection_id)
		values(1, 1), (4, 1), (6, 2), (7, 2),
				(9, 3), (11, 3), (13, 4), (14, 4),
				(15, 5), (2, 6), (3, 6), (12, 7),
				(5, 8), (8, 8), (10, 3);
				
insert into album(name, year_of_release)
		values('Крым', 2020);
	
insert into janr_artist(janr_id, artist_id)
		values(4, 6);
	
insert into track(name, duration, album_id)
		values('Крым', 202, 9);


		