-- List all genres of Dexter
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Looks for match between genre ID in tv_genres and genre_id in tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
-- Second join that matches the show_id with the actual name of the show
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;