import sys
from itertools import combinations
from collections import deque

def bfs(list1):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    queue = deque(virus)
    visited = [[0] * M for _ in range(N)]
    for l in list1:
        visited[l[0]][l[1]] = 1
    for w in wall:
        visited[w[0]][w[1]] = 1
    for q in queue:
        visited[q[0]][q[1]] = 1
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if area[ni][nj] == 0 and visited[ni][nj] == 0:
                    queue.append([ni, nj])
                    visited[ni][nj] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                cnt += 1
    return cnt
        

N, M = map(int, sys.stdin.readline().split())

area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

empty = []
virus = []
wall = []
for i in range(N):
    for j in range(M):
        if area[i][j] == 0:
            empty.append([i, j])
        elif  area[i][j] == 2:
            virus.append([i, j])
        else:
            wall.append([i, j])

combination = list(combinations(empty, 3))

result = -1
for c in combination:
    if bfs(c) > result:
        result = bfs(c)

print(result)