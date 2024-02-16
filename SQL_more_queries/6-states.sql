-- creates database 'hbtn_0d_usa' with the 'states' table. Table has an id row and a name row.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa; -- switches to database before table creation
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY (id) NOT NULL
);