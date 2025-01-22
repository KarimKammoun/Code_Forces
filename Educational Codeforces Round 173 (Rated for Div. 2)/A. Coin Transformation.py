t=int(input())


for i in range(t):
    n=int (input())
    s=1
    if n<=3:
        print(1)
    else:
        while True:
            n=n//4
            s=s*2
            if n<=3:
                break
        print(s)
