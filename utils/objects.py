# Wrapper for the song class
class Song:
    # Saves data for the song
    def __init__(self, name: str, artist: str, lyrics: str) -> None:
        self.name = name
        self.artist = artist
        self.lyrics = lyrics
        self.lyrics.replace('\n', ' ')

    # Returns simple string representation of song
    def __str__(self):
        return self.name + ' by ' + self.artist


# Representation of language
# These should only be created in languages.py
class Language:

    # Takes name (for reference and file naming), and ISO 639-1 language codes
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code
        self.file = 'databases/' + name + '.db'

    # simple printable look at language
    def __str__(self):
        return self.name
