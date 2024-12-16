t=int (input())
for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))
    u=0
    z=0
    for j in range(len(liste)):
        if liste[j]==0:
            z=z+1
        else:
            u=u+1
    print((u%2),min(u,z))