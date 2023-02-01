def modInverse(A, M):
 
    for X in range(1, M):

        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1
 

while __name__ == "__main__":
    A = int(input("Enter number: "))
    M = int(input("Enter mod: "))
 
    # Function call
    print("")
    print("Multiplicative inverse:",modInverse(A, M))
    print("")
