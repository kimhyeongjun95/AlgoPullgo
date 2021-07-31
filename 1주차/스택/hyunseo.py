import sys
    
N = int(sys.stdin.readline())

stack = []

for _ in range(N) :
    command = sys.stdin.readline()[:-1]

    if 'push' in command :
        number = int(command.split()[-1])
        stack.append(number)

    elif command == 'pop' :
        if stack :
            print(stack.pop())
        else :
            print(-1)

    elif command == 'size' :
        print(len(stack))

    elif command == 'empty' :
        if stack :
            print(0)
        else :
            print(1)

    elif command == 'top' :
        if stack :
            print(stack[-1])
        else :
            print(-1)