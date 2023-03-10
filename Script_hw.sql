create table if not exists janr (
	id serial primary key,
	name varchar(50) unique not null
);

create table if not exists artist (
	id serial primary key,
	name varchar(50) unique not null
);

create table if not exists janr_artist (
	janr_id integer references janr(id),
	artist_id integer references artist(id),
	constraint janr_artist_pk primary key (janr_id, artist_id)
);

create table if not exists album (
	id serial primary key,
	name varchar(50) unique not null,
	year_of_release integer not null
);

create table if not exists artist_album (
	artist_id integer references artist(id),
	album_id integer references album(id),
	constraint artist_album_pk primary key (artist_id, album_id)
);

create table if not exists track (
	id serial primary key,
	name varchar(50) unique not null,
	duration integer not null,
	album_id integer references album(id)
);

create table if not exists collection (
	id serial primary key,
	name varchar(50) unique not null,
	year_of_release integer not null
);

create table if not exists collection_track (
	track_id integer references track(id),
	collection_id integer references collection(id),
	constraint collection_track_pk primary key (track_id, collection_id)
);