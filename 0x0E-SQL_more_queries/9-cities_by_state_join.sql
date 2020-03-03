-- Lists all cities with their state contained in the
-- database `hbtn_0d_usa`.
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
