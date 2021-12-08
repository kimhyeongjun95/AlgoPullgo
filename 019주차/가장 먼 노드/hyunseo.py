# 프로그래머스 가장 먼 노드

from collections import deque

def bfs(n, graph):
    queue = deque()
    queue.append((1, 0))
    
    visited = [0 for _ in range(n+1)]
    visited[1] = -1
    
    while queue:
        v, dist = queue.popleft()
        
        for w in graph[v]:
            if not visited[w]:
                visited[w] = dist+1
                queue.append((w, dist+1))
    
    cnt = 0
    for dist in visited:
        if dist == max(visited):
            cnt += 1
    
    return cnt


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    answer = bfs(n, graph)
    return answer