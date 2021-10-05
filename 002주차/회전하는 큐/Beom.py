import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
numbers = deque(list(map(int, input().split())))
queue = deque([i for i in range(1,N+1)])
count = 0

while numbers:
    if queue[0] == numbers[0]:
        queue.popleft()
        numbers.popleft()

    else:
        if queue.index(numbers[0]) < len(queue)/2:  
            while queue[0] != numbers[0]:
                queue.append(queue.popleft())
                count += 1

        else:
            while queue[0] != numbers[0]:
                queue.insert(0,queue.pop())
                # queue.appendleft(queue.pop())
                count += 1

print(count)