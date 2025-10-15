-- Select the genre names for the show 'Dexter'
SELECT tv_genres.name
FROM tv_genres
-- Join tv_genres with tv_show_genres to link genres to shows
INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
-- Join tv_show_genres with tv_shows to get the genres for the show 'Dexter'
INNER JOIN tv_shows
    ON tv_shows.id = tv_show_genres.show_id
-- Filter the results for the show 'Dexter'
WHERE tv_shows.title = 'Dexter'
-- Sort the results by genre name in ascending order
ORDER BY tv_genres.name ASC;

