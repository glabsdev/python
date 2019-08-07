import requests
url = "https://devapi.globelabs.com.ph/rewards/v1/transactions/status"
payload = " {\"rewardStatusRequest\" : {\"app_id\" : \"<app_id>\", \"app_secret\" : \"<app_secret> \", \"rewards_token\" : \"<rewards_token> \", \"transaction_id\" : \"<transaction_id>\"} }"
headers = {
    'Content-Type': "application/json"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
