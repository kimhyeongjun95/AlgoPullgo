# 백준 1240 노드사이의 거리
from collections import deque

def distance(x, y):
    queue = deque()
    queue.append((x, 0))

    visited = [0 for _ in range(N+1)]
    visited[x] = 1

    while queue:
        v, d = queue.popleft()

        if v == y:
            return d

        for w, dist in graph[v]:
            if not visited[w]:
                visited[w] = 1
                queue.append((w, d+dist))


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    i, j, dist = map(int, input().split())

    graph[i].append((j, dist))
    graph[j].append((i, dist))

for _ in range(M):
    x, y = map(int, input().split())
    print(distance(x, y))