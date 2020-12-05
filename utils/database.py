from objects import Song, Language
from music import pull_music
import pickle
from collections import Counter


def search(
        vocab: list[str], language: Language, n_songs: int = 3,
) -> list[str]:
    """
    :param vocab: list of vocabulary words to be searched for
    :param language: language to be used
    :param n_songs: number of songs to return
    :return: list of n_songs songs, each represented as a string containing:
        (song name) by (artist name)
    """

    try:
        with open(language.file, 'rb') as f:
            words = pickle.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            'Language input does not have an existing associated database.\n' + repr(e)
        )

    counts = Counter()
    for word in vocab:
        for song in words[word]:
            counts[song] += 1

    ret = []
    for data, _ in counts.most_common(n_songs):
        ret.append(data)

    return ret


def add_files(language: Language, n_files: int = 100) -> None:
    """
    Adds a set amount of songs to a database.

    :param language: the language for the songs
    :param n_files: number of songs to be added
    :return:
    """
    try:
        with open(language.file, 'rb') as f:
            vocabulary = pickle.load(f)
    except FileNotFoundError:
        vocabulary = {}

    for song in pull_music(language, n_files=n_files):
        lyrics = song.lyrics.lower().split()
        name = str(song)
        for word in lyrics:
            word = ''.join([i for i in word if i.isalpha()])
            if word not in vocabulary:
                vocabulary[word] = set()
            vocabulary[word].add(name)

    with open(language.file, 'wb') as f:
        pickle.dump(vocabulary, f)
