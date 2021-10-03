from collections import deque


def bfs():
    q = deque()
    q.append((0,0,k))
    visit = [[[0 for _ in range(31)] for _ in range(m)] for _ in range(n)]
    while q:
        x,y,cnt = q.popleft()
        if x == (n - 1) and y == (m - 1):
            return visit[x][y][cnt]
        if cnt > 0:
            for i in range(8):
                nx,ny = x + dx_h[i], y + dy_h[i]
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0 and visit[nx][ny][cnt-1] == 0:
                    q.append((nx,ny,cnt-1))
                    visit[nx][ny][cnt-1] = visit[x][y][cnt] + 1

        for j in range(4):
            nx,ny = x + dx_m[j], y + dy_m[j]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0 and visit[nx][ny][cnt] == 0:
                q.append((nx, ny, cnt))
                visit[nx][ny][cnt] = visit[x][y][cnt] + 1

    return -1


k = int(input())
m, n = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

dx_m = [0,1,0,-1]
dy_m = [1,0,-1,0]
dx_h = [-2,-2,-1,-1,1,1,2,2]
dy_h = [-1,1,-2,2,-2,2,-1,1]

print(bfs())