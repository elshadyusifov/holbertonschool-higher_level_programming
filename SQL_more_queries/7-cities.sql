-- Create the database 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the 'cities' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- auto-incremented unique id, primary key
  state_id INT NOT NULL,              -- state_id must reference a valid state
  name VARCHAR(256) NOT NULL,         -- name field cannot be null
  FOREIGN KEY (state_id) REFERENCES states(id)  -- foreign key constraint to states table
);

