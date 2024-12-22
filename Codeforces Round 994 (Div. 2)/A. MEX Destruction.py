t=int(input())


for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))
    s=0
    k=-1
    test=True


    for j in range(n):
        if liste[j]==0:
            s=s+1
        else:
            if k==-1:
                k=j
                continue
            
            if j-k != 1:
                test=False
            k=j
    

    if s==n:
        print(0)
    elif  test==True:
        print(1)
    else:
        print(2)
