-- Import the database "dump" from "hbtn_0d_tvshows" to your MySQL server.
-- echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -hlocalhost -uroot -p
-- curl 'https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

-- 1. Lists all shows contained in "hbtn_0d_tvshows" that have at least one genre linked.
-- 2. Each record should display: tv_shows.title - tv_show_genres.genre_id.
-- 3. Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
-- 4. You can use only one SELECT statement.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
