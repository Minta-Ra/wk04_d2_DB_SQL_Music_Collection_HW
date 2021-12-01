import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()

# Artists
artist_1 = Artist("Apocalyptica")
artist_repository.save(artist_1)

artist_2 = Artist("Queen")
artist_repository.save(artist_2)

# Albums
album_1 = Album("Cult", "Symphonic metal", artist_1)
album_repository.save(album_1)

album_2 = Album("Innuendo", "Rock", artist_2)
album_repository.save(album_2)


all_artists = artist_repository.select_all()
all_albums = album_repository.select_all()


# Print it out to see in terminal
for artist in all_artists:
    print(artist.__dict__)

for album in all_albums:
    print(album.__dict__)


pdb.set_trace()