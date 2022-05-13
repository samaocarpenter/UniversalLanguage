from utils.objects import Language
import duolingo
from random import shuffle
from nltk.stem.snowball import SnowballStemmer


def get_vocab(
    language: Language, username: str, password: str, n_words: int = -1
) -> list[str]:
    """
    Retrieves a random number of the user's current vocab words.
    Function header may be changed depending on what authentication info Duolingo needs.

    :param language: language to be fetched
    :param username: user's Duolingo username
    :param password: user's Duolingo password
    :param n_words: number of words to be returned (-1 will do all)
    :return: list of vocab words as strings
    """

    # logs into user's Duolingo account
    lingo = duolingo.Duolingo(username, password)
    my_set = lingo.get_known_words(language.code)

    stemmer = SnowballStemmer(language.name)

    new_set = []
    for word in my_set:
        new = stemmer.stem(word)
        new_set.add(new)

    # if all words are requested, they're returned as a list
    my_list = list(new_set)
    if n_words == -1:
        return my_list

    # otherwise, a random subset of the words are returned
    shuffle(my_list)
    return my_list[:n_words]
