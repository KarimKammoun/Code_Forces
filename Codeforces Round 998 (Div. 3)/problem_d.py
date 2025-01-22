t=int(input())

for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    test=True

    for j in range(len(l1)-1):
        if l1[j]>l1[j+1]:
            test=False
            break
        else:
            l1[j+1]=l1[j+1]-l1[j]
            l1[j]=0
    if test==True :
        print("YES")
    else:
        print("NO")