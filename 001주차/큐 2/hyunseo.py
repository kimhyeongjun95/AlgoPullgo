import sys
# from collections import deque

N = int(sys.stdin.readline())

que = []
# que = deque([])
# que = ''

# append = que.append
# pop = que.pop

cnt = 0

for _ in range(N) :
    input = sys.stdin.readline()
    command = input.split()

    if command[0] == 'push' :
        que.append(command[1])
    elif command[0] == 'pop' :
        if len(que) > cnt :
            # print(que.pop(0))

            # print(que[0])
            # que = que[1:]

            # print(que.popleft())
            print(que[cnt])
            cnt += 1
        else :
            print(-1)
    elif command[0] == 'size' :
        print(len(que)-cnt)
    elif command[0] == 'empty' :
        if len(que) > cnt :
            print(0)
        else :
            print(1)
    elif command[0] == 'front' :
        if len(que) > cnt :
            print(que[cnt])
        else :
            print(-1)
    elif command[0] == 'back' :
        if len(que) > cnt :
            print(que[-1])
        else :
            print(-1)
