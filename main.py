#!/bin/env python

# Developing BCH with Python
# Help interact with Bitcoin Cash with Python
# using the bitcash module

# Check balance using a key
from bitcash import key

key = Key()
print(key.address)
print(key.get_balance())
print(key.get_balance('usd'))

## Send some coins (needs funding previously)
key.send([( \
            key.address, \
            0.1, \
            'usd'    )])

## Create a WIF (wallet import format)  backup
print(key.to_wif())

## Recover your MONEY!!
print('Please put your WIF key?')
mykey=raw_input()
recovered_key = Key(mykey)
