class Album():
    def __init__(self, title, genre, artist, id = None):
        self.title = title
        self.genre = genre
        # I need artist to connect to Artist class
        self.artist = artist
        self.id = id
