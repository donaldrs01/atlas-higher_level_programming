-- Provides comprehensize list of all TV shows in database alongside their genre(s) (NULL if no genre lsited)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
-- Matches show ID with its corresponding genre based on ID match
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Second join to match resulting genre ID to the name of the genre 
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
-- Uses left join so all values are included (including NULL)