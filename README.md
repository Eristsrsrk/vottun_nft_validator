# vottun_nft_validator
Python script to verify the owner of an NFT using Vottun APIs.
Folow these instructions if you want to use this python script to verify the owner of an NFT using Vottun APIs.

1) Go to https://vottun.com/ to sign up, and follow the process to get your API key and your project id. 
2) Make sure you have python3 install on your system.
3) Download and unzip this repository.
4) Using the terminal of your choice, go to the location where you downloaded and unziped this folder.
5) Replace <YOUR_VOTTUN_API_KEY> with the API key you created in step 1.
6) Replace <YOUR_VOTTUN_PROJECT_ID> with the project id you created in step 1.
7) Replace <CONTRACT_ADDRESS> with the smart contract address where the NFT was minted.
8) Replace <NETWORK_ID> with the id of the blockchain where the smart contract was deployed.
9) Replace <NFT_ID> with the id of the NFT want to verify the owner of.
10) Run the following code: python3 nftvalidator.py

The response will look like this: 

{
    "owner": "0x8c437496d4b31..4cd47863732165a3"
}


