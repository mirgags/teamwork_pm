# -*- coding: utf-8 -*-
from twpm import *
import requests

if __name__ == "__main__":
    auth = 'Basic '+base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
    print auth
    payload = {'todo-item': {'private':0}}
    headers = {'Content-Type': 'application/json', \
               'Authorization': auth}
    taskList = json.loads(getUrl(\
        'http://clients.pint.com/projects/85150/todo_lists.json'))
    for thing in taskList['todo-lists']:
        for theTask in thing['todo-items']:
            print theTask['private']
            if theTask['private'] > '0':
                url='http://clients.pint.com/tasks/%s.json' % theTask['id']
                r = requests.put(url, data=json.dumps(payload),\
                     headers=headers)
                print r.text 
