import sys

T = int(sys.stdin.readline())
stack = []

for tc in range(T):
    order = sys.stdin.readline().split()

    if order[0] == 'push' :
        stack.append(int(order[-1]))
    
    if order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    if order[0] == 'size':
        print(len(stack))
    
    if order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    if order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)