# UniversalLanguage
A project for HackDuke 2020!
This project takes in vocabulary words in a learned language, either from the user or from a Duolingo login.
Then, it uses a pre-indexed database to provide you with songs in the language that you're learning.
This project is currently being expanded by @samaocarpenter.

## Installation instructions

Make sure you have Python 3.9 or later installed. 
Then, install the tools for the Duolingo and Musixmatch APIs using this command:

```angular2html
pip install duolingo-api
pip install requests
```

NOTE: You only need to install requests if you plan on modifying the database.
Normal users need not install requests.

After your environment is set up, clone this repository.

A requirements.txt file will be provided relatively soon, as the dependencies are likely to expand as the project expands over time.

## Using the tool

In the terminal, navigate into the top-level directory, then run `python main.py`. 
Follow the instructions!

The GUI is no longer in development and has been deprecated: all files starting with GUI are experimental and should be used at one's own risk!
