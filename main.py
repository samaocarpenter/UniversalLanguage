from utils.duo import get_vocab
from utils.database import search
from utils import languages
import getpass


# This code controls the main logic.
# All it particularly does is accept inputs,
# then reroute those inputs to the correct functions.
# This runs in the command line: no GUI
def main():
    print(
        """
        ###          Welcome to the UniversalLanguage app!             ###
        Learning a foreign language? This code will take your vocabulary,
        and generate a list of songs that will help you practice listening.
        We currently support English and Spanish song searching. Enter 1
        for English, and enter 2 for Spanish.
        """
    )
    lang_choice = int(input(""))
    while lang_choice not in (1, 2):
        lang_choice = int(input("not recognized: try again? "))

    duo_choice = int(input("Would you like to link to your Duolingo account? Type 1 for yes, 2 for no. "))
    while duo_choice not in (1, 2):
        duo_choice = int(input("not recognized: try again? "))

    language = languages.English if lang_choice == 1 else languages.Spanish
    if duo_choice == 1:
        username = input("Enter your Duolingo username ")
        password = getpass.getpass("Enter your Duolingo password ")
        vocab = get_vocab(language, username, password)
    else:
        vocab = input("Enter your vocab words, separated by only a space. ").split(" ")
    n_songs = int(input("how many songs would you like? "))
    for name in search(vocab, "utils/" + language.file, n_songs):
        print(name)


if __name__ == '__main__':
    main()
