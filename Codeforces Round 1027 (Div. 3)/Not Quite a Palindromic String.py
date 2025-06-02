t=int(input())
 
for i in range(t):
    n,k=(map(int,input().split()))
    s=input()
    nb1=0
    nb0=0
    for j in s:
        if int(j)==0:
            nb0+=1
        else:
            nb1+=1
    k=k*2
    while k!=0:
        k-=2
        if nb1>nb0:
            nb1=nb1-2
        else:
            nb0=nb0-2
    if nb1!=nb0:
        print("NO")
    else:
        print("YES")