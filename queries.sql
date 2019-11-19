--Add new primary key table used for ORM
ALTER TABLE categories ADD COLUMN id SERIAL PRIMARY KEY;

-- SELECT * FROM TABLE to make sure tables were
-- imported
SELECT * FROM categories;