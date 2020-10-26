from decimal import *

def contFract(x):
    b=Decimal(x[-1])
    x=x[:-1]
    x=x[::-1]
    for i in x:
        b=i+(1/b)
    return b

getcontext().prec=100

##a=str(contFract([0,1,6,21,107,47176870]))
##x=Decimal((125 * 16**30341 + 1750 * 4**30340 + 15)//27 + 19885154163)
##x=(x+(x*x+4)**Decimal(0.5))/2
##b=str(contFract([0,1,6,21,107,47176870,x]))
##print(a==b)
##print(a)

print(contFract([0,1,6,21,107]))
print(contFract([0,1,6,21,107,47176870,47176871,47176872,47176873,47176874,47176875,47176876,47176877,47176878,47176879]))
