class Song:
    genre_count = {}
    artist_count = {}
    count = 0
    artists = set()
    genres = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
            Song.genres.add(self.genre)

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
            Song.artists.add(self.artist)

    @classmethod
    def get_genres(cls):
        return list(cls.genres)

    @classmethod
    def get_artists(cls):
        return list(cls.artists)


# Example usage:
song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
song4 = Song("Sara Smile", "Hall and Oates", "Pop")
song5 = Song("Empire State of Mind", "Jay Z", "Rap")
song6 = Song("Crazy in Love", "Beyonce", "Pop")
song7 = Song("Come as You Are", "Nirvana", "Rock")
song8 = Song("Maneater", "Hall and Oates", "Pop")
song9 = Song("Stan", "Eminem", "Rap")
song10 = Song("Toxic", "Britney Spears", "Pop")
song11 = Song("Smells Like Teen Spirit", "Foo Fighters", "Rock")

print("Genre Count:", Song.genre_count)
print("Artist Count:", Song.artist_count)
print("Total Count:", Song.count)

print("All Genres:", Song.get_genres())
print("All Artists:", Song.get_artists())


