DROP TABLE IF EXISTS Show;
CREATE TABLE Show
       (imdbId TEXT PRIMARY KEY     NOT NULL,
       Title           TEXT    NOT NULL,
       imdbRating            FLOAT   ,
       poster        TEXT,
       year	INT,
       type     TEXT,
       actors	TEXT,
       count         INT,
	 FOREIGN KEY(imdbId) REFERENCES Searched(imdbId));


DROP TABLE IF EXISTS Searched;
CREATE TABLE Searched
       (
       deviceId TEXT NOT NULL,
       imdbId TEXT NOT NULL,
       direct INT NOT NULL,
       entered_date DATETIME DEFAULT CURRENT_TIMESTAMP,
       PRIMARY KEY(deviceId,imdbId));
