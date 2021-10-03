# 바이러스
from collections import defaultdict

def dfs(G, root):
    visited = []
    stack = [root]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v) 
            stack += G[v] - set(visited)  # 연결된 노드 중 방문한 노드를 빼고 stack에 추가
    return len(visited)-1

V = int(input())
E = int(input())

network = defaultdict(set)
for _ in range(E):
    n, m = map(int,input().split())
    network[n].add(m)
    network[m].add(n) # 무방향 그래프이기 때문

print(dfs(network, 1))