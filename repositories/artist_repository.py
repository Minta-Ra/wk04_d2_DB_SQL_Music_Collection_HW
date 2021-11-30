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


# SELECT single artist
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'])
    return artist


# SELECT all artists
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    # To convert data and append to the list
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists