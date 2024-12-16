t=int(input())

for i in range(t):
    m,a,b,c=map(int,input().split())

    s=0
    if a>=m:
        s=s+m
    else:
        s=s+a
    if b>=m:
        s=s+m
    else:
        s=s+b
    if (s+c)>=(m*2):
        s=m*2
    else:
        s=s+c
    print(s)
    