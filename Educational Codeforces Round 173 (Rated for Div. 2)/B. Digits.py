t = int(input())  
for _ in range(t):
    n, d = map(int, input().split())  
    ans = [] 
    ans.append(1)
    if n >= 3 or d % 3 == 0:
        ans.append(3)
    if d == 5:
        ans.append(5)
    if n >= 3 or (n == 2 and d == 7):
        ans.append(7)
    if n >= 6:
        ans.append(9)
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        if (factorial * d) % 9 == 0:
            ans.append(9)
 
    print(" ".join(map(str, ans)))