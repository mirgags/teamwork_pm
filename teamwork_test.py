from twpm import *

theurl = 'http://clients.pint.com/todo_items/2592624.json'

#getUrl(theurl)

theurl = 'http://clients.pint.com/projects/86732/todo_lists.json'
theTasklistDict = {'todo-list': {'name': '2nd test list',                                                   'private type': True,                                                      'pinned type': True,                                                       'tracked type': True,                                                      'description': 'another test of                                            api integration'}}


#theJson = json.dumps(theTasklistDict)

#print json.dumps(theTasklistDict)


newList = dict(postUrl(theurl, theTasklistDict).info())
print newList
print newList['id']
