# 백준 11725번 트리의 부모 찾기
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True
ans = [0 for _ in range(n+1)]

while queue:
    curr = queue.popleft()
    for g in graph[curr]:
        if not visited[g]:
            ans[g] = curr
            queue.append(g)
            visited[g] = True

for i in range(2, n+1):
    print(ans[i])
