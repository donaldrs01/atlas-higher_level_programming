-- Lists all shows contained in _tvshows database, regardless of whether genre is listed or not
-- Will display 'NULL' if no genre for show
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Includes all records from left table (tv_shows) regardless of whether there is a match in right table (tv_show_genres)
-- Links 'id' column from tv_shows with 'show_id' column from tv_show_genres
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;