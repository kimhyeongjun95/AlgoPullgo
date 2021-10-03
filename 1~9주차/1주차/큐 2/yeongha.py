import sys
from collections import deque
N = int(sys.stdin.readline())

que = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    order = command[0]

    if order == "push":
        que.append(command[1])
    elif order == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif order == "size":
        print(len(que))
    elif order == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif order == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif order == "back":
        if que:
            print(que[-1])
        else:
            print(-1)