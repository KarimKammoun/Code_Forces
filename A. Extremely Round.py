t=int(input())

for i in range(t):

    n=int(input())
    ch=str(n)
    if len(ch)>=3:
        s=int(ch[0])+(9*(len(ch)-2))+9
    elif len(ch)>=2:
        s=int(ch[0])+9
    else:
        s=int(ch[0])

    print(s)
