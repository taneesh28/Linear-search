#from numpy import *
from array import *
#import numpy as np
n=int(input("enter the size on an array"))
arr = ([])
for i in range(n):
    x=int(input("enter its elements"))
    arr.append(x)
print(arr)
val=int(input("enter the value you want to see into your input values"))

#lsearch(arr,val)

def lsearch(arr,val):
    for i in range(n):
        if(arr[i]==val):
            print("we have found out your number",val,"at",arr[i],"value")
        else:
            print("value not found")

lsearch(arr,val)
