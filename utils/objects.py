class Song:
    def __init__(self, name: str, artist: str, lyrics: str) -> None:
        self.name = name
        self.artist = artist
        self.lyrics = lyrics
        self.lyrics.replace('\n', ' ')

    def __str__(self):
        return self.name + ' by ' + self.artist


class Language:
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code
        self.file = 'databases/' + name + '.db'

    def __str__(self):
        return self.name
