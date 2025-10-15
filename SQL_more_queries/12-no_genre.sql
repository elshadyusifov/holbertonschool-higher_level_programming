-- Select the title of the TV show and the genre_id associated with the show
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- LEFT JOIN ensures we include all shows even if they don't have an associated genre
LEFT JOIN tv_show_genres
    -- This condition links the TV shows with their respective genres
    ON tv_shows.id = tv_show_genres.show_id
-- Filter out the shows with a genre_id NULL (i.e., no genre is linked)
WHERE tv_show_genres.genre_id IS NULL
-- Sorting the results by show title in ascending order
ORDER BY tv_shows.title ASC;

