import requests

app_id = 'B54z9Ug5512HHrTGRT5g6hq64pGUq6ap'
app_secret = 'f655413712345607a696cd40741993758c411af3bb5f6c230270ec26e8d54126'
subscriber_number = '9771234567'
amount = '0.00'
duration = '0'

url = "https://devapi.globelabs.com.ph/payment/v1/smsoptin"

querystring = {"app_id":app_id,"app_secret":app_secret,"subscriber_number":subscriber_number,"duration":duration,"amount":amount}

payload = ""
headers = {
    'Host': "devapi.globelabs.com.ph",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)