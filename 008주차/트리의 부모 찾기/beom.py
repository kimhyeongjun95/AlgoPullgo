import sys
input = sys.stdin.readline
from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if result[i] == 0:
                result[i] = v
                queue.append(i)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

result = [0]*(N+1)
bfs(1)

for i in range(2, N+1):
    print(result[i])