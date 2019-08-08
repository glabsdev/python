import requests

app_id = 'B54z9Ug5512HHrTGRT5g6hq64pGUq6ap'
app_secret = 'f655413712345607a696cd40741993758c411af3bb5f6c230270ec26e8d54126'
code = 'osg68ErhoXxaACygn5yS7yAqRfB6E49S7qE75Id6z4puxBayXhpGMdzFzxeb6FKded8uayLbE8kxroI4zEB8taBrxeseAbLdsebpBLf4Rgp9Udkz6gFrnLdjC7oe9xu6begLFEyMj7FnRapRhjazkAuxaEyEIAoEdLSL6ALMfaqnE5SqjxXnCdX8johkpeBRs'


url = "https://developer.globelabs.com.ph/oauth/access_token"

querystring = {"app_id":app_id,"app_secret":app_secret,"code":code}

payload = ""
headers = { 'cache-control': "no-cache" }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)