# -*- coding: utf-8 -*-
from twpm import *
import re
import requests


if __name__ == '__main__':
    counter = 0
    companyList = []
    report = 'people' # or 'company'
    
    
    projectDict = json.loads(getUrl("https://clients.pint.com/projects.json?status=ALL"))
    peopleDict = json.loads(getUrl("https://clients.pint.com/people.json?pageSize=3000"))
    for project in projectDict['projects']:
        #if project['name'].lower().find('maintenance') > 0:
        if not any(project['company']['id'] in s for s in companyList):
            companyList.append({'companyId': project['company']['id'],                                     'companyName': project['company']['name'],                                 'clientType': project['category']['name'],                                 'contacts': []                                                           })
            counter += 1
    counter = 0
    
    companyDict = {}
    for company in companyList:
        if not any(company['companyId'] in s for s in companyDict):
            companyDict[company['companyId']] = company
            companyDict[company['companyId']]['clientType'] = []
        companyDict[company['companyId']]['clientType'].append(company['clientType'])
    
    for company in companyDict:
        for person in peopleDict['people']:
            if person['company-id'] == company:
                companyDict[company]['contacts'].append({                                                    'emailAddress': person['email-address'],                                   'firstname': person['first-name'],                                         'lastname': person['last-name']                                           })
                counter += 1
    
    f = open('teamwork_people_%s.csv' % datetime.datetime.now(), 'wb')
    f.write('CompanyID|CompanyName|ContactFirstname|ContactLastname|Emails|ClientType\n')
    for company in companyDict:
        name = ''
        email = ''
        counter = 0
        for contact in companyDict[company]['contacts']:
            counter += 1
        for contact in companyDict[company]['contacts']:
            #for emailAddress in contact:
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
            ##################################################################
            if report == 'people':
                f.write('%s|%s|%s|%s|%s|%s\n' % (company,                                       companyDict[company]['companyName'],                                       contact['firstname'],                                                      contact['lastname'],                                                       contact['emailAddress'],                                                   companyDict[company]['clientType']))
    
    if report == 'company':
        for company in companyDict:
            f.write('%s|%s|%s\n' % (company,                                       companyDict[company]['companyName'],                                       companyDict[company]['clientType']))
    
    f.close()
