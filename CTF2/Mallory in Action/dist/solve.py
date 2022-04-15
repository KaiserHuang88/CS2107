import json
from hashlib import sha512

from Crypto.Util.number import getPrime, getRandomRange, getRandomNBitInteger, long_to_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

def encrypt(msg: bytes, key: int):
    key = long_to_bytes(key)
    key = sha512(key).digest()[:16]
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(msg, 16))
    return {"iv": cipher.iv.hex(), "ciphertext": ct.hex()}

# If unpad error occurs then it means that 
# you are not supplying the right input
def decrypt(iv: str, ct: str, key: int):
    iv = bytes.fromhex(iv); ct = bytes.fromhex(ct)
    key = long_to_bytes(key)
    key = sha512(key).digest()[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = unpad(cipher.decrypt(ct), 16)
    return ct

print(decrypt("9d19c4f5e7e6a8d335a5fce16df30d55", "920812a7aa9fac330105892da945ae24097fc3e278a3ddd8584daa34d28ba865", 244404374794464105652216654517509287314182826251227867090907797626668614897097939743531161362545277168973516124491775654824421295184638404565703967895187))




