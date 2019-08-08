import requests

app_id = 'B54z9Ug5512HHrTGRT5g6hq64pGUq6ap'
app_secret = 'f655413712345607a696cd40741993758c411af3bb5f6c230270ec26e8d54126'
rewards_token = 'AbCkxKYid_F_p-JSgTejow'
transaction_id = '1234567'

url = "https://devapi.globelabs.com.ph/rewards/v1/transactions/status"
payload = "{\"rewardStatusRequest\" : {\"app_id\" : \""+app_id+"\", \"app_secret\" : \""+app_secret+"\", \"rewards_token\" : \""+rewards_token+"\", \"transaction_id\" : \""+transaction_id+"\" } }"
headers = { 'Content-Type': "application/json" }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
