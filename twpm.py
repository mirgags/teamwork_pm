import os
import urllib
import urllib2
import json
import datetime
import base64

#class TWPM(self):
#    def __init__(self):
#        self.account =

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

    req = urllib2.Request(theurl)
#    req.add_data(thePost)
    auth = 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
    req.add_header('Authorization', auth)
    req.add_header('Content-Type', 'application/json')

#    authUrl(theurl)
    pagehandle = urllib2.urlopen(req, json.dumps(thePost))

theurl = 'http://clients.pint.com/todo_items/2592624.json'

getUrl(theurl)

theurl = 'http://clients.pint.com/projects/86732/todo_lists.json'
theTasklistDict = {'todo-list': {'name': 'test list',                                                       'private type': True,                                                      'pinned type': True,                                                       'tracked type': True,                                                      'description': 'this is test of                                            api integration'}}


#theJson = json.JSONEncoder().encode(theTasklistDict)

print json.dumps(theTasklistDict)


postUrl(theurl, theTasklistDict)    
