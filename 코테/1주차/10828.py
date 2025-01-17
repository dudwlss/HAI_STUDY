import sys
input = sys.stdin.readline

stack = []

N = int(input())

for _ in range(N):
    command = input().strip()  

    if "push" in command:
        X = int(command.split()[1])  
        stack.append(X)  
    elif command == "pop":
        if stack:  
            print(stack.pop(-1))  
        else:
            print(-1) 
    elif command == "size":
        print(len(stack))  
    elif command == "empty":
        print(0 if stack else 1)  
    elif command == "top":
        if stack:  
            print(stack[-1])  
        else:
            print(-1)  
