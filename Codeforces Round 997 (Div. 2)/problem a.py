t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    xf=0
    yf=0
    for j in range(n):

        x,y=map(int,input().split())
        if j==0:
            xf=m
            yf=m
            
        else:
            xf=xf+x
            yf=yf+y
    print((yf+xf)*2)