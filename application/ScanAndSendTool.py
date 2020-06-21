import sys
import scanningmodule
import importmodule

pdfFile = sys.argv[1]

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
        emailList = importmodule.getEmailByName(competitorCandidates[response-1])
        emailIndex = 1
        print('Jos näistä joku on oikein, valitse numerolla muutoin paina 0')
        for emailCandidate in emailList:
            print(str(emailIndex) + ' ' + emailCandidate)
        emailResponse = int(input())
        if(emailResponse>0):
            email = emailList[emailResponse-1]
else:
    print('Anna nimi tai nimen alkuosa ja paina enter')

print(email)





