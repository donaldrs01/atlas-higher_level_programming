-- List of all cities contained in hbtn_0d_usa database using an inner join
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states on states.id = cities.state_id
ORDER BY cities.id ASC;
-- Tries to match each row in 'cities' table with a matching row in 'states'