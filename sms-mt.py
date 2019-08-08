import requests

v_shortcode = '2648'
v_access_token = 'A-2szoYus7mB13l5axDrr_1234AApSz8eu236GRNsoBQ'
v_address = '9771234567'
v_clientCorrelator = '268401'
v_message = 'Python SMS Test'

url = "https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/"+v_shortcode+"/requests"

querystring = {"access_token":v_access_token}

payload = "{\"outboundSMSMessageRequest\": { \"clientCorrelator\": \""+v_clientCorrelator+"\", \"senderAddress\": \""+v_shortcode+"\", \"outboundSMSTextMessage\": {\"message\": \""+v_message+"\"}, \"address\": \""+v_address+"\" } }"
headers = { 'Content-Type': "application/json", 'Host': "devapi.globelabs.com.ph" }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)