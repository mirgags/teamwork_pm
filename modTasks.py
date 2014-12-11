# -*- coding: utf-8 -*-
from twpm import *
import requests

def unPrivateTasks (headers, taskList):
    payload = {'todo-item': {'private':0}}
    for thing in taskList['todo-lists']:
        for theTask in thing['todo-items']:
            print theTask['private']
            if theTask['private'] > '0':
                url='http://clients.pint.com/tasks/%s.json' % theTask['id']
                r = requests.put(url, data=json.dumps(payload),\
                     headers=headers)
                print r.text 

def privateFiles (auth, projectID):
    payload = {'file': {'private':1}}
    r = json.loads(getUrl(\
    'http://clients.pint.com/projects/%s/files.json' % projectID))
    for theFile in r['project']['files']:
        print theFile['originalName']
        if theFile['private'] == '0':
            print 'should change to private'
            print 'http://clients.pint.com/files/%s.json' % theFile['id']
            p = requests.put('http://clients.pint.com/files/%s.json' % \
                theFile['id'], data=json.dumps(payload),\
                headers=headers)
            print p.text

if __name__ == "__main__":
    auth = 'Basic '+base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
    print auth
    headers = {'Content-Type': 'application/json', \
               'Authorization': auth}
#    taskList = json.loads(getUrl(\
#        'http://clients.pint.com/projects/85150/todo_lists.json'))
#    unPrivateTasks(headers, taskList)
    privateFiles(auth, 85151)
