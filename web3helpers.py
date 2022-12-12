from web3 import Web3
from decouple import config

infuraUrl= config('INFURA_URL')
contractAddress = Web3.toChecksumAddress(config('CONTRACT_ADDRESS'))
ownerAddress = Web3.toChecksumAddress(config('OWNER_ADDRESS'))
privateKey = config('SUPER_SECRET_PRIVATE_KEY')
abi = config('ABI')
# targetAddress = Web3.toChecksumAddress(config('TARGET_ADDRESS'))

# gets the balance of the provided account
def balanceOf(account):
   web3 = Web3(Web3.HTTPProvider(infuraUrl))
   res = web3.isConnected()
   if res:
       contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
       bal = contract_instance.functions.balanceOf(account).call()
   return bal

def decimals():
   web3 = Web3(Web3.HTTPProvider(infuraUrl))
   res = web3.isConnected()
   if res:
       contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
       decimals = contract_instance.functions.decimals().call()
   return decimals

def symbol():
   web3 = Web3(Web3.HTTPProvider(infuraUrl))
   res = web3.isConnected()
   if res:
       contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
       symbol = contract_instance.functions.symbol().call()
   return symbol

# Function to transfer token

def tokenTransfer(address):
    web3 = Web3(Web3.HTTPProvider(infuraUrl))
    res = web3.isConnected()
    if res:
        #  check balance function works
        bal = balanceOf(ownerAddress)
        if web3.isConnected():
            print('CONNECTED TO WEB3!!!!')
            contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
            # decimals = 10 ** 18 hard coding!!  NOOOOO
            targetAccount = web3.toChecksumAddress(address)
            dec = 10 ** decimals()
            bal = balanceOf(targetAccount)
            targetBalance = bal / dec
            transferValue = 1000 * dec
            if targetBalance >=1000:
                transferValue = 1 * dec

            print("about to transfer " + str(transferValue/dec) + " " + symbol() + " to " + targetAccount)
            # create a tx calling the transfer function in my token contract
            nonce = web3.eth.getTransactionCount(ownerAddress)

            transaction = contract_instance.functions.transfer(
            targetAccount, transferValue).buildTransaction({
                'gas': 200000,
                'gasPrice': web3.toWei('100', 'gwei'),
                'from': ownerAddress,
                'nonce': nonce,
                'chainId': 5 #goerli chain id
            })

            #  sign the tx
            signed_tx = web3.eth.account.sign_transaction(transaction, privateKey)

            #  submit the tx
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print('tx hash: ' + tx_hash.hex())

            web3.eth.waitForTransactionReceipt(tx_hash)
            print('tx mined')

# Function to transfer eth

def ethTransfer(address, amountInEther):
    web3 = Web3(Web3.HTTPProvider(infuraUrl))

    if web3.isConnected():
        print('CONNECTED TO WEB3!!!!')
        targetAccount = Web3.toChecksumAddress(address)

        nonce = web3.eth.getTransactionCount(ownerAddress)
        print("nonce (tx count) is " + str(nonce))

        gasPrice = web3.toWei('100', 'gwei')
        value = web3.toWei(amountInEther, 'ether')

        # build the tx
        tx = {
            'nonce': nonce,
            'to': targetAccount,
            'value': value,
            'gas': 50000,
            'gasPrice': gasPrice,
            'chainId': 5
        }

        #  sign the tx
        signed_tx = web3.eth.account.sign_transaction(tx, privateKey)

        #  submit the tx
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print('tx hash: ' + tx_hash.hex())

        web3.eth.waitForTransactionReceipt(tx_hash)
        print('tx mined')

#  Print details of the owener account

print("Initiating the code.... .....")

print("symbol is: " + symbol())

print("decimal places are: " + str(decimals()))

print("balance of owner account " + ownerAddress + " is " + str(balanceOf(ownerAddress)))