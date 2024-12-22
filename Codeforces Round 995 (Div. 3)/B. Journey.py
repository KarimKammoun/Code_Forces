t=int(input())


for i in range(t):

    l=list(map(int,input().split()))
    

    s=l[1]+l[2]+l[3]
    k=l[0]//s

    if l[0]<=(k*s):
        print(k*3)
    elif l[0]<=((k*s)+l[1]):
        print((k*3)+1)
    elif l[0]<=((k*s)+(l[2]+l[1])):
        print((k*3)+2)
    elif l[0]<= ((k*s)+(l[2]+l[1]+l[3])):
        print((k*3)+3)

