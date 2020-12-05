import re
regex = re.compile('[^a-zA-Z ]')


class Song:
    def __init__(self, name: str, artist: str, lyrics: str) -> None:
        self.name = name
        self.artist = artist
        self.lyrics = lyrics


class Language:
    def __init__(self, name: str) -> None:
        self.name = name
