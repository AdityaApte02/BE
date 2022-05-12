
import random
def findPrimitiveRoots(q):
    flag=0
    s=set()
    roots=set()
   
    for i in range(1,q):
        for k in range(1,q):
            s.add(k)

        for j in range(1,q-1):
            if ((i**j) % q) in s:
                s.remove((i**j) % q)
                flag=1

            else:
                flag=0

        if flag==1:
            roots.add(i)

        s.clear()
    return roots

def getKeys(alpha,q,nums):
    Xa=random.choice(nums)

    Ya=(alpha**Xa) % q

    Xb=random.choice(nums)
    Yb=(alpha ** Xb) % q

    return Xa,Ya,Xb,Yb

def Check( Xa,Ya,Xb,Yb):
    SenderKey = (Yb ** Xa) % q
    ReceiverKey = (Ya ** Xb) % q

    if SenderKey==ReceiverKey:
        print("SenderKey ",SenderKey,"\n")
        print("Receiver Key ", ReceiverKey, "\n")
        print("Success")

    else:
        print("Some problem occured")

if __name__=="__main__":
    q = int(input("Enter a prime number \n"))
    roots=findPrimitiveRoots(q)
    print(roots)

    alpha= random.sample(roots,1)[0]
    print(alpha)

    nums=[i for i in range(1,q)]

    Xa,Ya,Xb,Yb=getKeys(alpha,q,nums)

    Check( Xa,Ya,Xb,Yb)




























#Attempt 1

# import random


# def findPrimitiveRoots(q):
#     roots=set()
#     s=set()
#     flag=0
#     for i in range(1,q):
#         for k in range(1,q):
#             s.add(k)

#         for j in range(1,q-1):
#             if (i ** j)%q in s:
#                 s.remove((i ** j)%q)
#                 flag=1

#             else:
#                 flag=0

#         if flag==1:
#             roots.add(i)

#     return roots

# def getKeys(q,alpha,nums):

#     Xa=random.choice(nums)

#     Ya= (alpha ** Xa) % q

#     Xb= random.choice(nums)

#     Yb=(alpha ** Xb) % q

#     return Xa,Ya,Xb,Yb

# def check(Xa,Ya,Xb,Yb):

#     senderKey= (Yb ** Xa) % q
#     receiverKey= (Ya ** Xb) % q


#     print("SenderKey: ",senderKey)
#     print("Receiver Key: ",receiverKey)
#     if senderKey==receiverKey:
#         print("success")

#     else:
#         print("Some error occured")

# if __name__=="__main__":
#     q = int(input("Enter a prime number q \n"))
#     roots=findPrimitiveRoots(q)
#     print(roots)

#     alpha=random.sample(roots,1)[0]
#     nums=[i for i in range(1,q)]

#     Xa,Ya,Xb,Yb=getKeys(q,alpha, nums)

#     check(Xa,Ya,Xb,Yb)
