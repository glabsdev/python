import requests
url = "https://devapi.globelabs.com.ph/rewards/v1/transactions/send"
payload = "{\n \"outboundRewardRequest\" : {\n \"app_id\" : \"<app_id>\",\n \"app_secret\" : \"<app_secret> \",\n \"rewards_token\" : \"<rewards_token> \",\n \"address\" : \"<address>\",\n \"promo\" : \"<promo>\"\n }\n}"
headers = {
    'Content-Type': "application/json",
    'Host': "devapi.globelabs.com.ph"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
