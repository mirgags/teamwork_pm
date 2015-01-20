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

def getTasklists (headers, projectID):
    theUrl = 'http://clients.pint.com/projects/%s/todo_lists.json?status=all' % projectID
    print theUrl
    r = requests.get(theUrl, headers=headers)
    print r.status_code
    print r.headers
    return r.json()

def getTasklist (headers, tasklistId):
    theUrl = 'http://clients.pint.com/todo_lists/%s.json' % tasklistId
    print theUrl
    taskList = json.loads(getUrl(theUrl))
    return taskList

def getProjectTasks (headers, projectID, page=None, theTasks=None):
    if not theTasks:
        theTasks = []        
    theUrl = 'http://clients.pint.com/projects/%s/tasks.json?includeCompletedTasks=true' % projectID
    if page:
        theUrl += '&page=%s' % page
    print theUrl
    r = requests.get(theUrl, headers=headers)
    print r.status_code
    page = int(r.headers['x-page'])
    for header in r.headers:
        print header + ': ' + r.headers[header]
    for item in r.json()['todo-items']:
        theTasks.append(item)
    print len(theTasks)
    page += 1
    if page <= int(r.headers['x-pages']):
        return getProjectTasks(headers, projectID, page, theTasks)
    return theTasks


def changeTask (headers, taskId, payload):
    p = requests.put('http://clients.pint.com/tasks/%s.json' % \
        taskId, data=json.dumps(payload),\
        headers=headers)
    print 'change PUT resp: %s' % p.status_code

if __name__ == "__main__":
    auth = 'Basic '+base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
    print auth
    headers = {'Content-Type': 'application/json', \
               'Authorization': auth}
    theTasks = getProjectTasks(headers, 86732)
    counter = 0
    for theTask in theTasks:
        counter += 1
        if theTask['content'].find('PINT - Administrative Activity') < 0:
            print theTask['content']
            payload = {'todo-item': {'content': 'PINT - Administrative Activity: %s' % \
            theTask['content']}}
            print 'payload: %s' % payload 
            changeTask(headers, theTask['id'], payload)
    print 'total: ' + str(counter)
    '''
    taskLists = getTasklists (headers, 86732)
    for thing in taskLists['todo-lists']:
        for theTask in thing['todo-items']:
            if theTask['content'].find('PINT - Administrative Activity') < 0:
                print theTask['content']
                payload = {'todo-item': {'content': 'PINT - Administrative Activity: %s' % \
                theTask['content']}}
                print 'payload: %s' % payload 
                changeTask(headers, theTask['id'], payload)
    '''


#    taskList = json.loads(getUrl(\
#        'http://clients.pint.com/projects/85150/todo_lists.json'))

#    unPrivateTasks(headers, taskList)

#    privateFiles(auth, 85151)
