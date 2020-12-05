import tkinter as tk
from tkinter import Button, Label, Entry

master = Tk()

entry: StringVar = "search for words"
query = Entry(master, width=20, textvariable=entry)
query.grid(column=0, row=0, columnspan=15)

search = Button(master, text="Search!", padx=25, pady=25, command=None) # command to search for words entered in query

# need some way to read a string of comma-separated words
# can use split method for space-seperated words

# label prompting user to enter Duolingo username and password
name_label = tk.Label(text="Username")
name_entry = tk.Entry()
name_lable.pack
name_entry.pack
pass_label = tk.Label(text="Password")
pass_entry = tk.Entry()
pass_label.pack
pass_entry.pack


# button to submit login credentials. How to handle invalid login?
submit = Button(master, text="Login")



print(entry)
#mainloop()
