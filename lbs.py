import requests

access_token = 'A-2szoYus7mB13l5axDrr_1234AApSz8eu236GRNsoBQ'
address = '9771234567'
requestedAccuracy = '100'

url = "https://devapi.globelabs.com.ph/location/v1/queries/location"
querystring = {"access_token":access_token,"address":address,"requestedAccuracy":requestedAccuracy}
headers = {
    'Content-Type': "application/json",
    'Host': "devapi.globelabs.com.ph"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
