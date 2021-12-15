from collections import defaultdict, deque
def solution(N, road, K):
    dist = defaultdict(list)
    for a, b, c in road:
        dist[a].append((b,c))
        dist[b].append((a,c))

    visited = [0 for _ in range(N+1)]
    deq = deque([(1, 0)])
    visited[1] = 1
    while deq:
        x, d = deq.popleft()
        
        for v, w in dist[x]:
            if d + w <= K and (not visited[v] or d + w <= visited[v]):
                deq.append((v, d + w))
                visited[v] = d + w
                
    answer = N+1-visited.count(0)
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))