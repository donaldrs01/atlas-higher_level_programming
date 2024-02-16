-- Lists all records of second_table except for rows without 'name' value. Values listed in descending order.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;