t=int(input())

for i in range(t):
    n,m=map(int,input().split())

    test=True

    visited=[]

    res=[0 for i in range(n)]

    for j in range(n):
        
        liste=list(map(int,input().split()))
        liste.sort()
        
        if liste[0]<n:
            res[liste[0]]=j+1

        if liste[0] in visited:
            test=False
        visited.append(liste[0])
        if test==False:
            continue

        
        for j in range(1,m):
            if liste[j] != liste[j-1]+n:
                test=False
                break

    

    if test==True :
        print(" ".join(map(str, res)))
    else:
        print(-1)

