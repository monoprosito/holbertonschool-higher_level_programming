-- Creates the database `hbtn_0d_usa` and
-- the table `states` in MySQL Server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
