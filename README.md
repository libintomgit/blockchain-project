Name: Libin Tom
Dockerhub repo: 
```sh
docker pull libintomkk/blockchain-app:latest
```

# blockchain-project
Repo for the blockchain project in mcs cloud computing
 
# 1 - Create a digital wallet in metamask
> Create an Ethereum account (public/private secp256k1 keypair with associated address) on Ethereum Goerli network with at least 100-bits of entropy.

## Install metamask
```sh
search for metamask
and download plugin from https://metamask.io/download/
```

## Create account
```sh
click on the icon on in the extention to create new account

## this will open up in a new tab and follow the onscreen instruction
```
## Select the goreli test network
```sh
Once the accout is created and logged in. Click on the right top network dropdown and click on the show/hide test network

and turn the show test network ON
```
> Note: now you have your test netwrok listed in the Network dropdown

```sh
select the Goreli test network

# Your account should have 0 GoereliETH
```

## Export Privat Key
```sh
click on the more options (3 dots) and Accout details

Export private key
```

## View account on ether scan
```sh
click on the more options (3 dots) and view account on ether scan

Export private key
```

# 2 - Create an ERC20-compliant, fixed-supply token with the following parameters:
## Smart contract
* Smart contract is code running on the blockchain.

```sh
smart contract is created using the Remix (a smart contract code editor)

https://remix.ethereum.org/

```
* Under contracts directory in remix, select 1_storage.sol file
* that should have some code like below

```sh
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */
contract Storage {
    uint256 number;
    /**
     * @dev Store value in variable
     * @param num value to store
     */
    function store(uint256 num) public {
        number = num;
}
    /**
     * @dev Return value
     * @return value of 'number'
     */
    function retrieve() public view returns (uint256){
        return number;
} }

## This smart contract stores a number on the blockchain and allows it to be retrieved

```
## Testing Your Smart Contract
```sh
Choose Environment Remix VM in Deploy and Run Transactions Menu.

click deploy

```
## Creating a Security Audited, Production Ready ERC20 contract
* In order to create an ERC20 contract that has been security audited, we will use one of the Open Zeppelin contracts.
Open Zeppelin contracts are security audited best practices implementations. They are used throughout the industry.
Their github is at the following address:

## skip to next step - this is just for refferance as in from where the code was originally taken
```sh 

https://github.com/OpenZeppelin

# As we are looking for ERC20 contract, we need to go to the following URL:

https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/contracts/token/ERC20

# We’re going to use their erc20.sol contract.

https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC2 0/ERC20.sol
```
## Use the fully working erc-20.eol
[use this erc-20.eolfile erc-20.eol](https:://)
```sh
create a file called erc20.eol in remix

copy the content from the above [file]([use this erc-20.eolfile erc-20.eol]) and paste it in the erc-20.eol
```
## change the token name
```sh
inside the code just pasted find modifiy the below mentioned variables with your last 5 digits of your student id

_name = "SHB_XXXXX";
_symbol = "SHB_XXXXX";
```

## Compile the code
```sh
navigate to the COMPILE icon in the left side pane of remix

and click on the COMPILE blue button

```
## Deploy
* Deploy the token to the goerliETH accout
```sh
navigate to DEPLOY icon in the left side pane of remix

change the environment to INJECTED PROCIDER - METAMASK

it will open the metamask pluggin to connect with the remix and will add the account to the remix automatically
```
```sh
change the gas limit to 30K

select the contract MYSPECIALTOKENSHIB3-erc20.sol

then DEPLOY
```
```sh
metamask will popup for confirming the transaction - CONFIRM
```
* view the transaction on etherscan
```sh
in the right below terminal pannel of remix, find the transactoin status and link to ETHERSCAN

click on it to navigate
```
## VERIFY
* assuming you are in the etherscan
```sh 
click in the CONTRACT tab (usually in the middle of the page)

click on the verify and publish

## this will redirects to VERIFY AND PUBLISH CONTRACT SOURCE CODE

leave the contract address area as is with your deployed contract hash

select the compiler type SOLIDITY(single file)

compiler version to the compiler used to compile in the remix mostly 0.8.7+commit.e28d00a7

license type none

click  CONTINUE
```
* copy paste code to verify

```sh

copy the whole erc20.sol code from the remix and paste it in the ENTER THE SOLIDITY CONTRACT CODE BELOW

scrol down.. make sure you are not a robot

VERIFY AND PUBLISH

## This will verify and publish the block

scrol down and copy the ABI CONTRACT -  CONTENT and store it in a file for now

```

# 3 - Deploy the token contract to the Ethereum Testnet (Goerli).
## Import token to account
```sh
copy the transaction hash from the etherscan (to adderess)

open the metamask, click on the more option (3 dots) for expanded view

click on the ASSESTS of goerliETH accout (is it place below the account balance and next to activity)

click on the import tokens below

paste the token to TOKEN CONTRACT ADDRESS

this will automatically pull the symobl and token decimial we have deployed

ADD CUSTOM TOKEN
```

# 4 - Build an application to transfer the token and eth
* Create and activate a virtual environment for python packages
```sh
sudo python -m venv name_of_env

source name_of_env/bin/activate
```
* Install the python requiremtns for the Web3 and python-decouple
```sh
# install requiremtns using the requirements.txt file in this directory
pip install -r requirements.txt
```

* Create a web3 helper using the .env file (to manage value in different file )
```sh
# change the file name of DOTenv to .env

# add the contract address created in the above step to CONTRACT_ADDRESS=pate_contract_address

# add the owner address to which the contract address was imported to OWNER_ADDRESS=paste_the_owner_address (find this in the metamask)

# add the secret key of owner account to SUPER_SECRET_PRIVATE_KEY=secrete_key (find this in the metamask)

# add the seed phrase of the account to SEED_PHRASE=seed_words (find this in the metamask)

# leave the TARGET_ADDRESS= blank and commented as we provide this in the API later

# add the abi generated from the goerli.etherescan contract verification abi=[{copy paste the complete abi}]
```
* Web3 helper code is in web3helper.py

* Webserver code is in webserver.py

* Run the webserver
```sh
python webserver.py

# once the webserver is running access it using 127.0.0.1:8080 to check the status
```
## Now transfer the token and eth using the below cURL api
```sh
#Transfer eth change the address to desired target address and change the amount to desired amount
curl --header "Content-Type: application/json" --request POST --data '{"address":"0xE1d572356C174Baa4110A203a73cEEfEA4205180", "amount":"0.05"}' http://localhost:8080/eth

#Transfer token change the address to desired target address
curl --header "Content-Type: application/json" --request POST --data '{"address":"0xE1d572356C174Baa4110A203a73cEEfEA4205180"}' http://localhost:8080/token
```

# 5 - Containerise the application using docker 
## for ease of running application over the webserver with out installing any dependencies or ther settings

## Make sure to install docker engine and docker is running.

* Build the docker container using the Docerfile in this directory
```sh
doceker build -t reponame/imagename

# check the image is docker images 
docker images
```
* Run the docker continer
```sh
#Create a direcory in the current directory (we will use this to mount the volume to the docker to make changes in the application later poin)\
mkdir dockervol

#Run docker container using the image we created earlier
docker run --name custom_name -p 8090:8080 -d -v $(pwd)/dockervol:/var/dockervol reponame/imagename
```

## Use the cURL api to so the transfer by replacing the http://localhost:8080/eth_or_token to http://localhost:8090/eth_or_token

* Push the new image to docker hub
```sh
create a docker hub account 

create a repository

name the repository with reponame/imagename

# push the image to the created repo to from the terminal

docker login -u username
# enter the password when propted

docker push reponame/imagename:latest
```
* Pull the image from the docker hub
```sh
docker pull reponame/imagename:latest






