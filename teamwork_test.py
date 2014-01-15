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

theDict = {                                                                              "name": "event_fire",                                                      "events": ["push", "issues"],                                              "active": True,                                                            "config": {"url": "http://requestb.in/10gqbm81", "content_type": "json"}                                                                  }

theurl = 'https://api.github.com/repos/mirgags/teamwork_pm/hooks'
auth = 'Basic' + base64.urlsafe_b64encode('user:password')
req = urllib2.Request(theurl)
req.add_header('Authorization', auth)
req.add_header("content_type", "application/json")
urllib2.urlopen(req, json.dumps(theDict))

