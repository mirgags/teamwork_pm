from twpm import *

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

#theDict = {                                                                              "name": "event_fire",                                                      "events": ["push", "issues"],                                              "active": True,                                                            "config": {"url": "http://requestb.in/1deky0u", "content_type": "json"}                                                                  }
#
#theurl = 'https://api.github.com/repos/mirgags/teamwork_pm/hooks'
#auth = 'Basic' + base64.urlsafe_b64encode('user:password')
#req = urllib2.Request(theurl)
#req.add_header('Authorization', auth)
#req.add_header("content_type", "application/json")
#try:
#    handle = urllib2.urlopen(req, json.dumps(theDict))
#except IOError, e:
#    if hasattr(e, 'code'):
#        if e.code != 401:
#            print 'we got annother error'
#            print e.code
#        else:
#            for keys in e.headers:
#                print keys, ": ", e.headers[keys]

class twpm(object):
    def __init__(self):
        self.name = "TWPM Instance"
        self.projects = {}
#        self.loadProjects()

    def loadProjects(self):
        aList = json.loads(getUrl('http://clients.pint.com/projects.json'))
        for project in aList['projects']:
            self.projects[project['id']] = {'company': project['company']['name'],                                                                                                                'name': project['name']}

class project(twpm):
    def __init__(self, idNum):
        twpm.__init__(self)
#        self.loadProjects()
        self.projectName = self.projects[idNum]['name']
        self.projectID = idNum
        self.taskList = {}

    def loadTasklist(self):
        theJson = json.loads(getUrl('http://clients.pint.com/projects/%s/todo_lists.json' % self.projectID))
        if theJson:
            for tasklist in theJson['todo-lists']:
                self.taskList[tasklist['id']] = {'name': tasklist['name'],                                    'description': tasklist['description']                                    }
###
#    def getTasklist
#theProjectList = []
#theTaskListDict = {}
#
#class company(object):
#    def __init__(self, idNum):
#        name = ""
#        companyID = ""
#        url = getUrl('http://clients.pint.com/projects/%s/todo_lists.json' % idNum)
#    
#for project in theJson['projects']:
#    theProjectList.append([project['company']['name'],                                                project['name'],                                                           project['id']])
#for project in theProjectList:
#    theJson = json.loads(getUrl('http://clients.pint.com/projects/%s/todo_lists.json' % project[2]))
#    for tasklist in theJson['todo-lists']:
#        if tasklist:
            
    
#    for taskList in theJson['todo-lists']:
#        theTaskListDict[taskList['id']] = {'company': project[0],                                                     'project': project[1],                                                     'companyID': project[2]}
#
#for project in theTaskListDict:
#    print project, ": ", theTaskListDict[project], "\n"
