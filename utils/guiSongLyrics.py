# Display lyrics based on selection from guiSongRecs.py
# MAYBE have a link to the song on spotify, if we can get that API going
# Back button returns to guiSongRecs.py window

from tkinter import *


def go_back() -> None:
    print("ur_mom")

lyrics_text = "aaaaiaiiaiaivshadvnsfdjhbvhdNckhjasbdvodinbiashvabf"
lyrics_text1 = "AAAAAAA"

master = Tk()
S = Scrollbar(master)
S.pack(side=RIGHT, fill=Y)

lyrics = Text(master, font=("Helvetica", "16"), spacing1=2, height=8, width=30)
lyrics.insert(END, lyrics_text)
lyrics.insert(END, "\n")  # our magic next line thingy
lyrics.insert(END, lyrics_text1)
lyrics.pack(side=LEFT, fill=Y)


# maybe figure out a way to bold the vocab words found in the search?

back_button = Button(master, text="Back", command=go_back)

mainloop()