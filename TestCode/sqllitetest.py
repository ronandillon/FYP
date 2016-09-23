import sqlite3

conn = sqlite3.connect("testytest.db")

conn.execute('DROP TABLE IF EXISTS Show;')
conn.execute('''CREATE TABLE Show
       (imdbId INT PRIMARY KEY     NOT NULL,
       Title           TEXT    NOT NULL,
       imdbRating            INT     NOT NULL,
       poster        TEXT,
       count         INT);''')

conn.execute('DROP TABLE IF EXISTS Searched;')
conn.execute('''CREATE TABLE Searched
       (
       deviceId INT NOT NULL,
       imdbId INT NOT NULL,
       PRIMARY KEY (deviceId, imdbId),
       FOREIGN KEY(imdbId) REFERENCES Show(imdbId));''')

conn.close()
