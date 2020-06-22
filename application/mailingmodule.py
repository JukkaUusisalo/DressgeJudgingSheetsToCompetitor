from mailjet_rest import Client
import os
import base64
import configparser

def getBase64Content(pdfFile):
    with open(pdfFile, "rb") as pdf_file:
        base64Content = base64.b64encode(pdf_file.read())
    return base64Content.decode("utf-8")

def getApiKey():
    config = configparser.ConfigParser()
    config.read('conf/application.ini')   
    return config['mailjet']['api_key'] 
    
def getApiSecret():
    config = configparser.ConfigParser()
    config.read('conf/application.ini')   
    return config['mailjet']['api_secret']     

def sendMail(recipient,fullName,pdfFilePath):
    api_key = getApiKey()
    api_secret = getApiSecret()
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    fileName = fullName + "-arvostelu.pdf"
    base64Content = getBase64Content(pdfFilePath) 
    data = {
    'Messages': [
        {
        "From": {
            "Email": "luoteis.satakunnan.ratsastajat@gmail.com",
            "Name": "Luoteis-Satakunnan Ratsastajat Ry"
        },
        "To": [
            {
            "Email": recipient,
            "Name": fullName
            }
        ],
        "Subject": "Arvostelusi Lusarin kouluratsastuskisoista",
        "TextPart": "Hei, liitteenä arvostelusi kouluratsastuskisoista.",        
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