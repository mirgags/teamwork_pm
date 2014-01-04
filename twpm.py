import os
import urllib
import urllib2
import json
import datetime
import base64

#class apiCall(object):
#    def __init__(self):
#        self.id_num = None
#        self.url = ""
#        self.api = None
#
#    def createTasklist(self):


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
    
    return pagehandle.read()

def postUrl(theurl, thePost):

    req = urllib2.Request(theurl)
#    req.add_data(thePost)
    auth = 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
    req.add_header('Authorization', auth)
    req.add_header('Content-Type', 'application/json')

#    authUrl(theurl)
#    pagehandle = 
    return urllib2.urlopen(req, json.dumps(thePost))
#    return pagehandle.read()


theurl = 'http://clients.pint.com/todo_items/2592624.json'

#getUrl(theurl)

theurl = 'http://clients.pint.com/projects/86732/todo_lists.json'
theTasklistDict = {'todo-list': {'name': '2nd test list',                                                   'private type': True,                                                      'pinned type': True,                                                       'tracked type': True,                                                      'description': 'another test of                                            api integration'}}


#theJson = json.dumps(theTasklistDict)

#print json.dumps(theTasklistDict)


newList = dict(postUrl(theurl, theTasklistDict).info())
print newList
print newList['id']
