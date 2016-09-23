#!/usr/bin/python
import json
import urllib


searchfor="nobody who speaks german could be evil"
query = urllib.urlencode({'q': searchfor})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&%s' % query
search_response = urllib.urlopen(url)
search_results = search_response.read()
results = json.loads(search_results)
data = results['responseData']
hits = data['results']
for h in hits:
    if 'www.imdb.com/title/' in h['url']:
      spliturl = h['url'].split('/')
      print spliturl[4] 
              
