t=int (input())
for i in range(t):
    n=int(input())
    liste=list(map(int,input().split()))
    test=True
    for j in range(1,len(liste)):
        if ((liste[j]-liste[j-1])in[5,-5,7,-7])==False:
            test=False
            break
    if test==True:
        print("yes")
    else:
        print("no")