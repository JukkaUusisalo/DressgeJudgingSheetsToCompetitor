import PyPDF2
import importmodule



def parseCompetitor(pdfFile):
    candidates = []
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = pdfReader.getPage(0).extractText()
    competitorNames = importmodule.getCompetitorNames()
    for fullName in competitorNames:
        nameArray = fullName.split(' ')
        firstName = nameArray[0]
        lastName = nameArray[(len(nameArray)-1)]
        if(fullName in text): 
            candidates.append(fullName)
        if(lastName in text and not fullName in candidates):
            candidates.append(fullName)
        if(firstName in text and not fullName in candidates):
            candidates.append(fullName)
    return candidates
