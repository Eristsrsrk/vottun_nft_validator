import requests

address = input("Type or paste the address you want to verify: ")
nft_id = int(input("NFT_ID: "))
url = 'https://api.vottun.tech/erc/v1/erc721/ownerOf'
headers = {
    "Authorization": "Bearer <YOUR_VOTTUN_API_KEY>",
    "x-application-vkn": "<YOUR_VOTTUN_PROJECT_ID>", 
    "Content-Type": "application/json"
        }

data = {   
    "contractAddress": "<CONTRACT_ADDRESS>",
    "network": <NETWORK_ID>,
    "id": nft_id
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
    owner_value = json_data["owner"]
    if address == owner_value:
        print("TRUE. This address is the owner of the NFT.")
    else:
        print("FALSE. This addres is not the owner of the NFT.")
