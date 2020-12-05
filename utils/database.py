from objects import Song, Language


def search(vocab: list[str], language: Language, n_songs: int = 3) -> list[Song]:
    """
    :param vocab: list of vocabulary words to be searched for
    :param language: language to be used
    :param n_songs: number of songs to return
    :return: list of n_songs songs, each represented as a tuple containing:
        (song name, artist name)
    """

    raise NotImplementedError()


def add_files(language: Language, n_files: int = 100) -> None:
    """
    Adds a set amount of songs to a database.

    :param language: the language for the songs
    :param n_files: number of songs to be added
    :return:
    """

    raise NotImplementedError()
