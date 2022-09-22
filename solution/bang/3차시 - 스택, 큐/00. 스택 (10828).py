import sys
N = int(sys.stdin.readline())

stack = []

for i in range(N):
    arr = sys.stdin.readline().split()
    func = arr[0]
    
    if(func == "push"):
        stack.append(arr[1])
    elif(func == "pop"):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif(func == "size"):
        print(len(stack))
    elif(func == "empty"):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif(func == "top"):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])