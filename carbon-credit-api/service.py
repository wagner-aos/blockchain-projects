from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

def sign_transaction(private_key, txn_dict):
    account = w3.eth.account.from_key(private_key)
    signed_txn = account.signTransaction(txn_dict)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return tx_hash

# # Sample usage
# private_key = 'YOUR_PRIVATE_KEY'
# transaction = {
#     'to': 'RECIPIENT_ADDRESS',
#     'value': w3.toWei(1, 'ether'),  # Replace with token-specific values
#     'gas': 2000000,
#     'gasPrice': w3.toWei('40', 'gwei'),
#     'nonce': w3.eth.getTransactionCount('SENDER_ADDRESS'),
# }

# transaction_hash = sign_transaction(private_key, transaction)
# print(f"Transaction hash: {transaction_hash.hex()}")