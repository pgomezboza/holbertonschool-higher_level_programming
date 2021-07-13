-- Creates the MySQL server user "user_0d_1":
-- 1. "user_0d_1" should have all privileges on your MySQL server.
-- 2. The "user_0d_1" password should be set to "user_0d_1_pwd".
-- 3. If the user "user_0d_1" already exists, your script should not fail.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
