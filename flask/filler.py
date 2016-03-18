import sqlite3
import urllib
import requests
import json
import urllib2

conn = sqlite3.connect('testytest.db')
c = conn.cursor()

def search(quote,uuid):
    googlesearch = urllib.urlencode({'q': quote})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&%s' % googlesearch
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    hits = data['results']
    for h in hits:  
       if 'www.imdb.com/title/' in h['url']:
           spliturl = h['url'].split('/')
        
    re = requests.get("http://www.omdbapi.com/?i="+spliturl[4]+"&tomatoes=true&plot=full").json()
    #return re['Title']
    c = conn.cursor()
    
    #Check if searched for show is already in Database
    query =c.execute("SELECT * FROM Show WHERE imdbID = '"+re['imdbID']+"'")
    returns =query.fetchall()
    try:
        #If not put, it in
        if returns == []:
            c.execute("INSERT INTO Show VALUES (?,?,?,?,1)",(re["imdbID"],re["Title"],re["imdbRating"],re["Poster"]))
            c.execute("INSERT INTO Searched VALUES (?,?)",(uuid,re["imdbID"]))
        #If it is, increase the count 
        else:
            c.execute("UPDATE Show SET count = count + 1 WHERE imdbID = '"+re['imdbID']+"'")
            c.execute("INSERT INTO Searched VALUES (?,?)",(uuid,re["imdbID"]))

    except:
        #error
        print ''
    conn.commit()
    #conn.close()
    return str(re)

search("iddb Goodfellas",1234)


