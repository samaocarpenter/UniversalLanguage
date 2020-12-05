import re
regex = re.compile('[^a-zA-Z ]')


class Song:
    def __init__(self, name: str, artist: str, lyrics: str) -> None:
        self.name = name
        self.artist = artist

        lyrics = lyrics.lower()
        lyrics = regex.sub('', lyrics)
        self.lyrics = set(lyrics.split(' '))


class Language:
    def __init__(self, name: str) -> None:
        self.name = name
