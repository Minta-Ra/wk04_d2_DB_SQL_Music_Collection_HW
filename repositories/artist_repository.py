from db.run_sql import run_sql
from models.artist import Artist


# CREATE artists
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist 


# READ - SELECT single artist
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'])
    return artist


# READ - SELECT all artists
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    # To convert data and append to the list
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists


# DELETE all
def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)


# DELETE single album
def delete(id):
    sql = "DELETE * FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# UPDATE
def update(artist):
    sql = "UPDATE users SET (name) = (%s) WHERE id = %s"
    values = [artist.name]
    run_sql(sql, values)