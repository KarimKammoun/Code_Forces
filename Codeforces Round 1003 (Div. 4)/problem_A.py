t=int(input())

for i in range(t):
    ch=input()
    if ch[-3:-1]=="us":
        ch=ch[:-3]+"i"
        print(ch)
    else:
        ch=ch[:-2]+"i"
        print(ch)

