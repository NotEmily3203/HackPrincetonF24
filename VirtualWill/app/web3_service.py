import json
from web3 import Web3
from django.conf import settings

# Connect to the Ganache instance (or any other Ethereum node)
ganache_url = settings.GANACHE_URL  # It is better to store URLs and private keys in settings
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if the connection is established
if not web3.is_connected():
    raise Exception("Failed to connect to Ethereum network")

# Smart contract details
contract_address = settings.CONTRACT_ADDRESS
contract_abi = json.loads(settings.CONTRACT_ABI)

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def get_contract_balance():
    return contract.functions.getContractBalance().call()

def is_owner_deceased():
    return contract.functions.isOwnerDeceased().call()

def get_owner_details():
    owner_wallet = contract.functions.ownerWallet().call()
    owner_name = contract.functions.ownerName().call()
    return owner_wallet, owner_name

def get_beneficiary_details():
    beneficiary_wallet = contract.functions.beneficiaryWallet().call()
    beneficiary_name = contract.functions.beneficiaryName().call()
    return beneficiary_wallet, beneficiary_name

def check_in(account, private_key):
    # Build the transaction
    transaction = contract.functions.checkIn().buildTransaction({
        'from': account,
        'nonce': web3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': web3.toWei('20', 'gwei')
    })
    
    # Sign the transaction
    signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
    
    # Send the transaction
    transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return transaction_hash.hex()
