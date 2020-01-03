#!/bin/env python

# This will implement a Satoshi Shotgun action
# a script that flood the blockchain with
# transactions

import time
from bitcash import PrivateKeyTestnet

def shoot():
    out = [
        (ADDRESS, 1000, 'satoshi'),
        ]
    KEY.get_unspent()  # this refreshes the UTXO set
    print(KEY.send(output))


def main(tx_count=10):
    for i in range(tx_count):
        shoot()
        time.sleep(2)  # sends a transaction every 2 seconds

if __name__ == '__main__':
    main()
