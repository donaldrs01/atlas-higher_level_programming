-- Lists all records in second_table in descending order (best listed first)
SELECT name, score
FROM second_table
ORDER BY score DESC, name ASC;