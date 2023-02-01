letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    encrypt=input("Type 'Y' to encrypt or 'N' to decrypt: ")

    encrypt=encrypt.upper()

    if encrypt == "Y":

        encrypt_fun(letters)
        
    if encrypt == "N":

        decrypt_fun(letters)


def encrypt_fun(letters):

    stringtoencrypt=input("Enter message to encrypt:")

    stringtoencrypt=stringtoencrypt.upper()

    ciphershift=input("Enter key (1-25): ")

    ciphershift=int(ciphershift)

    stringencrypted=""

    for character in stringtoencrypt:

        position = letters.find(character)

        newposition = position+ciphershift

        if character in letters:

            stringencrypted = stringencrypted + letters[newposition]

        else:

            stringencrypted = stringencrypted + character

            

    ciphershift=str(ciphershift)

    print("Key = "+ciphershift)

    print("Encrypted message:")

    print(stringencrypted)

    print("")
    print("")

    main()


def decrypt_fun(letters):

    stringtodecrypt=input("Message to decrypt:")

    stringtodecrypt=stringtodecrypt.upper()

    ciphershift=input("Enter key (1-25): ")

    ciphershift=int(ciphershift)

    stringdecrypted=""

    for character in stringtodecrypt:

        position = letters.find(character)

        newposition = position-ciphershift

        if character in letters:

            stringdecrypted = stringdecrypted + letters[newposition]

        else:

            stringdecrypted = stringdecrypted + character

    ciphershift=str(ciphershift)

    print("Key = "+ciphershift)

    print("Decrypted message:")

    print(stringdecrypted)

    print("")

    tryAgain = input("Try another key? (Y/N): ")
    
    tryAgain = tryAgain.upper()
    
    if tryAgain == "Y":
        
        decrypt_fun(letters)
        
    else:
        
        print("")
        
        main()


main()
