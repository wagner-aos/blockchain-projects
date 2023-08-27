--CREATE DATABASE mydb;

CREATE SCHEMA IF NOT EXISTS mydb;

CREATE TABLE IF NOT EXISTS mydb.movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    released INTEGER NOT NULL,
    rating NUMERIC(2, 1) NOT NULL
);

CREATE TABLE IF NOT EXISTS mydb.users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    hashed_password TEXT NOT NULL,
    UNIQUE(email)
);

--Users
INSERT INTO mydb.users (user_id, name, email, hashed_password) VALUES (1, 'test user', 'test_user@myapi.com', '$2b$12$0id7RjPm.pw/swHqdn4WCeOUUdae1xOxVy7apCotwImixld42o4yG');
--Movies
INSERT INTO mydb.movies (movie_id, title, released, rating) VALUES (1, 'Velozes e Furiosos 150', 2023, 8.1);
INSERT INTO mydb.movies (movie_id, title, released, rating) VALUES (2, 'Indiana Jones', 2023, 8.0);
INSERT INTO mydb.movies (movie_id, title, released, rating) VALUES (3, 'MI-6', 2023, 7.4);
INSERT INTO mydb.movies (movie_id, title, released, rating) VALUES (4, 'O Protetor 3', 2023, 9.5);

