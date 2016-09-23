import json
import urllib2
import sqlite3

conn = sqlite3.connect('testytest.db')
c = conn.cursor()
query =c.execute("SELECT * FROM Searched")


#c.execute("INSERT INTO Searched VALUES (1,'help')")
conn.commit()

#c.execute("INSERT INTO Searched VALUES (22,"+title+") SELECT 22,"+title+" WHERE NOT EXISTS (SELECT 1 FROM Searched WHERE deviceId = 22 AND imdbId="+title+");")
returns =query.fetchall()

print returns
conn.close()
