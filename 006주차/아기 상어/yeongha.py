# 아기 상어
from collections import deque

def bfs(start, shark):
    global N
    t = 0

    flag1 = False
    for i in range(N):
        for j in range(N):
            if 0 < sea[i][j] < shark:
                flag1 = True
                break
        if flag1:
            break
    if not flag1:
        return 0, 0

    dxy = [(-1,0),(0,-1),(0,1),(1,0)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    fish = [[0 for _ in range(N)] for _ in range(N)]
    x, y = start
    q = deque([(x, y)])
    sea[x][y] = 0
    flag2 = flag3 = False
    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < N and -1 < ny < N and sea[nx][ny] <= shark and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] +1
                if flag2 and visited[nx][ny] > distance:
                    flag3 = True
                    break
                q.append((nx, ny))
                if 0 < sea[nx][ny] < shark:
                    distance = visited[nx][ny]
                    fish[nx][ny] = 1
                    flag2 = True
        if flag3:
            break
        
    
    if flag2:
        for i in range(N):
            for j in range(N):
                if fish[i][j]:
                    sea[i][j] = 0
                    return (i,j), visited[i][j]
    return 0, t
                    

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if 9 in sea[i]:
        x, y = i, sea[i].index(9)

start = (x, y)
time = 0
shark = 2
cnt = 0
while start:
    start, t = bfs(start, shark)
    time += t
    cnt += 1
    if shark == cnt:
        shark += 1
        cnt = 0
print(time)
