t=int(input())

for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))

    last=l1[0]
    res=1
    for j in range (0,n-1):
        
        if last+1<l1[j+1]:
            res+=1
            last=l1[j+1]
    print(res)
