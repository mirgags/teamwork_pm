import os
import urllib2
import json
import datetime



def getApiKey():
    curPath = os.getcwd()
    f = open('%s/teamworkpm_api_key.txt' % curPath, 'rb')
    apikey = f.readline().strip()
    f.close()
    return apikey

def authUrl(theurl):
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, theurl, getApiKey(), 'x')
    
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    
    opener = urllib2.build_opener(authhandler)
    
    urllib2.install_opener(opener)
    return

def getUrl(theurl):
    
    authUrl(theurl)
    pagehandle = urllib2.urlopen(theurl)
    
    print pagehandle.read()

def postUrl(theurl, thePost):

    authUrl(theurl)
    pagehandle = urllib2.urlopen(theurl, json.loads(thePost))

theurl = 'http://clients.pint.com/todo_items/2592624.json'

getUrl(theurl)

theurl = 'http://clients.pint.com/projects/86732/todo_lists.json'
theTasklistDict = {'name': 'test list', 'private type': True, 'pinned                         type': True, 'tracked type': True, 'description': 'this                    is test of api integration'}


theJson = json.JSONEncoder().encode(theTasklistDict)


postUrl(theurl, theJson)    
