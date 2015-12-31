# -*- coding: utf-8 -*-
from twpm import *
import requests
import re

key = getApiKey()
baseUrl = "https://pint.teamwork.com/"
s = requests.Session()
r = s.get(baseUrl + "projects.json?status=ALL", auth=(key, 'x'))
#print r.headers
projects = r.json()
companyDict = {}
peopleList = []
count = 0
for project in projects['projects']:
    companyDict[project["company"]["id"]] = []

#print companyDict
for key in companyDict:
    count += 1
print 'count is: ' + str(count)

r = s.get(baseUrl + "people.json?pageSize=500", auth=(key, 'x'))
count = 1
print r.headers
people = r.json()
for person in people["people"]:
    peopleList.append(person)

while r.headers["x-page"] < r.headers["x-pages"]:
    count += 1
    for person in people["people"]:
        peopleList.append(person)
    page = str(int(r.headers["x-page"]) + 1)
    r = s.get(baseUrl + "people.json?page=" + page, auth=(key, "x"))
    print r.headers
print 'people get count is: ' + str(count)
#print peopleList

for person in peopleList:
    try:
        companyDict[person["company-id"]].append(person)
    except:
        pass
curPath = os.getcwd()
f = open('%s/teamwork_people_%s.csv' % (curPath, datetime.datetime.now()), 'wb')
f.write('CompanyID|CompanyName|ContactFirstname|ContactLastname|Emails\n')

for company in companyDict:
    for person in companyDict[company]:
        if person['company-id'] != '33116':
#        print person
            f.write('%s|%s|%s|%s|%s\n' % (person['company-id'],                                                      person['company-name'],                                                    person['first-name'],                                                      person['last-name'],                                                       person['email-address']))
f.close()

