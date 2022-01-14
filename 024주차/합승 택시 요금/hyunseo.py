# 프로그래머스 합승 택시 요금

def solution(n, s, a, b, fares):
    def dijkstra(start, end):
        nonlocal temp
        
        visited = [0 for _ in range(n+1)]
        for t in temp:
            visited[t] = 1
        
        way = {start : [start]}
        
        dist = [float('inf') for _ in range(n+1)]
        dist[start] = 0
        
        for _ in range(n+1):
            min_idx = -1
            min_value = float('inf')
            
            for i in range(1, n+1):
                if not visited[i] and dist[i] < min_value:
                    min_idx = i
                    min_value = dist[i]
            
            if min_idx == end:
                return min_value
            
            visited[min_idx] = 1
            
            for j, d in graph[min_idx]:
                if dist[j] > dist[min_idx]+d:
                    dist[j] = dist[min_idx]+d
                    way[j] = way[min_idx] + [j]
                
        return 999999
            
                
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    
    answer = float('inf')
    for k in range(1, n+1):          
        temp = []
        cost = dijkstra(s, k) + dijkstra(k, a) +dijkstra(k, b)
        answer = min(answer, cost)
        
    return answer

print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))