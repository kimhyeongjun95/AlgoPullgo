# 프로그래머스 배달

from collections import deque
def dijkstra(start, graph, N, K):
    queue = deque([])
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    queue.append((0, start))
    
    while queue:
        long, now = queue.popleft()
        # 방문했다면
        if distance[now] < long:
            continue 

        for i in graph[now]:
            time = long + i[1]
            # 갱신
            if time < distance[i[0]]:
                distance[i[0]] = time
                queue.append((time, i[0]))

    count = 0
    for i in distance:
        if i <= K:
            count += 1
    return count

def solution(N, road, K):
    
    graph = [[] for _ in range(N+1)]
    
    for r in road:
        a, b, far = r
        graph[a].append((b,far))
        graph[b].append((a,far))

    answer = dijkstra(1, graph, N, K)
    return answer
    
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4