from tkinter import *
import getpass
import duolingo
from tkinter import Button, Label, Entry

master = Tk()

# Welcome and description
welcome_label = LabelFrame(master, text="Welcome to the UniversalLanguage app!", padx=10, pady=10)
description_label = Label(welcome_label, text="""Learning a foreign language? This code will
    take your vocabulary, and generate a list of
    songs that will help you practice listening. We
    currently support English and Spanish song searching.""")

welcome_label.grid(row=0, column=0)
description_label.grid(row=1, column=0)

# globals
global lang_choice
global duo_choice
global duo_songs
global vocab_songs
global username_entry
global password_entry
lang_choice = BooleanVar()
duo_choice = BooleanVar()

# language select
lang_label = LabelFrame(master, text="Choose a language!", padx=10, pady=10)
span = Radiobutton(lang_label, text="Spanish", variable=lang_choice, value=True)
engl = Radiobutton(lang_label, text="English", variable=lang_choice, value=False)
lang_label.grid(row=2, column=0)
span.grid(row=3, column=0)
engl.grid(row=4, column=0)

# duo select
duo_label = LabelFrame(master, text="Connect to Duolingo?", padx=10, pady=10)
duo_yes = Radiobutton(duo_label, text="Yes!", variable= duo_choice, value=True)
duo_no = Radiobutton(duo_label, text="Nope!", variable= duo_choice, value=False)

duo_label.grid(row=5, column=0)
duo_yes.grid(row=6, column=0)
duo_no.grid(row=7, column=0)

# song count
songs_label = LabelFrame(master, text="How many songs would you like?", padx=10, pady=10)
song_entry = Entry(songs_label)
songs_label.grid(row=8, column=0)
song_entry.grid(row=9, column=0)

submit_btn = Button(master, text="Submit!", command=lambda:decider(duo_choice.get()))
submit_btn.grid(row=10, column=0)

def decider(value):
    if value == True:
        ask_login()
    elif value == False:
        type_vocab()

def ask_login():
    login_label = LabelFrame(master, text="Please enter your Duolingo Login")
    email_entry = Entry(login_label, text="Usernme")
    password_entry = Entry(login_label, text="password")
    login_label.grid(row=11, column=0)
    email_entry.grid(row=12, column=0)
    password_entry.grid(row=13, column=0)
    

    

def type_vocab():
    vocab_label = LabelFrame(master, text="Please enter your desired vocabulary")
    vocab_entry = Entry(vocab_label)
    vocab_label.grid(row=11, column=0)
    vocab_entry.grid(row=12, column=0)
   



master.mainloop()