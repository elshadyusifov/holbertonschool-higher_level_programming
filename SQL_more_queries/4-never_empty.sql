-- Create the table 'id_not_null' if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,          -- id has a default value of 1
  name VARCHAR(256)          -- name field, no NOT NULL constraint
);

