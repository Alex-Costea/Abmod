import json

d=dict()
myMax=0
maxn=1000
for sum in range(0,2*maxn+1):
    for x in range(0,sum+1):
        y=sum-x
        if y>maxn:
            continue
        if x>maxn:
            break
        #print(x,y)
        if (x,y) not in d:
            z=(x,y)
            while z not in d:
                znew=(z[1],(z[0]*z[1])%(z[0]+z[1]+1))
                d[z]=znew
                z=znew
                if z[1]>myMax:
                    myMax=z[1]

