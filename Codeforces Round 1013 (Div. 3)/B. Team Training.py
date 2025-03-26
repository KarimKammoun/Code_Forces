t=int(input())

for i in range(t):
    res=[3,1,2,1,0,1,0,0,0,0]
    n,x=map(int,input().split())
    l1=list(map(int,input().split()))
    s=0
    l2=[]
    for i in range(len(l1)):
        if l1[i]>=x:
            s=s+1
        else:
            l2.append(l1[i])
    
    if len(l2)>0:
        s=s+1

    print(s)