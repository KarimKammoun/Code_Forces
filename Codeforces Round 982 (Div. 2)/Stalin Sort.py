t=int (input())
for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))
    max=0
    res=[]
    for j in range(n):
        if liste[j]>=max:
            res.append(j)
            max=liste[j]
    
    l=len(res)
    for j in range(0,len(res)):
        res[j]=res[j]+l-(j+1)
        
    print(res)
    print(min(res))
    