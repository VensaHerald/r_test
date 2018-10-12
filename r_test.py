from __future__ import print_function
from requests import request
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
# from googleapiclient.discovery import build
from open.globals import *
#using "https://httpbin.org/redirect/n" to follow redirections through 
#test r = requests.get(url, allow_redirects=False)
#r.headers['Location'] is the next url


# n = 9
# redir = 302
# host = 'https://httpbin.org'
# url = '{}/redirect/{}'.format(host,n)
# r = request('GET',url, allow_redirects=False)
# redir = r.status_code
# while (redir == 302):
	# print (r.status_code)
	# url = '{}{}'.format(host,r.headers['Location'])
	# r = request('GET',url, allow_redirects=False)
	# redir = r.status_code
# print ("end")


#make http request in form of
	#https://ediscovery.google.com/discovery/matters/{MATTER_ID}/exports/{EXPORT_ID}/files/{I}?hl=en_GB
	#where syntactical {} are relevant info and {I} is integer in the range (-1:5) 
	#will need to catch exceptions as files for {I} > 2 may not exist
	#these exceptions will return a 400 error
	#
	#
	#
	#
	#
	#
	#not sure what kind of requests these will fall under with regards to API  
	#will need to build in synchronous calling to prevent overloading of API requests
	#response of http request to be stored in relevant format in folder in mounted share



creds = service_account.Credentials.from_service_account_file(SERVICE_FILE)
scoped_credentials = creds.with_scopes(SCOPES)
delegated_creds = creds.with_subject(STD_USER)
authed_session = AuthorizedSession(creds)

google_host = "https://ediscovery.google.com/discovery/matters/"
matter_id = STD_MATTER
export_id = "exportly-9486871a-9013-4e89-91c0-52ec4223b4bf"
file_no = 0

url = "{}{}/exports/{}/files/{}?hl=en_GB".format(google_host,matter_id,export_id,file_no)
r = authed_session.request('GET',url,allow_redirects=False)
print (r.status_code)
heads = r.headers
print(heads['Location'])


print('-----------------------------------------')
url = heads['Location']
r = authed_session.request('GET',url,allow_redirects=False)
print (r.status_code)
heads = r.headers
for a in heads:
	print ('{} : {}'.format(a,heads[a]))


