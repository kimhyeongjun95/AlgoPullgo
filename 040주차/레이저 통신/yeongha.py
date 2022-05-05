from collections import deque

def bfs(x, y):
    deq = deque([(x, y)])
    visited[x][y] = 0
    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            while True:
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != "*" and visited[nx][ny] >= visited[x][y] + 1:
                    deq.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    nx = nx + dx
                    ny = ny + dy
                else:
                    break


W, H = map(int, input().split())
board = [input() for _ in range(H)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

C = []
for i in range(H):
    for j in range(W):
        if board[i][j] == "C":
            C.append((i, j))

(sx, sy), (ex, ey) = C

visited = [[float("inf")] * W for _ in range(H)]
bfs(sx, sy)
print(visited)

print(visited[ex][ey] - 1)