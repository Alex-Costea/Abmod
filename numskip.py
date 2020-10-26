from math import floor,log

def get_a_of_n(i):
    x=1+1/i
    j=i
    while floor(log(j,x))!=floor(log(j+1,x)):
        j+=1
    return floor(log(j,x))+1

def main():
    step=1
    i=2
    while True:
        y=get_a_of_n(i)
        print(y,end=", ")
        i+=step
