from utils.objects import Language, Spanish
from utils.music import pull_music
import pickle
from collections import Counter

def search(
        vocab: list[str], fname: str, n_songs: int = 3,
) -> list[str]:
    """
    :param vocab: list of vocabulary words to be searched for
    :param fname: file for language to be used
    :param n_songs: number of songs to return
    :return: list of n_songs songs, each represented as a string containing:
        (song name) by (artist name)
    """

    # Tries to open up the file
    try:
        with open(fname, 'rb') as f:
            words = pickle.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            'Language input does not have an existing associated database.\n' + repr(e)
        )

    # Tracks usages of words in each song
    counts = Counter()
    for word in vocab:
        if word in words:
            for song in words[word]:
                counts[song] += 1

    # Returns most relevant songs
    ret = []
    for data, _ in counts.most_common(n_songs):
        ret.append(data)

    return ret


def add_files(language: Language, apikey: str, n_files: int = 100) -> None:
    """
    Adds a set amount of songs to a database.

    :param language: the language for the songs
    :param apikey: the apikey for musixmatch
    :param n_files: number of songs to be added
    :return:
    """

    # Attempts to open the file
    try:
        with open(language.file, 'rb') as f:
            vocabulary = pickle.load(f)
    except FileNotFoundError:
        vocabulary = {}

    # retrieves songs and saves them
    for song in pull_music(apikey, language, n_files=n_files):
        lyrics = song.lyrics.lower().split()
        name = str(song)
        for word in lyrics:
            word = ''.join([i for i in word if i.isalpha()])
            if word not in vocabulary and word != '':
                vocabulary[word] = set()
            if word != '':
                vocabulary[word].add(name)

        # In an ideal world this should be outside of the for-loop
        # Sadly, because we use free API keys, they frequently stop randomly working halfway,
        # so we need to save much more frequently. Inefficient, but effective
        with open(language.file, 'wb') as f:
            pickle.dump(vocabulary, f)


def pull_only_contents(language: Language, apikey: str) -> list:
    """
    Pulls raw content of API calls from top charts.

    :param language: the language for the songs
    :param apikey: the apikey for musixmatch
    :return: list of songs
    """

    # Attempts to open the file
    try:
        with open("databases/songdb.dat", 'rb') as f:
            songs = pickle.load(f)
    except FileNotFoundError:
        songs = set()

    # retrieves songs and saves them
    for song in pull_music(apikey, language, n_files=10000):
        if song is None:
            break
        songs.add(song)
        # In an ideal world this should be outside of the for-loop
        # Sadly, because we use free API keys, they frequently stop randomly working halfway,
        # so we need to save much more frequently. Inefficient, but effective
        with open("databases/songdb.dat", 'wb') as f:
            pickle.dump(songs, f)