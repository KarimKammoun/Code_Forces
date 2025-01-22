t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    test=True
    liste=[0]*((n*m)-1)
    p=[0]*n
    l=[0]*((n*m))
    for j in range(n):

        liste=[0]*((n*m))
        
        l1=list(map(int,input().split()))
        
        if test==True:
            for c in range(len(l1)):
                if l[l1[c]]==1:
                    test=False
                l[l1[c]]=1
                liste[l1[c]]=1
            c=0
            while c<len(liste) and liste[c]!=1:
                c=c+1  
            p[c]=j+1  
            for d in range(c,len(liste),n):
                
                if liste[d]!=1:
                    test=False
                    break
        else:
            continue
    
    if test==True :
        print(" ".join(map(str, p)))
    else:
        print(-1)

