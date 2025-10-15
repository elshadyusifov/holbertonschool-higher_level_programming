-- Select the genre and the number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
-- Join tv_genres with tv_show_genres to link genres to shows
LEFT JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
-- Group the results by genre so we can count the shows for each genre
GROUP BY tv_genres.name
-- Exclude genres with no linked shows (i.e., count greater than 0)
HAVING COUNT(tv_show_genres.show_id) > 0
-- Sort the results by the number of shows in descending order
ORDER BY number_of_shows DESC;

