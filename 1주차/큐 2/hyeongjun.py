import sys
from collections import deque

n = int(sys.stdin.readline())
# n = int(input())
# queue = []
queue = deque()
for i in range(n):
    command = sys.stdin.readline().split()
    # command = input().split()
    # print(queue)
    
    if command[0] == 'push':
        queue.append(int(command[1]))
    
    if command[0] == 'pop':
        if queue:
            # popped = queue.pop(0)
            # print(popped)

            # print(queue[0])
            # queue = queue[1:]

            # print(queue[0])
            # queue.remove(queue[0])
            
            # print(queue[0])
            # del queue[0]
            popped = queue.popleft()
            print(popped)
        else:
            print(-1)

    if command[0] == 'size':
        print(len(queue))
    
    if command[0] == 'empty':
        if queue:
            print(0)
        else: # 큐가 비어있으면
            print(1)
    
    if command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    
    if command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)