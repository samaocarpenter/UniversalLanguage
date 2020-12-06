from utils.objects import Song, Language
import requests


# GENERATOR
# NOTE: this code requires a working apikey
# MxM keys expire after a certain number of uses, so this code cannot be used past
# n_files = 400 or so on a free API key, significantly limiting song indexing.
def pull_music(apikey: str, language: Language, n_files: int = 100) -> Song:
    """
    Generator function yielding songs in the desired language.
    Should pull lyrics and data from Genius or some other database.

    :param apikey: the musixmatch API key
    :param language: language to pull music for
    :param n_files: number of songs to bre returned
    :return: generates song objects
    """
    filter_explicit = True

    url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get"
    page = 1

    parameters = {
        "apikey": apikey,
        "f_lyrics_language": language.code,
        "page_size": min(100, n_files),
        "country": "US",
        "page": page,
        "chart_name": 'mxmweekly'
    }

    while n_files > 0:

        response = requests.get(url, params=parameters)
        songs = response.json()['message']['body']['track_list']

        for song in songs:

            song = song["track"]
            track_id = song['track_id']
            url2 = "https://api.musixmatch.com/ws/1.1/track.lyrics.get"

            small_p = {
                "track_id": track_id,
                "apikey": apikey
            }

            lyrics = requests.get(url2, params=small_p)
            lyrics = lyrics.json()["message"]["body"]["lyrics"]

            if (filter_explicit and not lyrics['explicit']) or not filter_explicit:
                n_files -= 1
                yield Song(song["track_name"], song["artist_name"], lyrics["lyrics_body"][:-58])

        page += 1

        parameters["page_size"] = min(n_files, 100)
        parameters["page"] = page