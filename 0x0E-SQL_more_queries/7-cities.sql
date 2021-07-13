-- Creates the database "hbtn_0d_usa" and the table "cities" (in the database hbtn_0d_usa).
-- cities description:
-- 1. id INT unique, auto generated, can’t be null and is a primary key.
-- 2. state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table.
-- 3. name VARCHAR(256) can’t be null.
-- 4. If the database hbtn_0d_usa already exists, your script should not fail.
-- 5. If the table cities already exists, your script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
