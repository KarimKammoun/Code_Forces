t=int(input())

for i in range(t):
    res=[3,1,2,1,0,1,0,0,0,0]
    n=int(input())
    l1=list(map(int,input().split()))
    s=8
    test=False
    for i in range(n):
        if res[l1[i]]>0:
            s=s-1
            res[l1[i]]-=1
        if s==0:
            print(i+1)
            test=True
            break
    if test==False :
        print(0)