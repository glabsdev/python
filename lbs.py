import requests
url = "https://devapi.globelabs.com.ph/location/v1/queries/location"
querystring = {"access_token":"<access_token>","address":"<address>","requestedAccuracy":"100"}
headers = {
    'Content-Type': "application/json",
    'Host': "devapi.globelabs.com.ph"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
