from tkinter import *

master = Tk()

entry: StringVar = "search for words"
query = Entry(master, width=20, textvariable=entry)
query.grid(column=0, row=0, columnspan=15)

search = Button(master, text="Search!", padx=25, pady=25, command=None) # command to search for words entered in query

# need some way to read a string of comma-separated words

# label prompting user to enter Duolingo username and password
# button to submit login credentials



print(entry)
mainloop()
