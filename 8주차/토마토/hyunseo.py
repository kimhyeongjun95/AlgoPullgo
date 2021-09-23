# 백준 7569 토마토

from collections import deque

def bfs(h, i, j):
    dxyz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    while queue:
        z, x, y = queue.popleft()

        for dz, dx, dy in dxyz:
            nz, nx, ny = z+dz, x+dx, y+dy

            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append((nz, nx, ny))

    max_day = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if not box[h][i][j]:
                    return -1
                
                if box[h][i][j] > max_day:
                    max_day = box[h][i][j]
    
    return max_day -1


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                queue.append((h, i, j))

print(bfs(0, 0, 0))