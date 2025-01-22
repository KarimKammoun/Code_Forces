t=int(input())

for i in range(t):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    p=[0]*(2*n)
    oc=[0]*(n*2)
    for j in range(len(l1)):
        p[l1[j]]=1
        oc[l1[j]]=oc[l1[j]]+1
    res=0
    for j in range(len(p)):
        if p[j]==1 and k>j and p[k-j]==1:
            res=res+1
            oc[k-j]=oc[k-j]-1
            oc[j]=oc[j]-1
            if oc[j]==0:
                p[j]=0
            if oc[k-j]==0:
                p[j]=0
    if (n%2==1 and oc[0]==0):
        print(res-1)
    else:
        print(res)



