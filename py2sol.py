import json
from web3 import Web3

# Connect to local Ganache instance
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection status
if web3.is_connected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect")

contract_address = "0x76e480C6d8521bEF535362fB4446337e9509e149"  # Contract address after deployment
owner_address = "0x418A486a51603D8367EcaC11eeDDEFe47dA87E7f"  # Owner's Ethereum address
private_key = "0x1bce540a12d41159a0853d97beeae84f8838628307525b82183d3a165ac8ee36"

contract_abi = json.loads('''[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ownerName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_beneficiaryName",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_beneficiaryWallet",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_ipfsHash",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_oracle",
				"type": "address"
			}
		],
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "beneficiaryWallet",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "beneficiaryName",
				"type": "string"
			}
		],
		"name": "BeneficiaryAssigned",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"name": "CheckIn",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "FundsHeld",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "FundsTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			}
		],
		"name": "IpfsAssigned",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "ownerWallet",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "ownerName",
				"type": "string"
			}
		],
		"name": "OwnerAssigned",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"inputs": [],
		"name": "beneficiaryName",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "beneficiaryWallet",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "checkIn",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "checkInPeriod",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getContractBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ipfsHash",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "isOwnerDeceased",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "lastCheckIn",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "oracle",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ownerName",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ownerWallet",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "transferFundsToBeneficiary",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	}
]''')

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def get_contract_balance():
    balance = contract.functions.getContractBalance().call()
    return balance

def is_owner_deceased():
    deceased_status = contract.functions.isOwnerDeceased().call()
    print(f"Is owner deceased? {deceased_status}")
    return deceased_status

print(f"I got this {get_contract_balance()} many fingers")
is_owner_deceased()

# Get owner details
owner_wallet = contract.functions.ownerWallet().call()
owner_name = contract.functions.ownerName().call()
print(f"Owner Wallet: {owner_wallet}")
print(f"Owner Name: {owner_name}")

# Get beneficiary details
beneficiary_wallet = contract.functions.beneficiaryWallet().call()
beneficiary_name = contract.functions.beneficiaryName().call()
print(f"Beneficiary Wallet: {beneficiary_wallet}")
print(f"Beneficiary Name: {beneficiary_name}")

# Check-in function (updates the last check-in timestamp)
def check_in():
    # Build the transaction
    transaction = contract.functions.checkIn().buildTransaction({
        'from': account,
        'nonce': web3.eth.getTransactionCount(account),
        'gas': 2000000,
        'gasPrice': web3.toWei('20', 'gwei')
    })
