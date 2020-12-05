from typing import Generator
from utils.objects import Song, Language
import requests
import json


def pull_music(language: Language, n_files: int = 100) -> Generator[Song]:
    """
    Generator function yielding songs in the desired language.
    Should pull lyrics and data from Genius or some other database.

    :param language: language to pull music for
    :param n_files: number of songs to bre returned
    :return: generates song objects
    """
    apikey = "85bc15a0e3c80f2e1112755526e4b80f"
    url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get"
    page = 1
    parameters = {
        "apikey": apikey,
        "f_lyrics_language": language.code,
        "page_size": str(100),
        "country": "XW",
        "page": str(page),
        "chart_name": 'hot'
    }
    while n_files > 0:
        response = requests.get(url, params=parameters)
        if response.status_code != 200:
            raise ConnectionError(
                "Musixmatch returned status code " + str(response.status_code)
            )

