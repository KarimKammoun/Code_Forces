t = int(input()) 
for _ in range(t):
    s = input().strip()  
    stack = [] 
    for char in s:
        if stack and stack[-1] == char:
            stack.pop() 
        else:
            stack.append(char) 
    print(max(1, len(stack)))
