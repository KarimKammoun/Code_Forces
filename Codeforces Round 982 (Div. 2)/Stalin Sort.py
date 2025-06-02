t=int (input())
for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))

    min=n


    for j in range(n):
        k=j
        pres=liste[j]
        for c in range(j+1,n):
            if liste[c]>pres:
                k=k+1
        if k<min:
            min=k
    print(min)



