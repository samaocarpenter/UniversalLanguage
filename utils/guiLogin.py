import tkinter as tk
import duo
import duolingo
from tkinter import Button, Label, Entry

master = Tk()

entry: StringVar = "search for words"
query = Entry(master, width=20, textvariable=entry)
query.grid(column=0, row=0, columnspan=15)

search = Button(master, text="Search!", padx=25, pady=25, command=None) # command to search for words entered in query

# need some way to read a string of comma-separated words
# can use split method for space-seperated words

#Trying out a function to handle username and password

def duo_login(username: str, password: str, language: str):
    """Takes in user login info once submit button is pressed.
    Reveals next button if login was successful. Reveals a "try again" label
    if login was unsuccessful."""
    error_label = tk.Label(text="Login failed")
    next_button = Button(master, text="next") #TODO: command SongRecs to open.
    try:
        duo.get_vocab(language, username, password, -1)
        error_label.pack_forget()
        next_button.grid(row=4, column=0)

    except DuolingoException("Login failed"):
            error_label.grid(row=4, column=0)


# label prompting user to enter Duolingo username and password
name_label = tk.Label(text="Username")
name_entry = tk.Entry()
name_label.grid(row=0, column=0)
name_entry.grid(row=1, column=0)

pass_label = tk.Label(text="Password")
pass_entry = tk.Entry()
pass_label.grid(row=2, column=0)
pass_entry.grid(row=3, column=0)

lang_label = tk.Label(text="Language")
lang_entry = tk.Entry()
lang_label.grid(row=4, column=0)
lang_entry.grid(row=5, column=0)

username = name_entry.get
password = pass_entry.get
language = lang_entry.get

# button to submit login credentials. How to handle invalid login?
login_button = Button(master, text="Login", command=lambda: duo_login(username, password, language))



print(entry)
mainloop()
