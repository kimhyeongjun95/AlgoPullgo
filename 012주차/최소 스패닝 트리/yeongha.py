import heapq
from collections import defaultdict

def find_MST(s):
    global ans
    visited[s] = 1
    candidate = edges[s]
    heapq.heapify(candidate)

    while candidate:
        w, n = heapq.heappop(candidate)

        if not visited[n]:
            visited[n] = 1
            ans += w
            
            for edge in edges[n]:
                if not visited[edge[1]]:
                    heapq.heappush(candidate, edge)

V, E = map(int, input().split())
edges = defaultdict(list)
for _ in range(E):
    n1, n2, w = map(int, input().split())
    edges[n1].append((w, n2))
    edges[n2].append((w, n1))
visited = [0] * (V+1)
ans = 0
find_MST(1)
print(ans)
