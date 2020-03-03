-- Creates the table `unique_id`
-- in MySQL Server with a UNIQUE column.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);
