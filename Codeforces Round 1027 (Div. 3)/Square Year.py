from math import *
t=int (input())
 
for i in range(t):
    s=input()
 
    k=sqrt(int(s))
 
    if (k!=int(k)):
        print(-1)
    elif (k==0):
        print(0,0)
    elif (k==1):
        print(0,1)
    else:
        print(1,int(k)-1)