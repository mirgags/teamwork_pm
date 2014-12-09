# -*- coding: utf-8 -*-
from twpm import *
import re


if __name__ == "__main__":
    t = twpm()
    t.loadProjects()
    alist = []
    acommentlist = []
    allTasks = []
    placeHolder = {}
    f = open('tw_export_%s.csv' % datetime.datetime.now(), 'wb')
    f.write('ProjectID^CompanyName^Project^Creator^Description^Content^Task    ID^' +              'DueDate^StartDate^EstimatedMinutes^' +                                        'Comments>>(First-Last-Date-Comment)')
    for i in range(1, 30):
        try:
            placeHolder = json.loads(getUrl('http://clients.pint.com/tasks.json?startdate=20140401&enddate=20140714&page=%s&pageSize=250&includeCompletedTasks=true' % i))
            print len(allTasks)
            for item in placeHolder['todo-items']:
#                print item
                allTasks.append(item)
        except:
            pass
        placeHolder = {}
    for aTask in allTasks:
        if aTask['created-on'] >= '2014-04-01T00:00:00Z':
            f.write("""\n""")
            print aTask
            Task = task(aTask['project-id'], aTask['id'])
            print Task.taskID
            Task.loadTask()
            print Task.attributes
            try:
                f.write(re.sub(r'\s+', ' ', str(aTask['project-id'])))
            except UnicodeError:
                f.write("^")
                pass
            for att in [Task.companyName, aTask['project-name'],                                  Task.creatorID, Task.description, Task.content,                            Task.taskID, Task.dueDate, Task.startDate,                                 Task.estimatedMinutes]:
                f.write("^")
                try:
                    print att
                    string = re.sub(r'\s+', ' ', str(att))
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

