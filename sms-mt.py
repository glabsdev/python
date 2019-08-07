import requests

url = "https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/<shortcode>/requests"

querystring = {"access_token":"<access_token>"}

payload = "{\"outboundSMSMessageRequest\": {\r\n   \"clientCorrelator\": \"<clientCorrelator>\",\r\n   \"senderAddress\": \"<shortcode>\",\r\n   \"outboundSMSTextMessage\": {\"message\": \"Hello World\"},\r\n   \"address\": \"<address>\"\r\n }\r\n}"
headers = {
    'Content-Type': "application/json",
    'Accept': "*/*",
    'Host': "devapi.globelabs.com.ph"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)