import math
characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def XOR(bit1, bit2):
    if bit1 == bit2: 
        return("0")
    else: 
        return("1")

def XORonByte(byte, key):

    emsg = ""
    
    for i in range(len(byte)):
        emsg += XOR(byte[i], key[i])

    return emsg

# print(XORonByte("0010", "0011"))

def XORonLetter(letter, keyLetter):
    
    letterBin = encode(letter)
    keyLetterBin = encode(keyLetter)

    encryptedLetter = XORonByte(letterBin, keyLetterBin)

    return decode(encryptedLetter)

k = input("Enter a word:")

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z'] 

for i in range(26):
    if k == alph[i]:
        x = i
        print(x)
    else:
        continue 

scath = ['b','p','v','r','g','w','d','t','m','n','l','h','k','s','z','a','i','e','o','u','j','f','c','q','x','y'] 

key = scath[x]
print(key)

def generateKey(message):
    if len(message) == len(key):
        return key
    elif len(message)<len(key):
        key = key[0:len(message)]
        return key
    else:
        genkey = ""
        rep = math.floor(len(message)/len(key))
        mo = len(message)%len(key)
        for i in range(rep):
            genkey += key
        genkey = genkey + key[0:mo]
        return genkey    

def XORonSentence(sentence):
    encryptedSentence = ""
    genkey=generateKey(sentence)    
    for i in range (len(sentence)):
        encryptedSentence += XORonLetter(sentence[i], genkey[i])
    
    return encryptedSentence

msg = input("Enter a message: ")
# print(len(msg))
print("Your encrypted message is: ", XORonSentence(msg))
# print(len(XORonSentence(msg, key)))

