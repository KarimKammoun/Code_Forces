t=int(input())


for i in range(t):
    n,m,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))

    if (n-k)>=2:
        print('0'*m)
    elif (n-k)==1:
        for j in range(k):
            if l2[j]!=l1[j]:
                print(('0'*j)+'1'+'0'*(m-j-1))
                break
            if j==k-1:
                print(('0'*(j+1))+'1')
                break
    else:
        print('1'*m)