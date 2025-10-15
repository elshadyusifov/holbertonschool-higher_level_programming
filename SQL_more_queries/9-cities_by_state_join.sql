-- List all cities with their respective states in the required format
SELECT cities.id, cities.name, 
       (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;

