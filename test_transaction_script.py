import requests
 
url = "http://localhost:5001/wallet/transact"
 
payload = "{\"recipient\":\"foo\",\"amount\":15}"
headers = {
    'Content-Type': 'application/json'
}
 
response = requests.request("POST", url, headers=headers, data=payload)
 
print(response.text.encode('utf8'))