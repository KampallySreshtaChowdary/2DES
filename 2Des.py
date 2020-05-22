#!/usr/bin/env python
import binascii
import itertools
from pyDes import des
from pyDes import CBC
import sys

plaintext = sys.argv[1]
keyOne = sys.argv[2]
keyTwo = sys.argv[3]

iv='5edcc504'

def_pad="0000000000000000"

effKeyLength1 = len(keyOne)
effKeyLength2 = len(keyTwo)

def twodes(plain, keyOne, keyTwo):
    cipherOne = des(binascii.unhexlify(keyOne), CBC, "5edcc504", pad=None)
    cipherTwo = des(binascii.unhexlify(keyTwo), CBC, "5edcc504", pad=None)
    return cipherTwo.encrypt(cipherOne.encrypt(plain))

def checkPad(effKeyLength):
    if(effKeyLength > 4):
        #since the test scope is out of the condition print the warning
        print 'Key Length greater than 4 will take much time'
    return def_pad[0:-(effKeyLength)]

def generateCipher(plaintext, keyOne, keyTwo, effKeyLength1, effKeyLength2):
    pad1=checkPad(effKeyLength1);
    pad2=checkPad(effKeyLength2);
    #initialize the dictionary to hold the values    
    #Loop thorugh all possible keys
    keyOne = pad1 + keyOne
    keyTwo = pad2 + keyTwo
    if(len(keyOne) != 16):
        print "padding gone wrong..."
    if(len(keyTwo) != 16):
        print "padding gone wrong..."
    #Initate the key for single DES encryption
    ciphertext == binascii.hexlify(twodes(plaintext,keyOne,keyTwo));
    print ciphertext

def main():
    generateCipher(plaintext, keyOne, keyTwo, effKeyLength1, effKeyLength2)


main()
    
