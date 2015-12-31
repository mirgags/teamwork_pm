# -*- coding: utf-8 -*-
from twpm import *
import re
import requests

counter = 0
companyList = []

projectDict = json.loads(getUrl("https://clients.pint.com/projects.json?status=ALL"))
peopleDict = json.loads(getUrl("https://clients.pint.com/people.json?pageSize=3000"))
for project in projectDict['projects']:
    #if project['name'].lower().find('maintenance') > 0:
    if not any(project['company']['id'] in s for s in companyList):
        companyList.append({'companyId': project['company']['id'],                                     'companyName': project['company']['name'],                                 'contacts': []                                                           })
#        print project['company']['id']
        counter += 1

counter = 0

for company in companyList:
    for person in peopleDict['people']:
        if person['company-id'] == company['companyId']:
            company['contacts'].append({person['email-address']:                                                  {'firstname': person['first-name'],                                         'lastname': person['last-name']}                                           })
            counter += 1

#for company in companyList:
#    print "*****"
#    print 'Id # is: ', company['companyId'], '\n'
#    print 'Name is: ', company['companyName'], '\n'
#    print 'Contacts are: ', company['contacts'], '\n'
#    print "*****"
#
#print "Count is: %s" % counter

f = open('teamwork_people_%s.csv' % datetime.datetime.now(), 'wb')
f.write('CompanyID|CompanyName|ContactFirstname|ContactLastname|Emails\n')
for company in companyList:
    name = ''
    email = ''
    counter = 0
    for contact in company['contacts']:
        counter += 1
    for contact in company['contacts']:
        for emailAddress in contact:
        #            if counter == 1:
        #                try:
        #                    name = name + contact[emailAddress]['firstname']+ ' ' +                                 contact[emailAddress]['lastname']
        #                    email = email + '%s' % emailAddress
        #                except KeyError:
        #                    pass
        #            elif counter >= 2:
        #                try:
        #                    name = name + contact[emailAddress]['firstname']+ ' ' +                                 contact[emailAddress]['lastname'] + ', '
        #                    email = email + '%s,' % emailAddress
        #                except KeyError:
        #                    pass
        #            counter -= 1
        #            print 'company is: ', company['companyName']
        #            print 'names are: ', name
        #            print 'emails are: ', email
        #            print 'counter is: ', counter
        #            f.write('%s|%s|%s|%s\n' % (company['companyId'],                                                      company['companyName'],                                                    name, email))
            f.write('%s|%s|%s|%s|%s\n' % (company['companyId'],                                                      company['companyName'],                                                    contact[emailAddress]['firstname'],                                       contact[emailAddress]['lastname'],                                         emailAddress))
f.close()

print company
