-- Creates a MySQL Server user `user_0d_1`
-- and sets a temporary password `user_0d_1_pwd`.
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
