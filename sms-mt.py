import requests

shortcode = '2648'
access_token = 'A-2szoYus7mB13l5axDrr_1234AApSz8eu236GRNsoBQ'
address = '9771234567'
clientCorrelator = '268401'
message = 'Python SMS Test'

url = "https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/"+shortcode+"/requests"

querystring = {"access_token":access_token}

payload = "{\"outboundSMSMessageRequest\": { \"clientCorrelator\": \""+clientCorrelator+"\", \"senderAddress\": \""+shortcode+"\", \"outboundSMSTextMessage\": {\"message\": \""+message+"\"}, \"address\": \""+address+"\" } }"
headers = { 'Content-Type': "application/json", 'Host': "devapi.globelabs.com.ph" }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)