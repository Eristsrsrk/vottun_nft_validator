import requests

url = 'https://api.vottun.tech/erc/v1/erc721/ownerOf'
headers = {
    "Authorization": "Bearer <YOUR_VOTTUN_API_KEY>",
    "x-application-vkn": "<YOUR_VOTTUN_PROJECT_ID>", 
    "Content-Type": "application/json"
        }

data = {   
    "contractAddress": "<CONTRACT_ADDRESS>",
    "network": <NETWORK_ID>,
    "id": <NFT_ID>
    }

try:
    response = requests.post(url, headers=headers, json=data,timeout=10)
    response.raise_for_status()
    json_data = response.json()
# Handle ConnectionError
except requests.exceptions.ConnectionError as ce:
    print('Connection error:', ce)
# Handle Timeout
except requests.exceptions.Timeout as te:
    print('Request timed out:', te)
# Handle HTTPError
except requests.exceptions.HTTPError as he:
    print('HTTP error occurred:', he)
# Handle ValueError
except ValueError as ve:
    print('JSON decoding error:', ve)
else:
    print('Request was successful')
    print(json_data)




