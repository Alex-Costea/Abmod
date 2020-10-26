from sympy import *
from math import *
from random import *

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def find_period(f):
    x=f(1)
    r=1
    while x!=1:
        x=f(x)
        r+=1
    return r

def factor(n,comments=False):
    if comments: print("check that",n,"is not 1 or prime")
    if n==1:
        if comments: print("1 is 1, returning")
        return []
    if isprime(n):
        if comments: print(n,"is prime, returning",n)
        return [n]
    for x in range(2,int(log(n,2))+1):
        if not isprime(x):
            continue
        if comments: print("check that",n,"is not a power of",x)
        l=round(log(n,x))
        if x**l==n:
            if comments: print(n,"is a power of",str(x)+", returning its factors")
            return [x]*l
    while True:
        a=randint(2,n-1)
        if comments: print("trying out a =",a)
        mygcd=gcd(n,a)
        if comments: print("greatest common divisor of",n,"and",a,"is",mygcd)
        if mygcd!=1 and mygcd!=n:
            if comments: print("gcd bigger than 1, factors "+str(mygcd)+", "+str(n//mygcd)+" found")
            return sorted(factor(mygcd,comments)+factor(n//mygcd,comments))
        #this part should be done using a quantum computer
        if comments: print("finding the period of",a,"^ x mod",n)
        r=find_period((lambda y:(y*a)%n))
        if comments: print("period is",r)
        if r%2==1:
            if comments: print(r,"is odd, trying another a")
            continue
        y=1
        for i in range(r//2):
            y=(y*a)%n
        if y%n==n-1:
            if comments: print(a,"^",r//2,"= -1 (mod "+str(n)+"), trying another a")
            continue
        break
    x1=gcd(y-1,n)
    x2=gcd(y+1,n)
    if x1!=n and x1>1:
        if comments: print("factors found: "+str(x1)+", "+str(n//x1))
        return sorted(factor(x1,comments)+factor(n//x1,comments))
    if x2!=n and x2>1:
        if comments: print("factors found: "+str(x2)+", "+str(n//x2))
        return sorted(factor(x2,comments)+factor(n//x2,comments))
