t=int(input())

for i in range(t):
    ch=input()
    ch=(ch[::-1])
    res=''
    for j in range(len(ch)):
        
        if ch[j]=='p':
            res=res+'q'
        elif ch[j]=='q':
            res=res+'p'
        else:
            res=res+'w'
    print(res)
