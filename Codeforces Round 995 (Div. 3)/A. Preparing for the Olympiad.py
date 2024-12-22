t=int(input())


for i in range(t):
    n= int (input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    s=0
    for j in range(n-1):
        if l1[j]>l2[j+1]:
            s=s+(l1[j]-l2[j+1])
    s=s+l1[-1]
    print(s)