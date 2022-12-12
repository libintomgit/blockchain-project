<strong>Name: Libin Tom <br>
Dockerhub repo: </strong>
```sh
docker pull libintomkk/blockchain-app:latest
```

# blockchain-project
Repo for the blockchain project in mcs cloud computing
 
# 1 - Create a digital wallet in metamask
> Create an Ethereum account (public/private secp256k1 keypair with associated address) on Ethereum Goerli network with at least 100-bits of entropy.

## Install metamask

* Download plugin from https://metamask.io/download/

## Create account

* Click on the metamask entention in the browser extentions list to create a new digital wallet account

## this will open up in a new tab and follow the onscreen instruction

* Select the goreli test network

> Once the accout is created and logged in. Click on the right top network dropdown and click on the show/hide test network
> and turn the show test network ON
> Note: now you have your test netwrok listed in the Network dropdown

```sh
select the Goreli test network

# Your account should have 0 GoereliETH
```

## Export Privat Key

* Click on the more options (3 dots) and Accout details
* Export private key

## View account on ether scan

* Click on the more options (3 dots) and view account on ether scan

## Export private key
* Click on the metamask account more options to show the private key
> Store it safe some where

# 2 - Create an ERC20-compliant, fixed-supply token with the following parameters:
## Creating a Security Audited, Production Ready ERC20 contract
> In order to create an ERC20 contract that has been security audited, we will use one of the Open Zeppelin contracts.
> Open Zeppelin contracts are security audited best practices implementations. They are used throughout the industry.
> Their github is at the following address:
* Refferance of the code in the ecr20.sol
> https://github.com/OpenZeppelin
> https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/contracts/token/ERC20
> https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC2 0/ERC20.sol

## Create Smart contract
> Smart contract is code running on the blockchain.
* smart contract is created using the Remix IDE (buit for the purose)
* https://remix.ethereum.org/

* In remix, create a file with .sol extention (ex. erc20.sol)
* Copy the code from the [erc20.sol](https://github.com/libintomgit/blockchain-project/blob/main/erc20.sol) to the new file in remix
> This is fully working smart contract created using the OpenZeppelin
> This smart contract stores a number on the blockchain and allows it to be retrieved

## change the token name
* Inside the code just pasted find and modifiy the below mentioned variables with your token name and symbol to your desired one
```sh
_name = "SHB_XXXXX";
_symbol = "SHB_XXXXX";
```
## Compile smart contract
* Click on the compile tab and run the compiler in the solidiy compiler

> Makesure to fix the errors if any and recompile until not errors

## Deploy compiled smart contract
> To the metamask digital wallet

* In environment select INJECTED PROVIDER - metamask
* Now select the account and approve it when the metamask pliggin will openup

## View the transaction on etherscan
* In the right below terminal pannel of remix, find the transactoin status and link to ETHERSCAN, click on it to navigate

## VERIFY
> assuming you are in the etherscan

* Click in the CONTRACT tab (usually in the middle of the page)

* Click on the verify and publish

> This will redirects to VERIFY AND PUBLISH CONTRACT SOURCE CODE

* Seave the contract address area as is with your deployed contract hash

* Select the compiler type SOLIDITY(single file)

* compiler version to the compiler used to compile in the remix (mostly 0.8.7+commit.e28d00a7)

* License type none

* click  CONTINUE

## Copy paste code to verify

* Copy the whole erc20.sol code from the remix and paste it in the ENTER THE SOLIDITY CONTRACT CODE BELOW

* scrol down.. make sure you are not a robot

## Verify and Publish
> This will verify and publish the block

> scrol down and copy the ABI CONTRACT -  CONTENT and store it in a file for now

# 3 - Deploy the token contract to the Ethereum Testnet (Goerli).
## Import token to account

* Copy the transaction hash from the etherscan (to adderess)

* Open the metamask, click on the more option (3 dots) for expanded view

* Click on the ASSESTS of goerliETH accout (is it place below the account balance and next to activity)

* Click on the import tokens below

* Paste the token to TOKEN CONTRACT ADDRESS

> his will automatically pull the symobl and token decimial we have deployed

# 4 - Build an application to transfer the token and eth
## Application to transfer the token and eth over the api rather using the web console

* Create and activate a virtual environment for python packages
```sh
sudo python -m venv name_of_env

source name_of_env/bin/activate
```
* Install the python [requiremtns](https://github.com/libintomgit/blockchain-project/blob/main/requirements.txt) for the Web3 and python-decouple
```sh
# install requiremtns using the requirements.txt file in this directory
pip install -r requirements.txt
```

* Create a web3 helper using the [.env](https://github.com/libintomgit/blockchain-project/blob/main/DOTenv) file (to manage value in different file )
```sh
# change the file name of DOTenv to .env

# add the contract address created in the above step to CONTRACT_ADDRESS=pate_contract_address

# add the owner address to which the contract address was imported to OWNER_ADDRESS=paste_the_owner_address (find this in the metamask)

# add the secret key of owner account to SUPER_SECRET_PRIVATE_KEY=secrete_key (find this in the metamask)

# add the seed phrase of the account to SEED_PHRASE=seed_words (find this in the metamask)

# leave the TARGET_ADDRESS= blank and commented as we provide this in the API later

# add the abi generated from the goerli.etherescan contract verification abi=[{copy paste the complete abi}]
```
* Web3 helper code is in [web3helper.py](https://github.com/libintomgit/blockchain-project/blob/main/web3helpers.py)

* Webserver code is in [webserver.py](https://github.com/libintomgit/blockchain-project/blob/main/webserver.py)

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
```

# EOF





