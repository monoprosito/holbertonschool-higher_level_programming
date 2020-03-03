-- Creates the table `id_not_null`
-- in MySQL Server with an ID default value.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
