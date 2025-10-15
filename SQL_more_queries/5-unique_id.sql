-- Create the table 'unique_id' if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,   -- id has a default value of 1 and must be unique
  name VARCHAR(256)          -- name field, no NOT NULL constraint
);

