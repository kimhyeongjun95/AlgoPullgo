from collections import deque

def solution(n, edge):
    adj_list = [[] for _ in range(n+1)]
    for e in edge:
        start = e[0]
        end = e[1]
        adj_list[start].append(end)
        adj_list[end].append(start)
    
    def bfs():
        nonlocal result
        result = [0] * (n + 1)
        queue = deque([[1, 0]])
        visited = [False] * (n + 1)
        visited[1] = True

        while queue:
            node, dist = queue.popleft()
            if node != 1:
                result[node] = dist
            for i in adj_list[node]:
                if visited[i] == False:
                    queue.append([i, dist + 1])
                    visited[i] = True

    result = []
    bfs()
    max_result = max(result)
    answer = result.count(max_result)
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))