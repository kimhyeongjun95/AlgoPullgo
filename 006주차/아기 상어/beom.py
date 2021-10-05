import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    queue = deque()
    queue.append([i, j])
    dxy = ((0, 1), (1, 0), (0, -1), (-1, 0)) 

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if matrix[ny][nx] == 0:
                    queue.append((ny, nx))
                if matrix[ny][nx] == 3:
                    return 1
    return 0



N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            sy, sx = i, j

print('#{} {}'.format(tc, bfs(sy, sx)))

