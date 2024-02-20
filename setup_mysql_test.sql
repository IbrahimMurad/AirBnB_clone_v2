-- This script that prepares a MySQL server for the project

-- create a new database hbnb_test_db for AirBnB clone project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a new user hbnb_test in the localhost for AirBnB clone project
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant hbnb_test all privileges on the database hbnb_test_db
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- grant hbnb_test SELECT privileges on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
