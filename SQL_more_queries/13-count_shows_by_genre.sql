-- Lists all genres in _tvshows database and displays number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
-- Pulls the name of the genres from one table and the show_id listing from another
FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Identifies matches between genre ID in tv_genres table and genre_id tv_show_genres table
GROUP BY tv_genres.name HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;
