import requests
import json
import urllib2


title="Game+Of+Thrones"

re = requests.get("http://www.omdbapi.com/?t="+title+"&tomatoes=true&plot=full").json()
print re

print
print

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
