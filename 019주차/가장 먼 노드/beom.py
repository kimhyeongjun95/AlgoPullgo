from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    queue = deque()
    queue.append(1)


    def bfs():
        while queue:
            temp = queue.popleft()
            visited[temp] = True
            for j in graph[temp]:
                if visited[j] == False:
                    visited[j] = True
                    dist[j] = dist[temp] + 1
                    queue.append(j)
    bfs()
    answer = dist.count(max(dist))
    return answer