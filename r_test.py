from __future__ import print_function
from requests import request
#using "https://httpbin.org/redirect/n" to follow redirections through 
#test r = requests.get(url, allow_redirects=False)
#r.headers['Location'] is the next url
n = 9
redir = 302
host = 'https://httpbin.org'
url = '{}/redirect/{}'.format(host,n)
r = request('GET',url, allow_redirects=False)
redir = r.status_code
while (redir == 302):
	print (r.status_code)
	url = '{}{}'.format(host,r.headers['Location'])
	r = request('GET',url, allow_redirects=False)
	redir = r.status_code
	
	

print ("end")