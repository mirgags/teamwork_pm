import os
import urllib
import urllib2
import json
import datetime
import base64

### Class not yet created. Should create a class and put the http methods      beneath it.  Instantiate it with the correct URL and JSON from a parent    class: Action(or something) that is the wrapper for everything.
#class apiCall(object):
#    def __init__(self):
#        self.id_num = None
#        self.url = ""
#        self.data = None
#        self.api = None

### Methods to create for apiCall class
#    def createTasklist(self, data):
#    def createTask(self, data):
#    def editTask(self, data):
#    def closeTask(self)

### Retrieve API key from local file ./teamworkpm_api_key.txt
    def getApiKey():
        curPath = os.getcwd()
        f = open('%s/teamworkpm_api_key.txt' % curPath, 'rb')
        apikey = f.readline().strip()
        f.close()
        return apikey

### Create authorization handler for TeamworkPM
    def authUrl(theurl):
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, theurl, getApiKey(), 'x')
        
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        
        opener = urllib2.build_opener(authhandler)
        
        urllib2.install_opener(opener)
        return

### GET request to establish parameters
    def getUrl(theurl):
        
        authUrl(theurl)
        pagehandle = urllib2.urlopen(theurl)
        
        return pagehandle.read()

### POST request accepts the Teamwork-specific URL and a JSON object with      the necessary parameters for the action.
    def postUrl(theurl, thePost):
    
        req = urllib2.Request(theurl)
        auth = 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
        req.add_header('Authorization', auth)
        req.add_header('Content-Type', 'application/json')
    
        return urllib2.urlopen(req, json.dumps(thePost))

### PUT request accepts the Teamwork-specific URL and a JSON object with       the necessary parameters for the action.
    def putUrl(theurl):
        req = urllib2.Request(url)
        auth = 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
        req.add_header('Authorization', auth)
        req.add_header("Content-Type", "application/json")
        req.get_method = lambda: "PUT"
        return pagehandle = urllib2.urlopen(req, json.dumps(thePut))

### DELETE request accepts the Teamwork-specific URL.
    def deleteUrl(theurl):
        req = urllib2.Request(url)
        auth = 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
        req.add_header('Authorization', auth)
        req.add_header("Content-Type", "application/json")
        req.get_method = lambda: "DELETE"
        return pagehandle = urllib2.urlopen(req)

### This is test code that has been moved to the test file teamwork_test.py
#theurl = 'http://clients.pint.com/todo_items/2592624.json'
#
##getUrl(theurl)
#
#theurl = 'http://clients.pint.com/projects/86732/todo_lists.json'
#theTasklistDict = {'todo-list': {'name': '2nd test list',                                                   'private type': True,                                                      'pinned type': True,                                                       'tracked type': True,                                                      'description': 'another test of                                            api integration'}}
#
#
##theJson = json.dumps(theTasklistDict)
#
##print json.dumps(theTasklistDict)
#
#
#newList = dict(postUrl(theurl, theTasklistDict).info())
#print newList
#print newList['id']
