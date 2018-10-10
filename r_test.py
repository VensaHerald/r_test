from __future__ import print_function
import requests
#using "https://httpbin.org/redirect/n" to follow redirections through 
#test r = requests.get(url, allow_redirects=False)
#r.headers['Location'] is the next url
n = 3
url = 'https://httpbin.org/redirect/{}'.format(n)
r = requests.request('GET',url, allow_redirects=False)
print (r.status_code, r.headers['location'])

