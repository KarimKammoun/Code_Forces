t=int(input())


for i in range(t):
    a1,a2,a4,a5=map(int,input().split())
    res=1
    a3=a1+a2
    if a3+a2==a4:
        res=res+1
    if a3+a4==a5:
        res=res+1
    r=1
    a3=a5-a4
    if a3+a2==a4:
        r=r+1
    if a1+a2==a3:
        r=r+1
    if res>r:
        print(res)
    else:
        print(r)


