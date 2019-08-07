import requests

url = "https://devapi.globelabs.com.ph/payment/v1/transactions/amount"

querystring = {"access_token":"<access_token>","amount":"<amount>","description":"AppTest","endUserId":"<endUserId>","referenceCode":"<referenceCode>","transactionOperationStatus":"Charged","duration":"<duration>"}

headers = {'cache-control': "no-cache" }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)