-- settings.sql
CREATE DATABASE oils;
CREATE USER oilsuser WITH PASSWORD 'oils';
GRANT ALL PRIVILEGES ON DATABASE oils TO oilsuser;
