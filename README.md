Folow these instruction if you want to verify if an address is the owner of an NFT using Vottun APIs:

1) Go to https://vottun.com/ to sign up, and follow the process to get your API key and your project id. 
2) Make sure you have python3 installed in your system.
3) Download and unzip this repository.
4) Using the terminal of your choice, go to the location where you downloaded and unzipped this repository.
5) Replace <YOUR_VOTTUN_API_KEY> with the API key you created in step 1.
6) Replace <YOUR_VOTTUN_PROJECT_ID> with the project id you created in step 1.
7) Replace <CONTRACT_ADDRESS> with the smart contract address where the NFT was minted.
8) Replace <NETWORK_ID> with the id of the blockchain where the smart contract was deployed on.
9) Run the folling code: "python3 nftvalidator.py"
10) Input the the address, press enter, input the NFT id, and press enter.

If the request is successful, you will get:

"TRUE. This address is the owner of the NFT."
or
"FALSE. This address is not the owner of the NFT."
