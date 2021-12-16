# 프로그래머스 배달

def solution(N, road, K):
    town = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for s, e, d in road:
        if town[s][e]:
            town[s][e] = min(town[s][e], d)
            town[e][s] = min(town[e][s], d)
        else:
            town[s][e] = d
            town[e][s] = d
    
    visited = [0 for _ in range(N+1)]
    
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0
    
    for _ in range(N):
        min_idx = -1
        min_val = float('inf')
        
        for i in range(1, N+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        
        visited[min_idx] = 1
        
        for i in range(1, N+1):
            if town[min_idx][i] and not visited[i]:
                distance[i] = min(distance[i], distance[min_idx]+town[min_idx][i])
        
    answer = 0
    for d in distance[1:]:
        if d <= K:
            answer += 1
            
    return answer