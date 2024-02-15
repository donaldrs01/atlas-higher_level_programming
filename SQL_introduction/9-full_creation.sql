-- Creates second_table in hbtn_0c_0 database and adds multiple rows
CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserts rows with specified values into second_table
INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);