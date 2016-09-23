import requests
import json
import urllib2
import sqlite3

conn = sqlite3.connect('testytest.db')

title="The Simpsons"
uuid="22"

#API CALL
re = requests.get("http://www.omdbapi.com/?t="+title+"&tomatoes=true&plot=full")

print jsonify(re)
print re["imdbID"]
print re["Title"]
print re["Plot"]
print re["Rated"]
print re["Released"]
print re["tomatoMeter"]
print re["Director"]
print re["Writer"]
print re["Production"]
print re["Actors"]
print re["Type"]
print re["tomatoConsensus"]
print re["Poster"]
print re["Awards"]
print re["Genre"]
print re["imdbRating"]
print re["Runtime"]

c = conn.cursor()

#Check if searched for show is already in Database
query =c.execute("SELECT * FROM Show WHERE imdbID = '"+re['imdbID']+"'")
returns =query.fetchall()
#If not put, it in
if returns == []:
    c.execute("INSERT INTO Show VALUES (?,?,?,?,1)",(re["imdbID"],re["Title"],re["imdbRating"],re["Poster"]))
    c.execute("INSERT INTO Searched VALUES (?,?)",(uuid,re["imdbID"]))
#If it is, increase the count 
else:
    c.execute("UPDATE Show SET count = count + 1 WHERE imdbID = '"+re['imdbID']+"'")
    c.execute("INSERT INTO Searched VALUES (?,?)",(uuid,re["imdbID"]))

conn.commit()
conn.close()
