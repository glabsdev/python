import requests

app_id = 'B54z9Ug5512HHrTGRT5g6hq64pGUq6ap'
app_secret = 'f655413712345607a696cd40741993758c411af3bb5f6c230270ec26e8d54126'
rewards_token = 'AbCkxKYid_F_p-JSgTejow'
address = '9001234567'
promo = 'LOAD 1'

url = "https://devapi.globelabs.com.ph/rewards/v1/transactions/send"
payload = "{ \"outboundRewardRequest\" : { \"app_id\" : \""+app_id+"\", \"app_secret\" : \""+app_secret+"\", \"rewards_token\" : \""+rewards_token+"\", \"address\" : \""+address+"\", \"promo\" : \""+promo+"\" } }"
headers = {
    'Content-Type': "application/json",
    'Host': "devapi.globelabs.com.ph"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
