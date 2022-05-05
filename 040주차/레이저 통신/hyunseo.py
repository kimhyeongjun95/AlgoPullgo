# 백준 6087 레이저 통신

from collections import deque

def bfs(start):
    queue = deque([(start[0], start[1])])
    cnt[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            while True:

                if 0 <= nx < H and 0 <= ny < W and cnt[nx][ny] >= cnt[x][y]+1 and grid[nx][ny] != '*':
                    cnt[nx][ny] = cnt[x][y]+1
                    queue.append((nx, ny))

                    nx, ny = nx+dx, ny+dy
                else:
                    break


W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]

c = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'C':
            c.append((i, j))

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = [[float('inf') for _ in range(W)] for _ in range(H)]

bfs(c[0])

print(cnt[c[1][0]][c[1][1]] - 1)