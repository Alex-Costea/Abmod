from math import *
from sympy import *
lastn=0
baseadd=10
x=0
i=1
while i<=100:
    y=lastn*baseadd+x
    if isprime(y):
        print(i,y)
        i+=1
        lastn=y
        x=0
        baseadd=10
    x+=1
    if x==baseadd:
        baseadd*=10
        x=1
