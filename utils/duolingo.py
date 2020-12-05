from utils.objects import Language


def get_vocab(language: Language, username: str, password: str, n_words: int = 10) -> list[str]:
    """
    Retrieves user's current vocab words.
    Function header may be changed depending on what authentication info Duolingo needs.

    :param language: language to be fetched
    :param username: user's Duolingo username
    :param password: user's Duolingo password
    :param n_words: number of words to be returned
    :return: list of vocab words as strings
    """
    raise NotImplementedError()

#Non-UI implementation
user_id = input("enter user id")
password = input("enter password")
lang = input("enter language")

lingo = duolingo.Duolingo(user_id, password)
abbrev = lingo.get_abbreviation_of(lang)
myset = lingo.get_known_words(abbrev)

mylist = list(myset)
