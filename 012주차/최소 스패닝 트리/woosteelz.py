# 1197번 최소 스패닝 트리
import sys
input = sys.stdin.readline

INF = float('inf')

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
key = [INF for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

key[0] = 0

for i in range(V + 1):
    min_weight = INF
    min_node = -1

    for n in range(V + 1):
        if not visited[n] and key[n] < min_weight:
            min_weight = key[n]
            min_node = n

    visited[min_node] = True

    for node, val in graph[min_node]:
        if not visited[node] and key[node] > val:
            key[node] = val

key[V] = 0

print(sum(key))
