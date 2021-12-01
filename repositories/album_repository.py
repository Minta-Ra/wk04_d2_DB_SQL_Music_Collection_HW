from db.run_sql import run_sql
from models.album import Album

import repositories.artist_repository as artist_repository


# CREATE albums
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


# READ - SELECT single album
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album


# READ - SELECT all albums
def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    # To convert data and append to the list
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums


# DELETE all
def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)


# DELETE single album
def delete(id):
    sql = "DELETE * FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# UPDATE
def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id]
    run_sql(sql, values)


# To see all albums that relates to an artist
# READ - SELECT all by artist
def select_all_by_artist(artist):
    albums = []
    sql = "SELECT * FROM tasks WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['genre'], artist)
        albums.append(album)
    return albums