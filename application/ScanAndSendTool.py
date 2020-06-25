import sys
import scanningmodule
import importmodule
import mailingmodule

def getEmailFromList(name):
    emailList = importmodule.getEmailByName(name)
    emailIndex = 1
    print('Jos näistä joku on oikein, valitse numerolla muutoin paina 0')
    for emailCandidate in emailList:
        print(str(emailIndex) + ' ' + emailCandidate)
    emailResponse = int(input())
    if(emailResponse>0):
        return emailList[emailResponse-1]    

def getEmailUsingCompetitorNameList():
   print('Anna nimi tai nimen alkuosa ja paina enter')
   nameCriteria = input()
   nameIndex = 1
   nameList = importmodule.getCompetitorListByName(nameCriteria)
   print('Jos näistä joku on oikein, valitse numerolla muutoin paina 0')
   for nameCandidate in nameList:
       print(str(nameIndex) + ' ' + nameCandidate)
       nameIndex += 1
   nameResponse = int(input())
   if(nameResponse>0):
       name = nameList[nameResponse-1]
       email = getEmailFromList(name)
       return email

pdfFile = sys.argv[1]
# pdfFile = "data/pdf/esimerkki_arvostelu.pdf"

email = ''
index = 1
competitorCandidates  = scanningmodule.parseCompetitor(pdfFile)

if(len(competitorCandidates)>0):
    print('Jos näistä joku on oikein, valitse numerolla muutoin paina 0')
    for competitorName in competitorCandidates:
        print(str(index) + ' ' + competitorName)
        index += 1
    response = int(input())
    if(response>0):
        email = getEmailFromList(competitorCandidates[response-1])
    else:
        email = getEmailUsingCompetitorNameList()
else:
    email = getEmailUsingCompetitorNameList()

if(email):        
    print(email)
    mailingmodule.sendMail(email,email,pdfFile)
else: 
    print("Ei löydy, selvitä manuaalisesti")

print("Paina Enter lopettaaksesi")
end = input()







