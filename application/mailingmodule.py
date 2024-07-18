from mailjet_rest import Client
import os
import base64
import configparser
from pathlib import Path


def confpath():
    return str(Path.home()) + "/dressage.ini"

def getBase64Content(pdfFile):
    with open(pdfFile, "rb") as pdf_file:
        base64Content = base64.b64encode(pdf_file.read())
    return base64Content.decode("utf-8")

def getApiKey():
    config = configparser.ConfigParser()
    config.read(confpath())   
    return config['mailjet']['api_key'] 
    
def getApiSecret():
    config = configparser.ConfigParser()
    config.read(confpath())
    return config['mailjet']['api_secret']     

def getSenderEmail():
    config = configparser.ConfigParser()
    config.read(confpath)
    defaultSenderName = config['mail_options']['sender_email']    

def getSenderName():
    config = configparser.ConfigParser()
    config.read(confpath)
    defaultSenderName = config['mail_options']['sender_name']       

def getSubject():
    config = configparser.ConfigParser()
    config.read(confpath)
    defaultSenderName = config['mail_options']['sender_name']
    defaultSubject = f"Arvostelusi {defaultSenderName} kouluratsastuskisoista"
    return config.get('mail_options','subject',fallback=defaultSubject)

def getBodyText():
    config = configparser.ConfigParser()
    config.read(confpath)
    defaultBodyText = "Hei, liitteenä arvostelusi kouluratsastuskisoista."
    return config.get('mail_options','subject',fallback=defaultBodyText)



def sendMail(recipient,fullName,pdfFilePath):
    api_key = getApiKey()
    api_secret = getApiSecret()
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    fileName = fullName + "-arvostelu.pdf"
    base64Content = getBase64Content(pdfFilePath) 
    senderEmail = getSenderEmail()
    senderName = getSenderName()
    subject = getSubject()
    bodyText = getBodyText()
    data = {
    'Messages': [
        {
        "From": {
            "Email": senderEmail,
            "Name": senderName
        },
        "To": [
            {
            "Email": recipient,
            "Name": fullName
            }
        ],
        "Subject": subject,
        "TextPart": bodyText,        
    	"Attachments": [
		    {
		        "ContentType": "application/pdf",
				"Filename": fileName,
				"Base64Content": base64Content
			}
        ]
		}
    ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())