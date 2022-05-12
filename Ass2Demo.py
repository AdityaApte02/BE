import math
import sys

sys.setrecursionlimit(5000)
def rsa(p,q,plainText):
    n = p * q
    z = (p-1) * (q-1)

    e=find_public_e(z)
    d=find_private_d(e,z)


    cipher_text=""
    for ch in plainText:
        ch=ord(ch)
        cipher_text=cipher_text+chr((ch ** e) % n)



    plaintext=""
    for ch in cipher_text:
        ch =ord(ch)
        plaintext=plaintext+chr((ch ** d) % n)

    return cipher_text, plaintext


def find_public_e(z):
    e=2
    while e < z:
        if gcd(e,z)==1:
            return e

        e=e+1
        

def find_private_d(e,z):
    d=2
    while d < z:
        if ((d * e) % z)==1:
            return d
        
        d=d+1

def gcd(x,y):
    if x==0:
        return y

    if y==0:
        return x

    if x==y:
        return x

    if x > y:
        return gcd(x-y,y)

    return gcd(x,y-x)





if __name__=="__main__":
    p,q=map(int, input("Enter the numbers p nad q \n").split())
    plainText=input("Enter the plainText \n")

    cipher_text, plaintext=rsa(p,q,plainText)

    print("Cipher_text: ",cipher_text)
    print("Decrypted Plain text: ",plaintext)


# print(gcd(89,97))

























#Attempt 1
import math
import sys
import sympy as prime

sys.setrecursionlimit(5000)
def rsa(p,q,plaintext):
    n = p * q
    z = (p-1) * (q-1)

    e=find_public_e(z)

    d=find_private_d(e,z)

    ciphertext=""
    for ch in plaintext:
        ch=ord(ch)
        ciphertext=ciphertext+chr((ch**e)%n)

    plain_text=""
    for ch in ciphertext:
        ch=ord(ch)
        plain_text=plain_text+chr((ch**d) % n)

    return plain_text, ciphertext




def find_public_e(z):
    e=2
    while e < z:
        if gcd(e,z)==1:
            return e

        e=e+1

def find_private_d(e,z):
    d=2
    while d < z:
        if ((d*e)%z)==1:
            return d

        d=d+1

def gcd(x,y):
    if x==0:
        return y

    if y==0:
        return x

    if x==y:
        return x
    
    if (x > y):
        return gcd(x-y,y)

    return gcd(x,y-x)



if __name__=="__main__":
    while True:
        p,q=map(int, input("Enter 2 large prime numbers \n").split(" "))

        if prime.isprime(p) and prime.isprime(q):
            break

        else:
            print("Please enter prime numbers only")
            continue

    plaintext=input("Enter the plaintext \n")
    plain_text, ciphertext=rsa(p,q,plaintext)


    print("Ciphertext: ", ciphertext, "\n")
    print("Decrypted Plaintext: ",plain_text,"\n")
    


    if plain_text==plaintext:
        print("Success")
       

    else:
        print("Something went wrong")

    


    
    