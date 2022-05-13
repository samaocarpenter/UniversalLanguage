This holds the databases for each language.
The .db files contain all of the information indexed for their language.

The "songdb.dat" file is a file for development purposes holding raw song data. 
Right now, it holds song data for Spanish.

The databases are extremely small. The working databases currently have roughly 80 songs, and most do not have their full lyrics. This is because Musixmatch does not currently allow free users many API calls and severely limits how many lyrics this tool can collect. As a result, further development will inevitably require a different API or a commercial key. This is one of the largest TODO factors for this project.