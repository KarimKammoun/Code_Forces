t=int (input())
for i in range(t):
    s1,s2=(map(str,input().split()))
    print(s2[0]+s1[1::]+" "+s1[0]+s2[1::])