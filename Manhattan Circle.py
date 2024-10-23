t = int(input())  
for i in range(t):
    n, m = map(int, input().split()) 
    s = 0
    ci = 0
    total_rows = 0
    first_found = False
    for j in range(n):
        liste = list(input())  
        if "#" in liste:
            current_ci = liste.index("#")  
            if not first_found:
                ci = current_ci 
                first_found = True
            s += j 
            total_rows += 1  
    if total_rows > 0:
        mid_row = s // total_rows 
        print(mid_row+1,ci+1)
    