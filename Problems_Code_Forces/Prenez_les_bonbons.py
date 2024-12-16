t=int (input())
for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))
    paire=0
    impaire=0
    for c in range(len(liste)):
        if liste[c]%2==0:
            paire+=liste[c]
        else:
            impaire+=liste[c]
    if paire>impaire:
        print("yes")
    else:
        print("no")