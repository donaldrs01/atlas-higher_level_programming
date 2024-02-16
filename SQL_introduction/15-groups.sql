-- Displays the number of occurrences of each score in second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score -- groups rows based on shared 'score' value
ORDER BY number DESC;