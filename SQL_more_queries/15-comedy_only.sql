-- Lists only comedies in _tvshow database (by show title)
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
-- Multi-part join to match show ID -> genre ID and then genre ID -> name of genre (comedy)
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;