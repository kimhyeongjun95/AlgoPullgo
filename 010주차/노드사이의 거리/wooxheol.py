from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    dist[a][b] = d
    dist[b][a] = d

queue = deque()

for _ in range(m):
    start, end = map(int, input().split())
    queue.append(start)
    ans = [0 for _ in range(n+1)]
    while queue:
        curr = queue.popleft()
        for node in graph[curr]:
            if not ans[node]:
                queue.append(node)
                ans[node] += dist[curr][node] + ans[curr]
    print(ans[end])
