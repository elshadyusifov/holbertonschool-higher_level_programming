-- Select the titles of the shows that belong to the 'Comedy' genre
SELECT tv_shows.title
FROM tv_shows
-- Join tv_show_genres with tv_shows to link shows and their genres
INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
-- Join tv_genres to get the genre name
INNER JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
-- Filter the results to only show 'Comedy' genre
WHERE tv_genres.name = 'Comedy'
-- Sort the results by show title in ascending order
ORDER BY tv_shows.title ASC;

