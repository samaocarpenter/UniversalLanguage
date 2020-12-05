from utils.objects import Song, Language
import requests


# GENERATOR
def pull_music(language: Language, n_files: int = 100) -> Song:
    """
    Generator function yielding songs in the desired language.
    Should pull lyrics and data from Genius or some other database.

    :param language: language to pull music for
    :param n_files: number of songs to bre returned
    :return: generates song objects
    """
    filter_explicit = True

    apikey = "85bc15a0e3c80f2e1112755526e4b80f"
    url = "https://api.musixmatch.com/ws/1.1/chart.tracks.get"
    page = 1

    parameters = {
        "apikey": apikey,
        "f_lyrics_language": language.code,
        "page_size": min(100, n_files),
        "country": "XW",
        "page": page,
        "chart_name": 'mxmweekly'
    }

    while n_files > 0:

        response = requests.get(url, params=parameters)
        if response.status_code != 200:
            raise ConnectionError(
                "Musixmatch returned status code " + str(response.status_code)
            )

        songs = response.json()['message']['body']['track_list']
        n = len(songs)

        for song in songs:

            song = song["track"]
            track_id = song['track_id']
            url2 = "https://api.musixmatch.com/ws/1.1/track.lyrics.get"

            small_p = {
                "track_id": track_id,
                "apikey": apikey
            }
            lyrics = requests.get(url2, params=small_p)

            if lyrics.status_code != 200:
                raise ConnectionError("Musixmatch returned status code: " + str(lyrics.status_code))

            lyrics = lyrics.json()["message"]["body"]["lyrics"]

            if filter_explicit and not lyrics['explicit']:
                yield Song(song["track_name"], song["artist_name"], lyrics["lyrics_body"][:-58])

        n_files -= n
        page += 1

        parameters["page_size"] = min(n_files, 100)
        parameters["page"] = page

        print(parameters)


def debug():

    n_files = 160
    lang = Language("Spanish", 'es')
    i = 0
    for song in pull_music(lang, n_files):
        print(song)
        print(i := i + 1)


if __name__ == '__main__':
    debug()