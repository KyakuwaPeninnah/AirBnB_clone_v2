-- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create new user
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
-- grant all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;
-- grant select privilege to the user
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;


