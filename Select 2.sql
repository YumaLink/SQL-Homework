select j.name, count(ja.artist_id) from janr j
		join janr_artist ja on j.id = ja.janr_id
		group by j.name;
   
select a.name, a.year_of_release, count(t.id) from album a 
		join track t on a.id = t.album_id 
		where a.year_of_release between 2019 and 2020
		group by a.name, a.year_of_release;
		
select a.name, avg(t.duration) from album a 
		join track t on a.id = t.album_id 
		group by a.name;
		
select a.name from artist a 
		join artist_album aa on a.id = aa.artist_id 
		join album a2 on a2.id = aa.album_id 
		where a2.year_of_release < 2020;
		
select c.name from collection c 
		join collection_track ct on c.id = ct.collection_id 
		join track t on t.id = ct.track_id 
		join album a on a.id = t.album_id 
		join artist_album aa on a.id = aa.album_id 
		join artist a2 on a2.id = aa.artist_id 
		where a2.name like '%Eminem%';
		
select a.name from album a 
			join artist_album aa on a.id = aa.album_id 
			join artist a2 on a2.id = aa.artist_id 
			join janr_artist ja on ja.artist_id = a2.id 
			join janr j on j.id = ja.janr_id 
			group by a2.name, a.name
		having count(ja.janr_id) > 1;
	
select t.name from track t 
		left join collection_track ct on ct.track_id = t.id 
		where ct.track_id is null;
		
select a.name from artist a 
		join artist_album aa on aa.artist_id = a.id 
		join album a2 on a2.id = aa.album_id 
		join track t on t.album_id = a2.id 
		where duration = (select min(duration) from track);
		
select a.name, count(t.id) from album a 
		join track t on t.album_id = a.id 
		group by a.name
		having count(t.id) in (
			select count(t.id) from album a
			join track t on t.album_id = a.id 
			group by a.name
			order by count (t.id)
			limit 1);
			
