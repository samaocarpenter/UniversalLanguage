from utils.objects import Language
import duolingo
from random import shuffle


def get_vocab(language: Language, username: str, password: str, n_words: int = 10) -> list[str]:
    """
    Retrieves user's current vocab words.
    Function header may be changed depending on what authentication info Duolingo needs.

    :param language: language to be fetched
    :param username: user's Duolingo username
    :param password: user's Duolingo password
    :param n_words: number of words to be returned (-1 will do all)
    :return: list of vocab words as strings
    """

    lingo = duolingo.Duolingo(username, password)
    my_set = lingo.get_reviewable_topics(language.code)
    my_set = list(my_set)
    if (n_words == -1):
        return my_set
    return shuffle(my_set)[:n_words]