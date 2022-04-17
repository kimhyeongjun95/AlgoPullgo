# 백준 2206 벽 부수고 이동하기

from collections import deque

N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, list(input()))))

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque([(0, 0, 0)])

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

answer = float('inf')

while queue:
    x, y, z = queue.popleft()
    if x == N-1 and y == M-1:
        answer = min(answer, visited[x][y][z])
        break

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M:
            if not grid[nx][ny] and not visited[nx][ny][z]:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            
            if not z and grid[nx][ny] and not visited[nx][ny][1]:
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))

if answer == float('inf'):
    print(-1)
else:
    print(answer)