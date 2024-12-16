t=int (input())
for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))
    s=0
    max=liste[0]
    if (liste[0]==0):
        s=1
    for j in range(1,n):
        if liste[j]>max:
            max=liste[j]
        if max==(liste[j-1]-max+liste[j]) :
            s=s+1
        liste[j]=liste[j]+liste[j-1]
    print(s)



