import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = list(sys.stdin.readline().split())
    # if command[0]== 'push':
    #     print(command)
    if command[0] == 'push':
        stack.append(command[1])
    
    elif command[0] == 'pop':
        if stack:
            popped = stack.pop()
            print(popped)
        else:
            print('-1')
    
    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')

    elif command[0] == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])

    # print(stack)