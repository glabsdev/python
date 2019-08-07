import requests

url = "https://developer.globelabs.com.ph/oauth/access_token"

querystring = {"app_id":"<app_id>","app_secret":"<app_secret>","code":"<code>"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "d959da88-d4cb-4ac8-b5da-9ed7f1b830bf"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)