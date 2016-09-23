import urllib, urllib2, json


query1 = raw_input("What do you want to search for ? >> ")



query = urllib.quote_plus(query1)
base_url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='
url = base_url + '%22' + query + '%22'
request = urllib2.Request(url,None)
response = urllib2.urlopen(request)
result = json.load(response)
output = []

if ( len(result) and
    'responseData' in result and 
    'results' in result['responseData'] and      
    result['responseData']['results'] != []):
        firstMatch = result['responseData']['results'][0]
        output.append(firstMatch['title'])
        output.append(firstMatch['visibleUrl'])
        output.append(firstMatch['content'])

print output

