t=int (input())
for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))
    test=True
    for j in range(n):
        for c in range(j+1,n):
            if liste[c]==liste[j]:
                print("no")
                test=False
                break
        if test ==False:
            break
    if test==True:
        print("yes")