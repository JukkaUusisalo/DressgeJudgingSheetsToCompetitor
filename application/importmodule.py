import csv
import re
from tinydb import TinyDB, Query

class Competitor:
    def __init__(self,name, email, licenseNo):
        self.licenseNo = licenseNo        
        self.name = name
        self.email = email


def readCvs(csvFile): 
    with open(csvFile, mode='r') as csv_file:
        db = TinyDB('data/db.json')
        competitorDict = {}
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            line_count += 1            
            licenseNr=row['Athlete licence nr']
            name=row['Athlete name']
            email=row['Athlete e-mail']
            c = Competitor(name,email,licenseNr)
            competitorDict[licenseNr] = c              
        for c in competitorDict:
            db.insert(vars(competitorDict[c]))
        return competitorDict

def getCompetitorNames():
    names = []
    db = TinyDB('data/db.json')
    competitors = db.all()
    for competitor in competitors:
        names.append(competitor['name'])
    return names

def getEmailByName(name):
    emailList = []
    db = TinyDB('data/db.json')
    query = Query()
    result = db.search(query.name == name)
    for doc in result:
        emailList.append(doc['email'])
    return emailList

def getCompetitorListByName(nameCriteria):
    nameList = []
    db = TinyDB('data/db.json')
    query = Query()
    test_contains = lambda value, search: search in value
    result = db.search(query.name.test(test_contains, nameCriteria))
    for doc in result:
        nameList.append(doc['name'])
    return nameList

                  
       