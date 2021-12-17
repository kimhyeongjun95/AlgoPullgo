from collections import deque


def solution(N, road, K):
    visited = [100000000 for _ in range(N+1)]
    town = [[] for _ in range(N+1)]
    queue = deque()
    queue.append([1, 0])

    for a, b, c in road:
        town[a].append([b, c])
        town[b].append([a, c])

    while queue:
        curr, curr_cost = queue.popleft()
        for node, cost in town[curr]:
            if curr_cost + cost <= visited[node]:
                visited[node] = curr_cost + cost
                queue.append([node, visited[node]])
    ans = 1
    for i in range(2, len(visited)):
        if visited[i] <= K:
            ans += 1
    # print(visited)
    return ans
