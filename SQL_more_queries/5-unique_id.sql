-- Creates 'unique_id' table with id and name rows. id value default value is 1 and will always be unique
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE, -- 
    name VARCHAR(256)
);