-- Create the table 'force_name' if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
  id INT PRIMARY KEY,         -- id column is the primary key
  name VARCHAR(256) NOT NULL  -- name column cannot be NULL
);

