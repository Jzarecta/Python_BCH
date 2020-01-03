#!/bin/env python

# Write data on the Bitcoin Cash Blockchain

from bitcash import PrivateKeyTestnet

testnet_key = PrivateKeyTestnet()
testnet_key.to_wif()

# We generate a private key

testnet_key.address

# We generate an address

testnet_key.get_balance()

# We output some balance (after a transaction)

output = [
    ('bchtest:qq0sea6rkxzw8eakxy65rwfftfh3qf97zgnagypgvx', 1000, 'satoshi'),
    ]

testnet_key.send(output, message='I am in the blockchain!')

# We output a transaction signature.
