t=int (input())
for i in range(t):
    liste=list(map(int,input().split()))
    s=0
    for j in range(len(liste)):
        s=s+liste[j]
    for j in range(len(liste)):
        if (s-liste[j])==liste[j]:
            print("yes")
            break
        if j==len(liste)-1:
            print("No")