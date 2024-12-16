t=int (input())
for i in range(t):
    n,k=(map(int,input().split()))
    liste=[0]*(k+1)
    for j in range(k):
        b,c=(map(int,input().split()))
        liste[b]+=c
    sum=0
    liste.sort()
    for k in range(k):
        sum=sum+liste[-1-k]
    print(sum)

