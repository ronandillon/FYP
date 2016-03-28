from flask import Flask,request
app = Flask(__name__)
from flask import json
import sqlite3
from flask import g
import urllib
import requests
import json



@app.route('/search/<quote>/<uuid>')
def search(quote,uuid):

    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

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


    query =c.execute("SELECT * FROM show WHERE imdbID = '"+re['imdbID']+"'")
    returns =query.fetchall()


    #Check if the result is an episode
    if re['Type']=='episode':
        try:
            if returns == []:
                c.execute("INSERT INTO show VALUES (?,?,?,?,?,?,1)",(re["imdbID"],re["Title"],re["imdbRating"],re["Poster"],re["Year"],re["Type"]))
                c.execute("INSERT INTO Searched VALUES (?,?,1,datetime())",(uuid,re["imdbID"]))
            #If it is, increase the count
            else:
                c.execute("UPDATE show SET count = count + 1 WHERE imdbID = '"+re['imdbID']+"'")
                c.execute("UPDATE Show SET count = count + 1 WHERE imdbID = '"+re['seriesID']+"'")
                c.execute("INSERT INTO Searched VALUES (?,?,0,datetime())",(uuid,re["imdbID"]))
                c.execute("INSERT INTO Searched VALUES (?,?,1,datetime())",(uuid,re["seriesID"]))


            query =c.execute("SELECT * FROM Show WHERE imdbID = '"+re['seriesID']+"'")
            returns =query.fetchall()

            if returns == []:

                se = requests.get("http://www.omdbapi.com/?i="+re['seriesID']+"&tomatoes=true&plot=full").json()
                c.execute("INSERT INTO Show VALUES (?,?,?,?,?,?,1)",(se["imdbID"],se["Title"],se["imdbRating"],se["Poster"],se["Year"],se["Type"]))
                c.execute("INSERT INTO Searched VALUES (?,?,0,datetime())",(uuid,se["imdbID"]))


        except:
            print 'SQL Query Failed'




    else:
        try:
                #Check if searched for show is already in Database
                query =c.execute("SELECT * FROM Show WHERE imdbID = '"+re['imdbID']+"'")
                returns =query.fetchall()
                #If not put, it in
                #try:
                if returns == []:
                        c.execute("INSERT INTO Show VALUES (?,?,?,?,?,?,1)",(re["imdbID"],re["Title"],re["imdbRating"],re["Poster"],re["Year"],re["Type"]))
                        c.execute("INSERT INTO Searched VALUES (?,?,1,datetime())",(uuid,re["imdbID"]))
                #If it is, increase the count
                else:
                        c.execute("UPDATE Show SET count = count + 1 WHERE imdbID = '"+re['imdbID']+"'")
                        c.execute("INSERT INTO Searched VALUES (?,?,1,datetime())",(uuid,re["imdbID"]))

        except:
                print 'SQL Query Failed'

    conn.commit()
    conn.close()


    return json.dumps(re)

@app.route('/search2')
def search2():
    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

    query =c.execute("SELECT * FROM Searched")
    returns =query.fetchall()
    conn.close()
    return str(returns)

@app.route('/top20')
def top20():
    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type != 'episode'  ORDER BY count  DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/etop20')
def etop20():
    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type='episode' ORDER BY count DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/mtop20')
def mtop20():
    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type='movie' ORDER BY count DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/stop20')
def stop20():
    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type='series' ORDER BY count DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/history/<uuid>')
def history(uuid):
    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

    query =c.execute("SELECT Title,imdbRating,poster FROM show JOIN Searched ON show.imdbId = searched.imdbId WHERE direct=1 AND deviceId="+uuid)
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/ref/<imdbid>/<uuid>')
def ref(imdbid,uuid):
    conn = sqlite3.connect('/tmp/quotr.db')
    c = conn.cursor()

    #query = c.execute("select * FROM Show WHERE imdbId IN (select imdbId from Searched WHERE imdbID !='"+imdbid+"' AND deviceId IN (SELECT deviceId from Sea
    returns = query.fetchall()
    return json.dumps(returns)

if __name__ == '__main__':
    app.run()

