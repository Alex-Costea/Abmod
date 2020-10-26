from sympy import isprime
from functools import reduce
from math import *

x=0
i=1
while i<15:
    x=ceil(log(factorial(i),2))
    print(x,end=", ")
    i+=1
