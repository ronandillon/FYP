#!/usr/bin/python
import json
import urllib

def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  
  print 'Top %d hits:' % len(hits)
  for h in hits:  
      if 'urbandictionary' not in h['url'] and 'wiki' not in h['url'] and 'youtube' not in h['url'] and 'reddit' not in h['url'] and 'imgur' not in h['url']:
          print ' ', h['url']
          if 'www.imdb.com/title/' in h['url']
              
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

showsome('nobody that speaks german could be evil')
