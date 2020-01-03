#!/bin/env python

from bitcash import PrivateKeyTestnet

def show_pair():
    key  = PrivateKeyTestnet()
    wif = key.to_wif()
    address = key.address
    return wif + ' is the private key associated with ' + address

# This will return
# cPQ6D6ad4ejj1xNuH5ApqM3QijtjL3pZwwkEM3Mxdmtts1fmHZtb is the
# private key associated with bchtest:qq25uvnlvacamvmuqulp2c3k7pgal0x3xucenm9cdv

print(show_pair())
