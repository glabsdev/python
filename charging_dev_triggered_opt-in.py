import requests

url = "https://devapi.globelabs.com.ph/payment/v1/smsoptin"

querystring = {"app_id":"<app_id>","app_secret":"<app_secret>","subscriber_number":"<subscriber_number>","duration":"<duration>","amount":"<amount>"}

payload = ""
headers = {
    'Host': "devapi.globelabs.com.ph",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)