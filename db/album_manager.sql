DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    -- ON DELETE CASCADE - Deletes from album and from artist
    artist_id INT REFERENCES artists(id) ON DELETE CASCADE
);