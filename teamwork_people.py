# -*- coding: utf-8 -*-
from twpm import *
import re

counter = 0
companyList = []

projectDict = json.loads(getUrl("https://clients.pint.com/projects.json?status=ALL"))
peopleDict = json.loads(getUrl("https://clients.pint.com/people.json?pageSize=300"))
for project in projectDict['projects']:
    if project['name'].lower().find('maintenance') > 0:
        if not any(project['company']['id'] in s for s in companyList):
            companyList.append({'companyId': project['company']['id'],                                     'companyName': project['company']['name'],                                 'contacts': []                                                           })
            print project['company']['id']
            counter += 1

counter = 0

for company in companyList:
    for person in peopleDict['people']:
        if person['company-id'] == company['companyId']:
            company['contacts'].append({person['email-address']:                                                  {'firstname': person['first-name'],                                         'lastname': person['last-name']}                                           })
            counter += 1

for company in companyList:
    print "*****"
    print 'Id # is: ', company['companyId'], '\n'
    print 'Name is: ', company['companyName'], '\n'
    print 'Contacts are: ', company['contacts'], '\n'
    print "*****"

print "Count is: %s" % counter
