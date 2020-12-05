class Song:
    def __init__(self, name: str, artist: str, lyrics: str) -> None:
        self.name = name
        self.artist = artist
        self.lyrics = lyrics

    def __str__(self):
        return self.name + ' by ' + self.artist


class Language:
    def __init__(self, name: str) -> None:
        self.name = name
        self.file = 'databases/' + name + '.db'

    def __str__(self):
        return self.name
