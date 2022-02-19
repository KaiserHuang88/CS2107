import os

FLAG = "CS2107{}"

# xor 2 byte strings
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


def encrypt(msg) :
    otp = os.urandom(20)
    print(otp.hex())
    print("\n")
    res = b""
    for i in range(0, len(msg), 20):
        res += xor(otp, msg[i:i+20])
    return res

def findOTP(ciphertextString, msg) :
    ciphertextByte = bytes.fromhex(ciphertextString)
    result = b""
    result += xor(msg[0:20], ciphertextByte)
    return result

def check(ciphertextString, msg) :
    otp = findOTP(ciphertextString, msg)
    res = b""
    for i in range(0, len(msg), 20):
        res += xor(otp, msg[i:i+20])
    return res

def decrypt(ciphertextString, msg) :
    ciphertextByte = bytes.fromhex(ciphertextString)
    otp = findOTP(ciphertextString, msg)
    res = b""
    for i in range(0, len(ciphertextByte), 20):
        res += xor(otp, ciphertextByte[i:i+20])
    result = res.decode()
    print(result)






msg = f"Hey Grandma Susan'oo, I have told you not to play with my Photoshop! \
Why did you crop your head on the dragon... {FLAG}".encode()

ciphertextString = "faa4a0ba8d435a2b2015c4625c80443e820c523a9ee190baa2504d20640cca2e6bd54e30990b533ac6e1adf5ea4157243d58d22b7b9d1732950b6d3dddb5b6e9a25e4b64642fcd3b2f915e3bcc52522092a2abf5ba11422a310a852a6a94537f83451d21daa4f9feb8505c2a2a568b6c2fb6646ddd1b0a2efd9589d59e616475300895367faa656c9c185c21edaaeae395000e1a320dc92c3c87563d804e40"
ciphertextHex = 0xfaa4a0ba8d435a2b2015c4625c80443e820c523a9ee190baa2504d20640cca2e6bd54e30990b533ac6e1adf5ea4157243d58d22b7b9d1732950b6d3dddb5b6e9a25e4b64642fcd3b2f915e3bcc52522092a2abf5ba11422a310a852a6a94537f83451d21daa4f9feb8505c2a2a568b6c2fb6646ddd1b0a2efd9589d59e616475300895367faa656c9c185c21edaaeae395000e1a320dc92c3c87563d804e40

print(findOTP(ciphertextString, msg).hex())
print("\n")
print(ciphertextString)
print("\n")
print(check(ciphertextString, msg).hex())
print("\n")
decrypt(ciphertextString, msg)
