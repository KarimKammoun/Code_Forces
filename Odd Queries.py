t=int (input())
for i in range(t):
    n,q=(map(int,input().split()))
    liste=list(map(int,input().split()))
    s=0
    for j in range(len(liste)):
        s=s+liste[j]


    for c in range(q):
        if s%2==0:
            p=1
        else:p=-1
        l,r,k=(map(int,input().split()))
        for h in range(l-1,r,1):
            if liste[h]%2 != k%2:
                p=p*-1
        if p==1:
            print("no")
        else:
            print("yes")
