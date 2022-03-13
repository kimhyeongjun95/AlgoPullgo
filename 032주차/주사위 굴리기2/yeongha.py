def dfs(x, y, n):
    c = 1
    visited = [[0] * M for _ in range(N)]
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == n:
                visited[nx][ny] = 1
                stack.append((nx, ny))
                c += 1
    return n*c

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dice = [1, 2, 3, 4, 5, 6]
x, y = 0, 0
score = 0
d = 0
for _ in range(K):
    dx, dy = dxy[d]
    x += dx
    y += dy
    if not 0 <= x < N or not 0 <= y < M:
        x -= dx*2
        y -= dy*2
        d = (d+2)%4
    

    if d == 0:
        dice[0], dice[3], dice[5], dice[2]= dice[3], dice[5], dice[2], dice[0]
    elif d == 1:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    elif d == 2:
        dice[2], dice[5], dice[3], dice[0] = dice[5], dice[3], dice[0], dice[2]
    else:
        dice[4], dice[5], dice[1], dice[0] = dice[5], dice[1], dice[0], dice[4]

    score += dfs(x, y, board[x][y])

    if dice[5] > board[x][y]:
        d = (d+1)%4
    elif dice[5] < board[x][y]:
        d = (d-1)%4
        
print(score)
