import sqlite3

conn = sqlite3.connect("testytest.db")

conn.execute('''CREATE TABLE Show
       (imdbId INT PRIMARY KEY     NOT NULL,
       Title           TEXT    NOT NULL,
       imdbRating            INT     NOT NULL,
       poster        TEXT,
       count         INT);''')


conn.execute('''CREATE TABLE Searched
       (
       deviceId INT PRIMARY KEY     NOT NULL,
       imdbId INT NOT NULL,
       FOREIGN KEY(imdbId) REFERENCES Show(imdbId));''')

conn.close()
