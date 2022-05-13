# TODO: Access login info from guiLogin.py
# Access vocab list from duo.py
# Display list of songs and known vocab
# Allow button press to select a song, then go to new window with lyrics
# Have a logout button

from utils.duo import get_vocab
from utils.deprecated.guiLogin import language, username, password

vocab = get_vocab(language, username, password)
print(vocab)

