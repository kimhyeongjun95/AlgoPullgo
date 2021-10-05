# 백준 문제번호 2606번 바이러스
import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

while queue:
    curr = queue.popleft()
    visited[curr] = True
    for n in graph[curr]:
        if not visited[n]:
            queue.append(n)

print(visited.count(True)-1)
