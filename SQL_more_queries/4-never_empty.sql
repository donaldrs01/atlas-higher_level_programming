-- Creates 'id_not_null' table in MYSQL server with id and name rows
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);