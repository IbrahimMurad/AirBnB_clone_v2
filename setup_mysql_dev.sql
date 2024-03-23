-- Active: 1702391851621@@127.0.0.1@3306
-- create a new database hbnb_dev_db for AirBnB clone project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a new user hbnb_dev in the localhost for AirBnB clone project
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant hbnb_dev all privileges on the database hbnb_dev_db
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- grant hbnb_dev SELECT privileges on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
