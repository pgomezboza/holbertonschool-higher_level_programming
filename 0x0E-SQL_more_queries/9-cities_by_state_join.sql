-- Lists all cities contained in the database hbtn_0d_usa.
-- 1. Each record should display: cities.id - cities.name - states.name.
-- 2. Results must be sorted in ascending order by cities.id.
-- 3. You can use only one SELECT statement.
SELECT cities.id, cities.name, states.name 
FROM cities JOIN states 
WHERE cities.state_id = states.id 
ORDER BY cities.id ASC;
