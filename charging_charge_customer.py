import requests

access_token = 'A-2szoYus7mB13l5axDrr_1234AApSz8eu236GRNsoBQ'
amount = '0.00'
description = 'NodeJS Charging Description'
endUserId = '9771234567'
referenceCode = '26481000001'
transactionOperationStatus ='Charged'
duration = '0'

url = "https://devapi.globelabs.com.ph/payment/v1/transactions/amount"

querystring = {"access_token":access_token}

payload = "{ \"amount\": \""+amount+"\", \"description\": \""+description+"\", \"endUserId\": \""+endUserId+"\", \"referenceCode\": \""+referenceCode+"\", \"transactionOperationStatus\":\""+transactionOperationStatus+"\", \"duration\":\""+duration+"\" } "
headers = { 'Content-Type': "application/json", 'Host': "devapi.globelabs.com.ph" }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)