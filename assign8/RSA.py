import random

def generateKey():
    p=random.randint(2,999)
    q=random.randint(2,999)
    
    flag=isPrime(p)
    flag2=isPrime(q)
    if flag==0 and flag2==0:
        RSA(p,q)

    else:
        generateKey()

def RSA(p,q):
    print("{} and {} are prime numbers".format(p,q))
    #2nd step
    N=p*q
    
    #Finding E
    product=(p-1)*(q-1)        
    for i in range(1,99999):
        if (product%i!=0):
            E=i                
            break
    #Finding D
    for i in range(1,product-1):
        if(((i*E)%product)==1):
            D=i
            break
        
    print("N  is {}".format(N)) 
    print("product((p-1)*(q-1)) is {}".format(product))
    print("Encryption key is {}".format(E))
    print("Decryption key is {}".format(D))
    
    PT=[]
    pt=[]
    ct=[]
    CT=[]
    PT=input("Enter any text \n")
    for i in PT:
        #print(ord(i))
        pt.append(ord(i))	#removing -65
    print("Plain text is "+PT)
    
    for i in pt:
        ct.append((i**E)%N)
    
    print("cipher text in numbers is {}".format(ct))
    for i in ct:
        CT.append(chr(((i**D)%N)))	#removing +65
        
    print("Cipher text is :'",end="")
    for i in CT:
        print(i,end="")
    print("'")
    
def isPrime(num):
    flag=0
    r=int(num/2)
    for i in range(2,r):
        if(num%i==0):
            flag=1
            break

    return flag

N=0
E=0
D=0
generateKey()

