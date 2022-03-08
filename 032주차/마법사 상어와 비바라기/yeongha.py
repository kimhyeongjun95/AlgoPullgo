import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dxy1 = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
dxy2 = [(-1, 1),(1, -1),(1, 1),(-1, -1)]
clouds = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for _ in range(M):
    d, c = map(int, sys.stdin.readline().split())
    is_cloud = [[0]*N for _ in range(N)]
    for _ in range(len(clouds)):
        x, y = clouds.popleft()
        dx, dy = dxy1[d-1]
        nx, ny = (x + dx*c)%N, (y + dy*c)%N
        board[nx][ny] += 1
        clouds.append((nx, ny))
        is_cloud[nx][ny] = 1
    
    for cloud in clouds:
        x, y = cloud
        cnt = 0
        for dx, dy in dxy2:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
                cnt += 1
        board[x][y] += cnt

    new_clouds = deque()
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not is_cloud[i][j]:
                board[i][j] -= 2
                new_clouds.append((i, j))

    clouds = new_clouds

total = 0
for i in range(N):
    total += sum(board[i])

print(total)