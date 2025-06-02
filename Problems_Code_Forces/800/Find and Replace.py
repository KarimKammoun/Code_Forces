t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    dic={}
    test=True
    for j in range(0,n,2):
        if s[j] in dic:
            dic[s[j]]+=1
        else:
            dic[s[j]]=1
    for c in range(1,n,2):
        if s[c]in dic:
            print("no")
            test=False
            break
    if test==True:
        print("yes")

        
