# 백준 1966번 프린터 큐
import sys
from collections import deque

TC = int(sys.stdin.readline())

for _ in range(TC):
    N, idx = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))

    queue = deque(temp)
    cnt = 0
    while queue:
        if queue[0] == max(queue):
            if idx == 0:
                cnt += 1
                break
            else:
                queue.popleft()
                cnt += 1
                idx -= 1
                if idx < 0:
                    idx = len(queue)-1
        else:
            queue.append(queue.popleft())
            idx -= 1
            if idx < 0:
                idx = len(queue)-1
    print(cnt)
