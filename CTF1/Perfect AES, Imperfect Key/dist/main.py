from ctypes.wintypes import PINT
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha512
import json
"""
FLAG = "CS2107{ONE_TWO_THREE_FOUR_FIVE_SIX_SEVEN_EIGHT_NINE}"

key = sha512(os.urandom(20)[:3]).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(FLAG.encode('utf-8'), AES.block_size))
iv, ct = cipher.iv, ct_bytes
iv = cipher.iv
print(iv)
print(key.hex())
print(ct_bytes.hex())
print(f'iv : {iv.hex()}\nct : {ct.hex()}')
"""

def decryption() :
    while True :
        iv = "4b0fb9a4dfbabe6810b2fb01d2012b84"
        ct = "c089a2553fdcbb0bbdbd7655fc34c75eb7f2ccd28fc801480c5a15b7f366f8737a30aa3e845d79e509486ffd6aa81a0b"
        key = sha512(os.urandom(20)[:3]).digest()[:16]
        cipher = AES.new(key, AES.MODE_CBC, bytearray.fromhex(iv))
        pt = cipher.decrypt(bytearray.fromhex(ct))
        if pt[:6] == "CS2107".encode('utf-8') :
            print(pt.decode('utf-8'))

decryption()

