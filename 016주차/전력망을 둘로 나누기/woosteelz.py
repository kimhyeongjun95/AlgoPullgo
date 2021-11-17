from collections import deque


def solution(n, wires):
    answer = []

    def bfs(node, x, y):
        queue = deque()
        queue.append(node)
        visited[node] = True
        while queue:
            curr = queue.popleft()
            for next_node in graph[curr]:
                if not visited[next_node] and not sorted([curr, next_node]) == sorted([x, y]):
                    queue.append(next_node)
                    visited[next_node] = True

    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [False for _ in range(n+1)]
        for i in range(1, n+1):
            if not visited[i]:
                bfs(i, a, b)
                break
        answer.append(abs(sum(visited) - (n-sum(visited))))

    return min(answer)
