# -*- coding: utf-8 -*-
from twpm import *
import re

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

if __name__ == "__main__":
    t = twpm()
    t.loadProjects()
    alist = []
    acommentlist = []
    allTasks = []
    f = open('tw_export_%s.csv' % datetime.datetime.now(), 'wb')
    f.write('ProjectID^CompanyName^Project^Creator^Description^Content^TaskID^' +              'DueDate^StartDate^EstimatedMinutes^' +                                    'Comments>>(First-Last-Date-Comment)')
    for p in t.projects:
        alist.append(project(p))
#    alist[0].loadTasklist()
    for aProject in alist:
        aProject.loadTasklist()
        for aTasklist in aProject.taskList:
            theTasks = json.loads(getUrl('http://clients.pint.com/todo_lists/%s/tasks.json' % aProject.taskList[aTasklist]['id']))
            for theTask in theTasks['todo-items']:
                allTasks.append(theTask)
            print allTasks
    for aTask in allTasks:
        if aTask['created-on'] >= '2014-04-01T00:00:00Z':
            f.write("""\n""")
            print aTask
            Task = task(aProject.projectID, aTask['id'])
            print Task.taskID
            Task.loadTask()
            print Task.attributes
            try:
                f.write(re.sub(r'\s+', ' ', aProject.projectID))
            except UnicodeError:
                f.write("^")
                pass
            for att in [Task.companyName, aTask['project-name'],                                  Task.creatorID, Task.description, Task.content,                            Task.taskID, Task.dueDate, Task.startDate,                                 Task.estimatedMinutes]:
                f.write("^")
                try:
                    string = re.sub(r'\s+', ' ', att)
                    for ch in ['\n', r'\r', '\f', '^M', '\r', '^J']:
                        string.replace(ch, ' ')
                    string.replace('^', 'CARAT')
                    f.write(string)
                except UnicodeError:
                    f.write("^")
                    pass
            Task.loadComments()
            for comment in Task.commentsDict:
                f.write("^")
                try:
                    f.write(Task.commentsDict[comment]['author-firstname'].replace('^', 'CARAT'))
                except UnicodeError:
                    f.write("^")
                    pass
                f.write("^")
                try:
                    f.write(Task.commentsDict[comment]['author-lastname'].replace('^', 'CARAT'))
                except UnicodeError:
                    f.write("^")
                    pass
                f.write("^")
                try:
                    f.write(Task.commentsDict[comment]['datetime'].replace('^', 'CARAT'))
                except UnicodeError:
                    f.write("^")
                    pass
                f.write("^")
                try:
                    string = re.sub(r'\s+', ' ', Task.commentsDict[comment]['body'])
                    for ch in ['\n', r'\r', '\f', '^M', '\r', '^J']:
                        string.replace(ch, ' ')
                    string.replace('^', 'CARAT')
                    f.write(string)
                except UnicodeError:
                    f.write("^")
                    pass
                print Task.commentsDict[comment]
            string = ""
    f.close()

