t=int (input())
for i in range(t):
    n=int(input())
    liste=[0]*100
    maxh=0
    maxl=0
    for j in range(n):
        l,h=(map(int,input().split()))
        if h>liste[l-1]:
            liste[l-1]=h
            if h>maxh:
                maxh=h
        if l>maxl:
            maxl=l
    print((maxl+maxh)*2)
