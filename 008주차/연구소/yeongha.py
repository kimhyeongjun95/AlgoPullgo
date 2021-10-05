from collections import deque
from itertools import combinations

def bfs(visited):
    global ans
    dxy = [(1,0),(0,1),(-1,0),(0,-1)]
    deq = deque()
    for item in virus:
        deq.append(item)
                
    while deq:
        x, y = deq.popleft()
        visited[x][y] == 1

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < N and -1 < ny < M and visited[nx][ny] == 0 and map[nx][ny] == 0:
                deq.append((nx, ny))
                visited[nx][ny] = 1
                
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and map[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)

def wall_func(wall):
    for items in combinations(wall, 3):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for i in items:
            x, y = i
            visited[x][y] = 2
        bfs(visited)


N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
ans = 0
virus = []
wall = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 2:
            virus.append((i,j))
        elif map[i][j] == 0:
            wall.append((i,j))
wall_func(wall)
print(ans)