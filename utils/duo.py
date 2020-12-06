from utils.objects import Language
import duolingo
from random import shuffle


def get_vocab(language: Language, username: str, password: str, n_words: int = 10) -> list[str]:
    """
    Retrieves a random number of the user's current vocab words.
    Function header may be changed depending on what authentication info Duolingo needs.

    :param language: language to be fetched
    :param username: user's Duolingo username
    :param password: user's Duolingo password
    :param n_words: number of words to be returned (-1 will do all)
    :return: list of vocab words as strings
    """

    lingo = duolingo.Duolingo(username, password)
    my_set = lingo.get_known_words(language.code)
    my_list = list(my_set)
    if n_words == -1:
        return my_list
    shuffle(my_list)
    return my_list[:n_words]
