
from flask import Flask,request
app = Flask(__name__)
from flask import json
import sqlite3
from flask import g
import urllib
import requests
import json
from flask.ext.mysql import MySQL
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ronnie2k10'
app.config['MYSQL_DATABASE_DB'] = 'myquotrdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/search/<quote>/<uuid>')
def search(quote,uuid):
    
    conn = mysql.connect()
    c = conn.cursor()

    googlesearch = urllib.urlencode({'q': quote})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&%s' % googlesearch
    url2= 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&start=9&%s' % googlesearch
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    hits = data['results']
    spliturl=[]
    for h in hits:  
       if 'imdb.com/title/' in h['url']:
           spliturl = h['url'].split('/')
       
    if spliturl==[]:
        search_response2 = urllib.urlopen(url2)
        search_results2 = search_response2.read()
        results2 = json.loads(search_results2)
        data2 = results2['responseData']
        hits2 = data2['results']
         
        for h in hits2:
           if 'imdb.com/title/' in h['url']:
                spliturl = h['url'].split('/')

    re = requests.get("http://www.omdbapi.com/?i="+spliturl[4]+"&tomatoes=true&plot=full").json()
    

    query =c.execute("SELECT * FROM show WHERE imdbID = '"+re['imdbID']+"'")
    returns =query.fetchall()


    #Check if the result is an episode
    if re['Type']=='episode':
#	try:

            if returns == []:
                c.execute("INSERT INTO show (imdbId,title,imdbRating,poster,year,type,actors,genre,count) VALUES(%s,%s,%s,%s,%s,%s,%s,1)",(re["imdbID"],re["Title"],re["imdbRating"],re["Poster"],re["Year"],re["Type"],re["Actors"],re["Genre"]))
                c.execute("INSERT INTO Searched (deviceId,imdbId,direct,entered_date)VALUES (%s,%s,1,datetime())",(uuid,re["imdbID"]))
            #If it is, increase the count
            else:
                c.execute("UPDATE show SET count = count + 1 WHERE imdbID = '"+re['imdbID']+"'")
                c.execute("UPDATE Show SET count = count + 1 WHERE imdbID = '"+re['seriesID']+"'")
               
                searchQuery =c.execute("SELECT * FROM Searched WHERE imdbId='"+re['imdbID']+"' AND deviceId='"+uuid+"'")
                searchReturns =searchQuery.fetchall()
                if searchReturns == []:
                        c.execute("INSERT INTO Searched (deviceId,imdbId,direct,entered_date) VALUES (%s,%s,1,datetime())",(uuid,re["imdbID"]))
                        c.execute("INSERT INTO Searched (deviceId,imdbId,direct,entered_date) VALUES (%s,%s,0,datetime())",(uuid,re["seriesID"]))
                else:
                        c.execute("UPDATE Searched SET entered_date=datetime() WHERE imdbID = '"+re['imdbID']+"'")
                        c.execute("UPDATE Searched SET entered_date=datetime() WHERE imdbID = '"+re['seriesID']+"'")

            query =c.execute("SELECT * FROM Show WHERE imdbId = '"+re['seriesID']+"'")
            returns =query.fetchall()
        
            if returns == []:

                se = requests.get("http://www.omdbapi.com/?i="+re['seriesID']+"&tomatoes=true&plot=full").json()
                c.execute("INSERT INTO Show (imdbId,title,imdbRating,poster,year,type,actors,genre,count) VALUES (%s,%s,%s,%s,%s,%s,%s,1)",(se["imdbID"],se["Title"],se["imdbRating"],se["Poster"],se["Year"],se["Type"],se["Actors"],se["Genre"]))
                c.execute("INSERT INTO Searched (deviceId,imdbId,direct,entered_date) VALUES (%s,%s,0,datetime())",(uuid,se["imdbID"]))


 #   	except:
  #          print 'SQL Query Failed'

        
        

    else:
#	try:
                #Check if searched for show is already in Database
                query =c.execute("SELECT * FROM Show WHERE imdbID = '"+re['imdbID']+"'")
                returns =query.fetchall()
                #If not put, it in
                #try:
                if returns == []:
                        c.execute("INSERT INTO show (imdbId,title,imdbRating,poster,year,type,actors,genre,count) VALUES(%s,%s,%s,%s,%s,%s,%s,1)",(re["imdbID"],re["Title"],re["imdbRating"],re["Poster"],re["Year"],re["Type"],re["Actors"],re["Genre"]))
                        c.execute("INSERT INTO Searched (deviceId,imdbId,direct,entered_date)VALUES (%s,%s,1,datetime())",(uuid,re["imdbID"]))
                #If it is, increase the count 
                else:
                        c.execute("UPDATE Show SET count = count + 1 WHERE imdbId = '"+re['imdbID']+"'")

                        searchQuery =c.execute("SELECT * FROM Searched WHERE imdbId='"+re['imdbID']+"' AND deviceId='"+uuid+"'" )
                        searchReturns =searchQuery.fetchall()
                        if searchReturns == []:
                                c.execute("INSERT INTO Searched (deviceId,imdbId,direct,entered_date) VALUES (%,%,1,datetime())",(uuid,re["imdbID"]))
                        else:
                                c.execute("UPDATE Searched SET entered_date=datetime()  WHERE imdbId = '"+re['imdbID']+"'")

                        

 #   	except:
  #      	print 'SQL Query Failed'

    conn.commit()
    conn.close()


    return json.dumps(re)

@app.route('/search2')
def search2():
    conn = mysql.connect()
    c = conn.cursor()

    query =c.execute("SELECT * FROM Searched")
    returns =query.fetchall()
    conn.close()
    return str(returns)

@app.route('/top20')
def top20():
    conn = mysql.connect()
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type != 'episode'  ORDER BY count  DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/etop20')
def etop20():
    conn = mysql.connect()
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type='episode' ORDER BY count DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/mtop20')
def mtop20():
    conn = mysql.connect()
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type='movie' ORDER BY count DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/stop20')
def stop20():
    conn = mysql.connect()
    c = conn.cursor()

    query =c.execute("SELECT * FROM Show WHERE type='series' ORDER BY count DESC LIMIT 20")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)


@app.route('/history/<uuid>')
def history(uuid):
    conn = mysql.connect()
    c = conn.cursor()

    query =c.execute("SELECT Title,imdbRating,poster,year,actors,show.imdbId FROM show JOIN Searched ON show.imdbId = searched.imdbId WHERE direct=1 AND deviceId="+uuid+" ORDER BY entered_date DESC")
    returns =query.fetchall()
    conn.close()
    return json.dumps(returns)

@app.route('/ref/<imdbid>/<uuid>')
def ref(imdbid,uuid):
    conn = mysql.connect()
    c = conn.cursor()
    genre= c.execute("select genre from Show WHERE show.imdbId='"+imdbid+"'")
    mainGenre=genre.split(',')
    query = c.execute("select * FROM Show WHERE type !='episode' AND genre ='"+mainGenre[0]+"' AND imdbId IN (select imdbId from Searched WHERE imdbID !='"+imdbid+"' AND deviceId IN (SELECT deviceId from Searched WHERE imdbID ='"+imdbid+"' AND deviceId !='"+uuid+"')  GROUP BY imdbId ORDER BY count(imdbId))LIMIT 3;")
    returns = query.fetchall()
    return json.dumps(returns)

if __name__ == '__main__':
    app.run()


#SELECT * FROM Show WHERE imdbID IN (select imdbId, count(*) as SearchAmount from Searched WHERE imdbID !='"+imdbid+"' AND deviceId IN 
#(SELECT deviceId from Searched WHERE imdbID ='"+imdbid+"' AND deviceId !='"+uuid+"') GROUP BY imdbid ORDER BY SearchAmount DESC LIMIT 3);")

