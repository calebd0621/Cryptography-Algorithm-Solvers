def convertPlainTextToDiagraphs (plainText):
    
    # append X if Two letters are being repeated
    
    for s in range(0,len(plainText)+1,2):
        
        if s<len(plainText)-1:
            
            if plainText[s]==plainText[s+1]:

                plainText=plainText[:s+1]+'X'+plainText[s+1:]

    # append Z if the total letters are odd, to make plaintext even
    if len(plainText)%2 != 0:

        plainText = plainText[:]+'Z'

    return plainText


def generateKeyMatrix (key): 

    # Intially create 5X5 matrix with all values as 0
    # [
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0]
    # ]

    matrix_5x5 = [[0 for i in range (5)] for j in range(5)]

    simpleKeyArr = []

    for c in key:

        if c not in simpleKeyArr:

            if c == 'J':

                simpleKeyArr.append('I')

            else:

                simpleKeyArr.append(c)

    is_I_exist = "I" in simpleKeyArr

    # A-Z's ASCII Value lies between 65 to 90

    for i in range(65,91):

        if chr(i) not in simpleKeyArr:

            if i==73 and not is_I_exist:

                simpleKeyArr.append("I")

                is_I_exist = True

            elif i==73 or i==74 and is_I_exist:

                pass

            else:

                simpleKeyArr.append(chr(i))

    index = 0

    for i in range(0,5):

        for j in range(0,5):

            matrix_5x5[i][j] = simpleKeyArr[index]

            index+=1
            
    print("")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix_5x5]))
    print("")
    
    return matrix_5x5


def indexLocator (char,cipherKeyMatrix):

    indexOfChar = []

    # convert the character value from J to I

    if char=="J":

        char = "I"

    for i,j in enumerate(cipherKeyMatrix):

        # enumerate will return object like this:         
        # [
        #   (0, ['K', 'A', 'R', 'E', 'N']),
        #   (1, ['D', 'B', 'C', 'F', 'G']), 
        #   (2, ['H', 'I', 'L', 'M', 'O']), 
        #   (3, ['P', 'Q', 'S', 'T', 'U']), 
        #   (4, ['V', 'W', 'X', 'Y', 'Z'])
        # ]
        # i,j will map to tupels of above array

        # j refers to inside matrix =>  ['K', 'A', 'R', 'E', 'N'],

        for k,l in enumerate(j):

            if char == l:

                indexOfChar.append(i) #add 1st dimension of 5X5 matrix => i.e., indexOfChar = [i]

                indexOfChar.append(k) #add 2nd dimension of 5X5 matrix => i.e., indexOfChar = [i,k]

                return indexOfChar


def encryption (plainText,key):

    cipherText = []

    # 1. Generate Key Matrix
    keyMatrix = generateKeyMatrix(key)

    # 2. Encrypt According to Rules of playfair cipher
    i = 0
    while i < len(plainText):
        
        # 2.1 calculate two grouped characters indexes from keyMatrix

        n1 = indexLocator(plainText[i],keyMatrix)

        n2 = indexLocator(plainText[i+1],keyMatrix)


        if n1[1] == n2[1]:

            i1 = (n1[0] + 1) % 5

            j1 = n1[1]

            i2 = (n2[0] + 1) % 5

            j2 = n2[1]

            cipherText.append(keyMatrix[i1][j1])

            cipherText.append(keyMatrix[i2][j2])

            cipherText.append(", ")

        # same row
        elif n1[0]==n2[0]:

            i1= n1[0]

            j1= (n1[1] + 1) % 5

            i2= n2[0]

            j2= (n2[1] + 1) % 5

            cipherText.append(keyMatrix[i1][j1])

            cipherText.append(keyMatrix[i2][j2])

            cipherText.append(", ")

        else:

            i1 = n1[0]

            j1 = n1[1]

            i2 = n2[0]

            j2 = n2[1]

            cipherText.append(keyMatrix[i1][j2])

            cipherText.append(keyMatrix[i2][j1])

            cipherText.append(", ")

        i += 2  

    return cipherText


def main():

    key = input("Enter key: ").replace(" ","").upper()

    plainText =input("Plain Text: ").replace(" ","").upper()

    convertedPlainText = convertPlainTextToDiagraphs(plainText)
    
    cipherText = " ".join(encryption(convertedPlainText,key))

    print(cipherText)

if __name__ == "__main__":
    main()
              
