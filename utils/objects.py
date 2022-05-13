# Representation of language
# These should only be created in this file, below its definition
class Language:

    # Takes name (for reference and file naming), and ISO 639-1 language codes
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code
        self.file = 'databases/' + name + '.db'

    # simple printable look at language
    def __str__(self):
        return self.name


# Creates default languages to be used with corresponding codes
Spanish = Language('spanish', 'es')
English = Language('english', 'en')

# List of languages
langs = [
    Spanish,
    English,
]


class Song:
    # Saves data for the song
    def __init__(self, name: str, artist: str, lyrics: str, id: int, language: Language = English) -> None:
        self.name = name
        self.artist = artist
        self.lyrics = lyrics
        self.id = id
        self.language = language

    # Returns simple string representation of song
    def __str__(self):
        return self.name + ' by ' + self.artist

    # hashing (IMPORTANT FOR SETS)
    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id