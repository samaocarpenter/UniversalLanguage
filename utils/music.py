from typing import Generator
from utils.objects import Song, Language


def pull_music(language: Language, n_files: int = 100) -> Generator[Song]:
    """
    Generator function yielding songs in the desired language.
    Should pull lyrics and data from Genius or some other database.

    :param language: language to pull music for
    :param n_files: number of songs to bre returned
    :return: generates song objects
    """
    raise NotImplementedError()
