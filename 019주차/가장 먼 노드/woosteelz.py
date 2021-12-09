# Programmers 가장 먼 노드
from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited = [0 for _ in range(n+1)]

    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        curr = queue.popleft()
        for g in graph[curr]:
            if not visited[g]:
                visited[g] = visited[curr]+1
                queue.append(g)

    max_depth = max(visited)

    for i in range(n+1):
        if visited[i] == max_depth:
            answer += 1

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
