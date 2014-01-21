from twpm import *
import unicodedata

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
    f = open('tw_export.csv', 'wb')
    for p in t.projects:
        alist.append(project(p))
#    alist[0].loadTasklist()
    for aProject in alist:
       aProject.loadTasklist()
       for aTasklist in aProject.taskList:
            print aTasklist
            for aTask in aProject.taskList[aTasklist]['todo-items']:
#                print 'company: ', aTask['project-name'], '\n',                                  'task: ', aTask['content'], '\n',                                          'start date: ', aTask['start-date'], '\n',                                 'complete date: ', aTask['completed_on'], '\n',                            'created by: ', aTask['creator-firstname'], " ", aTask['creator-lastname'], '\n',                                                                     'description: ', aTask['description'].replace('\n', ' '), '\n',                                                                                      'assigned to: ', aTask['responsible-party-names'], '\n'
#                print aTask
                Task = task(aProject.projectID, aTask['id'])
#                print Task.taskID
                Task.loadTask()
#                print Task.attributes
                f.write("|")
                try:
                    f.write(aProject.projectID)
                except UnicodeError:
                    pass
                for att in [Task.creatorID, Task.description, Task.content,                            Task.taskID, Task.dueDate, Task.startDate,                                 Task.estimatedMinutes]:
                    f.write("|")
                    try:
                        string = att.strip()
                        for ch in ['\n', r'\r']:
                            string.replace(ch, ' ')
                        f.write(string)
                    except UnicodeError:
                        pass
                Task.loadComments()
                for comment in Task.commentsDict:
                    f.write("|")
                    try:
                        f.write(Task.commentsDict[comment]['author-firstname'])
                    except UnicodeError:
                        pass
                    f.write("|")
                    try:
                        f.write(Task.commentsDict[comment]['author-lastname'])
                    except UnicodeError:
                        pass
                    f.write("|")
                    try:
                        f.write(Task.commentsDict[comment]['datetime'])
                    except UnicodeError:
                        pass
                    f.write("|")
                    try:
                        string = Task.commentsDict[comment]['body'].strip()
                        for ch in ['\n', r'\r']:
                            string.replace(ch, ' ')
                        f.write(string)
                    except UnicodeError:
                        pass
#                    print Task.commentsDict[comment]
                f.write("\n")
            f.write(line)
    f.close()
#        print aTasklist, ": ", alist[0].taskList[aTasklist],"\n\n"
        
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
