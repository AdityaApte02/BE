# P10 = (3,5,2,7,4,10,1,9,8,6)
# P8= (6,3,7,4,8,5,10,9)
# P4=(2,4,3,1)


# IP=(2,6,3,1,4,8,5,7)
# IPi=(4,1,3,5,7,2,8,6)

# E=(4,1,2,3,2,3,4,1)

# S0=[
#     [1,0,3,2],
#     [3,2,1,0],
#     [0,2,1,3],
#     [3,1,3,2]
# ]

# S1=[
#     [0,1,2,3],
#     [2,0,1,3],
#     [3,0,1,0],
#     [2,1,0,3]
# ]


# def permutation(pattern, key):
#     permuted=""
#     for i in pattern:
#         permuted=permuted+key[i-1]

#     return permuted

# def generate_first_key_k1(left,right):
#     left=left[1:]+left[:1]
#     right=right[1:]+right[:1]
#     key= left+right
#     return permutation(P8,key)

# def generate_second_key_k2(left,right):
#     left=left[3:]+left[:3]
#     right=right[3:]+right[:3]
#     key=left+right
#     return permutation(P8,key)

# def transform(right,key):
#     extended=permutation(E,right)
#     xor_cipher=bin(int(extended,2) ^ int(key,2))[2:].zfill(8)
#     print("xor_cipher: "+xor_cipher)
#     xor_left=xor_cipher[:4]
#     xor_right=xor_cipher[4:]

#     new_left=Sbox(xor_left,S0)
#     new_right=Sbox(xor_right,S1)

#     return permutation(P4,new_left+new_right)

# def Sbox(data,box):
#     row=int(data[0]+data[3],2)
#     column=int(data[1]+data[2],2)

#     return bin(box[row][column])[2:].zfill(4)

# def encrypt(left,right,key):
#     cipher=int(left,2) ^ int(transform(right,key),2)
#     return right, bin(cipher)[2:].zfill(4)

# key=input('Enter a 10 bit key')
# if len(key)!=10:
#     raise Exception("Check the input")

# plainText=input("Enter a 8 bit plaintext")
# if len(plainText)!=8:
#     raise Exception("Check the input")

# p10key=permutation(P10, key)
# print("p10key", p10key)

# left_key=p10key[:len(p10key)//2]
# right_key=p10key[len(p10key)//2:]
# print("\n\n")
# first_key=generate_first_key_k1(left_key,right_key)
# print("First key: "+first_key)
# print("\n\n")
# second_key=generate_second_key_k2(left_key,right_key)
# print("Second key: "+second_key)

# initialPermutation=permutation(IP,plainText)
# left_data=initialPermutation[:len(initialPermutation)//2]
# right_data=initialPermutation[len(initialPermutation)//2:]

# left,right = encrypt(left_data,right_data, first_key)
# left,right=encrypt(left,right,second_key)
# print("\n\n")
# print("CipherText: ", permutation(IPi, left+right))



#Attempt 1
P10=(5,3,10,6,1,7,2,4,9,8)
P8=(4,8,2,6,1,7,3,5)
P4=(2,4,1,3)

E=(1,3,2,4,3,4,1,2)

IP=(6,2,8,3,1,7,5,4)
IPi=(3,1,8,4,6,7,2,5)

S0=[
    [1,0,2,3],
    [2,1,3,0],
    [0,1,2,3],
    [2,1,2,0]
]

S1=[
    [3,1,3,2],
    [0,3,2,1],
    [1,2,3,0],
    [2,0,1,3]
]

def permutation(pattern, key):
    permuted=""
    for i in pattern:
        permuted=permuted+key[i-1]

    return permuted

def generate_key_k1(left,right):
    left=left[1:]+left[:1]
    right=right[1:]+right[:1]
    key=left+right

    return permutation(P8,key)

def generate_key_k2(left,right):
    left=left[3:]+left[:3]
    right=right[3:]+right[:3]
    key=left+right

    return permutation(P8,key)

def transform(right,key):
    extended=permutation(E,right)
    xor_cipher=bin(int(extended,2) ^ int(key,2))[2:].zfill(8)
    xor_left=xor_cipher[:4]
    xor_right=xor_cipher[4:]

    new_left=Sbox(xor_left,S0)
    new_right=Sbox(xor_right,S1)

    return permutation(P4, new_left+new_right)

def Sbox(data, box):
    row=int(data[0]+data[3], 2)
    column=int(data[1]+data[2],2)

    return bin(box[row][column])[2:].zfill(4)

def encrypt(left,right,key):
    cipher= int(left,2) ^ int(transform(right,key), 2)
    return right, bin(cipher)[2:].zfill(4)

if __name__=="__main__":
    plaintext=input("Enter a 8 bit plaintext \n")
    if len(plaintext)!=8:
        raise Exception("Please check your input \n")

    key=input("Enter a 10 bit key")
    if len(key)!=10:
        raise Exception("Please check your input")

    p10key=permutation(P10,key)
    print("p10 key: ",p10key)

    left_key=p10key[:len(p10key)//2]
    right_key=p10key[len(p10key)//2:]

    key1=generate_key_k1(left_key,right_key)
    print("key1: ",key1)
    print(len(key1))
    key2=generate_key_k2(left_key,right_key)
    print("key2: ",key2)

    initial_permutation=permutation(IP,plaintext)
    left_data=initial_permutation[:len(initial_permutation)//2]
    right_data=initial_permutation[len(initial_permutation)//2:]

    left,right=encrypt(left_data,right_data, key1)
    left, right=encrypt(left,right,key2)

    print("Cipher Text is: ",permutation(IPi, left+right))





