# 백준 1600 말이 되고픈 원숭이

from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j, 0))

    visited = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
    visited[i][j][0] = 1

    dxy1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dxy2 = [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (-1, 2), (1, -2), (-1, -2)]

    while queue:
        curr_x, curr_y, cnt = queue.popleft()

        if curr_x == H-1 and curr_y == W-1:
            return visited[curr_x][curr_y][cnt] - 1

        if cnt < K:
            for dx, dy in dxy2:
                nx, ny = curr_x + dx, curr_y + dy

                if 0 <= nx <= H-1 and 0 <= ny <= W-1 and visited[nx][ny][cnt+1] == 0 and board[nx][ny] == 0:
                    visited[nx][ny][cnt+1] = visited[curr_x][curr_y][cnt] + 1
                    queue.append((nx, ny, cnt+1))
        
        for dx, dy in dxy1:
            nx, ny = curr_x + dx, curr_y + dy

            if 0 <= nx <= H-1 and 0 <= ny <= W-1 and visited[nx][ny][cnt] == 0 and board[nx][ny] == 0:
                visited[nx][ny][cnt] = visited[curr_x][curr_y][cnt] + 1
                queue.append((nx, ny, cnt))
        
    return -1


K = int(input())
W, H = map(int, input().split())

board = []
for _ in range(H):
    board.append(list(map(int, input().split())))

print(bfs(0, 0))
