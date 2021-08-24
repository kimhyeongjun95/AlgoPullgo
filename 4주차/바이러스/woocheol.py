# 백준 문제번호 2606번 바이러스

import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = []
visited = [False for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph.append([a, b])
    graph.append([b, a])

queue = deque()
queue.append(1)

while queue:
    temp = queue.popleft()
    visited[temp] = True
    for a, b in graph:
        if a == temp and not visited[b]:
            queue.append(b)

print(visited.count(True)-1)
