t=int (input())
for i in range(t):
    n,s,m=(map(int,input().split()))
    k=0
    d=0
    for j in range(n):
        c,r=(map(int,input().split()))
        if (c-k)>d:
            d=c-k
        k=r
    if (d>=s) or (m-k)>=s:
        print("YES")
    else:
        print("NO")


