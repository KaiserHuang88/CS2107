import random

f = open("encrypted2.txt", "r").read().upper()

alphabet = [chr(ord('A') + i) for i in range(26)]
#random.shuffle(alphabet)

alphabetArray = [0] * 26

def conversion(oldIndice) :
    switcher = {
        0: 'U',
        1: 'A',
        2: 'X',
        3: 'N',
        4: 'Y',
        5: 'H',
        6: 'Y',
        7: 'I',
        8: 'J',
        9: 'L',
        10: 'M',
        11: 'O',
        12: 'V',
        13: 'G',
        14: 'F',
        15: 'D',
        16: 'B',
        17: 'W',
        18: 'P',
        19: 'S',
        20: 'C',
        21: 'K',
        22: 'T',
        23: 'R',
        24: 'E',
        25: 'Q'
    }

    return switcher.get(oldIndice, "nothing")

encrypted = ""
"""for i in f:
    if (i in alphabet):
        encrypted += alphabet[ord(i) - ord('A')]
    else :
        encrypted += i
"""
for i in f :
    if (i in alphabet):
        alphabetArray[ord(i) - ord('A')] += 1

for i in f :
    if (i in alphabet) :
        encrypted += conversion(ord(i) - ord('A'))
    else :
        encrypted += i

print(alphabetArray)
g = open("decrypted.txt", 'w')
g.write(encrypted)