import numpy as np


# Key-scheduling algorithm function
def KSA(key):

    # Defines key length
    keylength = len(key)

    # Defines range as a list
    S = list(range(256))

    # Defines j
    j = 0

    # For j modulo range (up to 256 in this case), then swap S[i] and S[j]
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]

    return S


# Pseudo-random generation algorithm Function
def PRGA(S, n):

    # Defines i, j as 0
    i = 0
    j = 0

    # Defines empty array for key
    key=[]

    # Where n is the length of the plaintext, while loop repeats until n !> 0, then appends K to key for each instance
    while n>0:
        n -= 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        K = S[(S[i] + S[j]) % 256] 
        key.append(K)
        
    return key


# USER INPUTS
key = input("Enter key: ")
plaintext = input("Enter Plaintext: ")

print("")


# Key translation into array
def key_array(s):
    return [ord(c) for c in s]


# Takes user input key and calls the key array function
key = key_array(key)


# Calls key-Scheduling Algorithm (KSA) function after key array
S = KSA(key)


# Calls pseudo-random generation algorithm (PRGA) function and output keystream in array form
keystream = np.array(PRGA(S, len(plaintext)))
print("Keystream array:" , keystream)


# Output plaintext in array form
plaintext = np.array([ord(i) for i in plaintext])
print("Plaintext array:" , plaintext)

print("")


# XOR the 2 arrays
cipher = keystream ^ plaintext


# Output ciphertext in HEX
print("Ciphertext in HEX format:" , cipher.astype(np.uint8).data.hex())

