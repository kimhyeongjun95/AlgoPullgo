# 알고스팟

import sys
from collections import deque

def BFS(graph):
    dxy = [(1,0), (-1,0), (0,1), (0,-1)]
    q = deque([(0,0)])
    
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            if -1 < nx < M and -1 < ny < N and AOJ[nx][ny] == -1:
                if graph[nx][ny] == '0':
                    q.appendleft((nx, ny))
                    AOJ[nx][ny] = AOJ[x][y]
                else:
                    q.append((nx, ny))
                    AOJ[nx][ny] = AOJ[x][y]+1

N, M = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline() for _ in range(M)]
 
AOJ = [[-1 for _ in range(N)] for _ in range(M)]
AOJ[0][0] = 0
BFS(graph)
print(AOJ[M-1][N-1]-1)