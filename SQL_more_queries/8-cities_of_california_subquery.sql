-- Using subquery to select all cities in California
SET @cali_id = (SELECT id FROM states WHERE name = 'California');
SELECT id, name FROM cities WHERE state_id = @cali_id
ORDER BY id ASC;