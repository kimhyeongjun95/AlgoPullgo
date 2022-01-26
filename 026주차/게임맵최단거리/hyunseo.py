# 프로그래머스 게임 맵 최단거리

from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    queue = deque()
    queue.append((0, 0))
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]
        
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return -1