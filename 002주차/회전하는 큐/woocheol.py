# 1021번 회전하는 큐
from collections import deque

n, m = map(int, input().split())
queue = deque([i + 1 for i in range(n)])
pick = list(map(int, input().split()))
ans = 0

for num in pick:
    if queue[0] == num:
        queue.popleft()
        continue

    idx = queue.index(num)
    if idx < len(queue) // 2 + 1:
        while True:
            queue.append(queue.popleft())
            ans += 1
            if queue[0] == num:
                queue.popleft()
                break
    else:
        while True:
            queue.appendleft(queue.pop())
            ans += 1
            if queue[0] == num:
                queue.popleft()
                break
print(ans)
