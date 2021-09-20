# BOJ 7569번 토마토
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split()))
          for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

dir_x = [1, -1, 0, 0, 0, 0]
dir_y = [0, 0, 1, -1, 0, 0]
dir_z = [0, 0, 0, 0, 1, -1]

queue = deque()


def BFS():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            nz = z + dir_z[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if not visited[nx][ny][nz] and graph[nx][ny][nz] == 0:
                    queue.append([nx, ny, nz])
                    visited[nx][ny][nz] = True
                    graph[nx][ny][nz] = graph[x][y][z] + 1


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1 and not visited[i][j][k]:
                queue.append([i, j, k])
                visited[i][j][k] = True

BFS()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                sys.exit()


ans = 0
for i in graph:
    for j in i:
        list_max = max(j)
        ans = max(ans, list_max)
print(ans-1)
