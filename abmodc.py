import json
import itertools
 
def brent_length(f, x0):
    # main phase: search successive powers of two
    hare = x0
    power = 1
    while True:
        tortoise = hare
        for i in range(1, power+1):
            hare = f(hare)
            if tortoise == hare:
                return i
        power *= 2
 
def brent(f, x0):
    lam = brent_length(f, x0)
 
    # Find the position of the first repetition of length lam
    mu = 0
    hare = x0
    for i in range(lam):
    # range(lam) produces a list with the values 0, 1, ... , lam-1
        hare = f(hare)
    # The distance between the hare and tortoise is now lam.
 
    # Next, the hare and tortoise move at same speed until they agree
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
 
    return lam, mu
 
def iterate(f, x0):
    while True:
        yield x0
        x0 = f(x0)
        
f = lambda z: (z[1],(z[0]*z[1])%(z[0]+z[1]+1))
x0=0
while True:
    if x0%100000==0:
        print(x0)
    lam, mu = brent(f, (x0,x0))
    if mu==0:
        print("Zero found:",x0)
    x0+=1
