

t=int(input())


for i in range(t):
    n,x,y=map(int,input().split())
    l1=list(map(int,input().split()))
    
    s=sum(l1)

    l2=[]
    for j in range(n):
        l2.append(s-l1[j])

    res=0
    for j in range(n):
        for c in range(j+1,n):
            if  (x<=(l2[c]-l1[j])<=y):
                res=res+1
                
    print(res)