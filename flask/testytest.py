from googlesearch import GoogleSearch
gs = GoogleSearch.top_results()
for url in gs.top_urls():
  print url
